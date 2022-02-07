from multiprocessing import Manager, Pool
import os
from src.infraestructure.adapters.meli.sellerProxy import SellerProxy
from src.domain.site import Site
from src.infraestructure.adapters.meli.categoryProxy import CategoryProxy
from src.infraestructure.adapters.meli.itemProxy import ItemProxy
from src.infraestructure.adapters.meli.currencyProxy import CurrencyProxy
from src.infraestructure.adapters.files.JSONItemsFileLoader import JSONItemsFileLoader
from src.infraestructure.adapters.files.TXTItemsFileLoader import TXTItemsFileLoader
from src.infraestructure.adapters.files.itemsFileLoader import ItemsFileLoader
from src.infraestructure.adapters.files.CSVItemsFileLoader import CSVItemsFileLoader
from src.application.repository.itemResumeRepository import ItemResumenRepository
from src.infraestructure.adapters.db.repository.mysqlParameterRepository import MySQLParameterRepository
from src.infraestructure.adapters.db.repository.mysqlItemResumenRepository import MySQLItemResumenRepository
from src.application.service.IItemsProcessFileService import IItemsProcessFileService
from src.utils import constans
from datetime import datetime

"""instancia del repositorio especifico para almacenar los registros en la base de datos"""
itemResumenRepository = MySQLItemResumenRepository()
"""instancia del repositorio especifico para consultar los parametros respectivos para realizar la logica de negocio"""
parameterRepository = MySQLParameterRepository()

"""Se instancia los proxies respectivos que permiten traer la informacion de las APIS externas"""
currencyProxy = CurrencyProxy()
categoryProxy = CategoryProxy()
itemProxy = ItemProxy()
sellerProxy = SellerProxy()

"""Contiene las instancias de los diferentes tipo de file loaders que permite realizar la lectura de los archivos"""
itemsFileLoaderPoolList = []




