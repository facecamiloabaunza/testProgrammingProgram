/*
-- Query: SELECT * FROM DB_PROCESS_ITEMS.parameters
LIMIT 0, 1000

-- Date: 2022-02-06 22:27
*/
CREATE TABLE `parameters` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `value` varchar(200) NOT NULL,
  `description` varchar(400) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1


CREATE TABLE `itemsProcessFile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idItem` varchar(100) NOT NULL,
  `site` varchar(100) NOT NULL,
  `price` float DEFAULT NULL,
  `startTime` datetime DEFAULT NULL,
  `categoryName` varchar(200) DEFAULT NULL,
  `currencyDescription` varchar(200) DEFAULT NULL,
  `sellerName` varchar(350) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3243 DEFAULT CHARSET=latin1