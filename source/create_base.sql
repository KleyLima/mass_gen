CREATE SCHEMA IF NOT EXISTS `db_mass` DEFAULT CHARACTER SET utf8 ;
USE `db_sagitario` ;

CREATE TABLE IF NOT EXISTS `db_mass`.`people` (
  `id_people` INTEGER NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `dt_nasc` DATETIME NOT NULL,
  `cpf` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_people`) );