class ItemsProcessFileServiceImp (IItemsProcessFileService):
    """Esta clase es la implementacion concreta de la logica de negocio la cual se define en su respectiva interface """
    

    def __init__(self):
        """Se determina que esta clase de logica debe tener instanciado por defecto los posibles tipos de archivos y mantenerlos en con contenedor para su respectiva reutilizacion"""
        itemsFileLoaderCSV = CSVItemsFileLoader()
        itemsFileLoaderTXT = TXTItemsFileLoader()
        itemsFileLoaderJSON = JSONItemsFileLoader()
        itemsFileLoaderPoolList.append(itemsFileLoaderCSV)
        itemsFileLoaderPoolList.append(itemsFileLoaderTXT)
        itemsFileLoaderPoolList.append(itemsFileLoaderJSON)
        

    """Descripción de la función
        Esta funcion contiene la logica de orquestar la diferentes validaciones e integraciones con los repositorios para consultar y almacenar y logica de negocio
        Parameters
        ----------
        parametro_1 : file
           Contiene la informacion que sera leiada en el formato de archivo que ha sido recivida por el controlador del servicio
        parametro_2 : contentType
            Contiene el contentType estandar del tipo de archivo que fue enviado
        Returns
        -------
        mensaje
            Devuelve un mensaje general con la informacion de la carga exitosa del archivo o mensaje de error
            TODO:realizar un manejo adecuado de las respuesta de los metodos para poder espeficiar codigos de error de negocio
    """
    def processItemsFile(self, file, contentType):
       
        """Se consulta los content types permitidos en la configuracion"""
        allowsParamtersFormatFiles = parameterRepository.queryByCodeValue(
            constans.ALLOW_FORMAT_ITEM_FILE_PARAMETER_CODE, contentType)
        if(len(allowsParamtersFormatFiles) > 0):
            """Se consulta los delimitadores de archivo asociados al content type"""
            delimiterContentTypeConfiguration = parameterRepository.queryByCode(
                constans.DELIMITER_PARAMETER_NAME+contentType.upper())
            """Se consulta el content type en la configuracion para ese content type"""
            encodingContentTypeConfiguration = parameterRepository.queryByCode(
                constans.ENCODING_PARAMETER_NAME+contentType.upper())
            for fileLoader in itemsFileLoaderPoolList:
                """Se determinar cual file loader se debe usar dependiento del content type"""
                if(fileLoader.contentType == contentType):
                    fileToProcess = fileLoader.saveFileToLocalStore(file)
                    if(len(delimiterContentTypeConfiguration) > 0):
                        fileLoader.delimiter = delimiterContentTypeConfiguration[0].value
                       
                    if(len(encodingContentTypeConfiguration) > 0):
                        fileLoader.encoding = encodingContentTypeConfiguration[0].value
                        """Contiene los objetos de dominio resultado de la lectura del archivo por medio del fileloader"""
                        itemsToComplement = fileLoader.fileRowsToObjects(
                            fileToProcess)

                        if(len(itemsToComplement)>0):

                            urlItem = parameterRepository.queryByCode(
                                constans.MELI_API_ITEM_ENDPOINT_PARAMETER_NAME)[0].value

                            for itemToComplete in itemsToComplement:
                                itemToComplete.setItemEndPoint(urlItem)

                            fileLoader.deleteItemsFile()

                            urlCurrencies = parameterRepository.queryByCode(
                                constans.MELI_API_CURRENCY_ENDPOINT_PARAMETER_NAME)[0].value

                            all_currencies_meli = currencyProxy.get(urlCurrencies)
                            urlCategories = parameterRepository.queryByCode(
                                constans.MELI_API_CATEGORY_ENDPOINT_PARAMETER_NAME)[0].value
                            urlSellers = parameterRepository.queryByCode(
                                constans.MELI_API_SELLER_ENDPOINT_PARAMETER_NAME)[0].value
                            
                            """Con el objetivo de reealizar el proceso de consulta y almacenamiento de los registro los mas rapido posibles se crear espacio de memoria compartida"""
                            """"Estos espacios de memoria son comportidos y se crean con la finaliza de almacenar consulta de entidades previas y evitar y tanto a los servicios de las APIS"""
                            shared_memory = Manager()
                            result_currencies_items_shared_memory = shared_memory.list(all_currencies_meli)
                            result_categories_items_shared_memory = shared_memory.list([])
                            result_seller_items_shared_memory =shared_memory.list([])
                            #position 0 to categories num call services
                            #position 1 to sellers num call services
                            callNumServices = shared_memory.list([0,0])

                            "Se consulta el numero de procesos que dependiendo de donde se ejecuta el proceso se aplica mas o menos dependiente de la configuracion del parametro"
                            numberOfProcess = parameterRepository.queryByCode(
                                constans.MAX_PROCESS_POOL_PARAMETER_NAME)[0].value
                            print(numberOfProcess)
                            poolProcecessing = Pool(int(numberOfProcess))

                            itemToComplementMP =[]

                            for itemToComplete in itemsToComplement:
                                itemToComplementMP.append((itemToComplete,result_currencies_items_shared_memory,result_categories_items_shared_memory,result_seller_items_shared_memory,urlCategories,callNumServices,urlSellers))
                            
                            """Se toma timestamp de inicio y fin del proceso de lanzamiento y finalizacion de los procesos por cada item"""
                            inicio = datetime.today()
                            itemProcessedList = list(poolProcecessing.starmap(self.complementDataItem, itemToComplementMP))
                            fin = datetime.today()


                            """TODO: IMPLEMENTAR UNA INSTANCIA DEL LOGGER PARA PODER MOSTRAR EL RESULTADO DE LA EJECUCION"""
                            print("************************()")

                            for item in itemProcessedList:
                                print("OBJ COMPLETO: ", item.getItemKey(), "-", item.itemId,"-", item.itemSite+ "-", item.itemPrice, "-",
                                    item.itemStartTime, "-", item.categoryID, "-", item.categoryName, "-", item.currencyID, "-", item.currencyDescription, "-", item.sellerID, "-", item.sellerNickName)

                            print("************************()")
                            print("INICIA EN: ", inicio)
                            print("FINALIZA EN: ", fin)
                            print("Llamados categorias ",callNumServices[0])
                            print("Llamados seller ",callNumServices[1])
                            return "Finalizado"
                        else:
                            return "no fue posible su lectura, revise la configuración"
        return "Formato no permitido"


    """Descripción de la función
        Esta funcion es la encargada de que por cada registro o entidade ItemResumen que debe ser complementada en su informacion, 
        interactura con los proxies para traer la informacion y los repositorio para almacenarla
        Parameters
        ----------
        parametro_1 : itemToComplete
           Contiene la informacion que sera leiada en el formato de archivo que ha sido recivida por el controlador del servicio
        parametro_2 : result_currencies_items_shared_memory
            Contiene las monedas que cada proceso va consultado y lo deja en la memoria compartida para evitar ir al servicio proxy de nuevo
        parametro_3 : result_categories_items_shared_memory
            Contiene las categorias que cada proceso va consultado y lo deja en la memoria compartida para evitar ir al servicio proxy de nuevo
        parametro_4 : result_seller_items_shared_memory
            Contiene los seller o usuarios que cada proceso va consultado y lo deja en la memoria compartida para evitar ir al servicio proxy de nuevo
        parametro_5 : categoryBaseURL
            Contiene el parametro general para el proxy de catagories
        parametro_6 : callNumServices
            Permite llevar una metrica de cuentos llamada se realizan en realidad a las apis de categorias y sellers
        parametro_7 : sellerBaseURL
            Contiene el parametro general para el proxy de sellers
        
        Returns
        -------
        item
            Devuelte la informacion del item con toda la informacion recopilada
            TODO:realizar un manejo adecuado de las respuesta de los metodos para poder espeficiar codigos de error de negocio
    """
    def complementDataItem(self, itemToComplete,result_currencies_items_shared_memory,result_categories_items_shared_memory,result_seller_items_shared_memory,categoryBaseURL,callNumServices,sellerBaseURL):
        item = itemProxy.get(itemToComplete)
        
        #Buscando las currencies que estan ya generalizadas en la memoria
        if result_currencies_items_shared_memory:
            currentcyFiltered = list(filter(lambda currency: currency.id==item.currencyID, result_currencies_items_shared_memory))
            if(len(currentcyFiltered)>0):
                item.currencyDescription = currentcyFiltered[0].description
        
        #Buscando si tenemos categorias por pais ya almanecadas en la sharedmemory
        siteFiltered = list(filter(lambda site: site.id==item.itemSite, result_categories_items_shared_memory))
        if(len(siteFiltered)>0):
            categoryFiltered = list(filter(lambda category: category.id==item.categoryID, siteFiltered[0].categories))
            if(len(categoryFiltered)>0):
                item.categoryName = categoryFiltered[0].name
            else:
                item.categoryName = None
        else:
            categoryURL = categoryBaseURL.replace(constans.MELI_API_CATEGORY_ENDPOINT_PARAMETER_PATH_REPLACE, item.itemSite)
            siteCategories = categoryProxy.get(categoryURL)
            callNumServices[0]=callNumServices[0] +1;
            site = Site(item.itemSite,siteCategories)

            for categorySite  in result_categories_items_shared_memory:
                if categorySite.id==item.itemSite:
                    print("Eliminando Categoria",categorySite.id)
                    result_categories_items_shared_memory.remove(categorySite)

            result_categories_items_shared_memory.append(site)
            categoryFiltered = list(filter(lambda category: category.id==item.categoryID, site.categories))
            if(len(categoryFiltered)>0):
                item.categoryName = categoryFiltered[0].name

        #Buscando si tenemos sellers ya almanecadas en la sharedmemory
        sellerFiltered = list(filter(lambda seller: seller.id==item.sellerID, result_seller_items_shared_memory))
        if(len(sellerFiltered)>0):
                item.sellerNickName = sellerFiltered[0].name
        else:
            sellerURL = sellerBaseURL+ str(item.sellerID)
            newSeller = sellerProxy.get(sellerURL)
            if(newSeller):
                item.sellerNickName = newSeller.name
                result_seller_items_shared_memory.append(newSeller)
            
            callNumServices[1]=callNumServices[1] +1;
            for seller  in result_seller_items_shared_memory:
                if seller.id==item.sellerID:
                    result_seller_items_shared_memory.remove(seller)
            
        itemResumenRepository.save(item)
        return item
