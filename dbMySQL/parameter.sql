/*
-- Query: SELECT * FROM DB_PROCESS_ITEMS.parameters
LIMIT 0, 1000

-- Date: 2022-02-06 22:27
*/
INSERT INTO `` (`code`,`value`,`description`) VALUES ('FORMAT_ITEM_FILE','text/csv','CONTENT TYPE FOR CSV FILES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('FORMAT_ITEM_FILE','text/plain','CONTENT TYPE FOR PLAIN TEXT FILES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('FORMAT_ITEM_FILE','application/json','CONTENT TYPE FOR JSONLINE FILES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('DELIMITER_TEXT/CSV',',','SEPARATOR FOR CSV FILES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('DELIMITER_TEXT/PLAIN',',','SEPARATOR FOR TEXT FILES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('ENCODING_TEXT/CSV','utf-8','ENCODING FOR CSV FILES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('MAX_PROCESS_POOL','20','NUMBER OF PROCESSES CREATED TO ITEMPS QUERIES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('MELI_API_CURRENCY_ENDPOINT','https://api.mercadolibre.com/currencies/','ENDPOINT TO ALL CURRENCIES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('MELI_API_ITEM_ENDPOINT','https://api.mercadolibre.com/items/','ENDPOINT TO SPECIFIC ITEM');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('MELI_API_CATEGORY_ENDPOINT','https://api.mercadolibre.com/sites/[site]/categories','ENDPOINT TO SPECIFIC SITE CATEGORIES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('MELI_API_USER_ENDPOINT','https://api.mercadolibre.com/users/','ENDPOINT TO SPECIFIC SELLER');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('ENCODING_TEXT/PLAIN','utf-8','ENCODING FOR TXT FILES');
INSERT INTO `` (`code`,`value`,`description`) VALUES ('ENCODING_APPLICATION/JSON','utf-8','ENCODING FOR JSON FILES');
