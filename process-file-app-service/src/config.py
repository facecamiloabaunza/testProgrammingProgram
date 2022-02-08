"""Se inicializa cada una de las configuraciones posibles segun los ambientes requeridos, para este caso solo esta el ambiente de desarrollo"""
class DevelomentConfig():
    DEBUG = True
    SERVER_NAME="localhost:4000"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://userprocessfiledb:mysqlmelitest@localhost:12306/DB_PROCESS_ITEMS"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROCESSED_FILE_NAME_PREFIX ="PROCESS_FILE_LOAD"
    PROCESSED_FILE_NAME_PATH ="PROCESS_FILE_LOAD"
    
config = {
    'development': DevelomentConfig
}