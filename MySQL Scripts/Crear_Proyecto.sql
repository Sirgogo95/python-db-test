CREATE TABLE `mydatabase`.`new_table` (
  `Nombre` VARCHAR(64) NOT NULL,
  `Itbis` FLOAT ZEROFILL NOT NULL,
  `Manejo` FLOAT ZEROFILL NOT NULL,
  `Auxiliares` FLOAT ZEROFILL NOT NULL,
  `Desperdicio` FLOAT ZEROFILL NOT NULL,
  `Listado_Precios` VARCHAR(255) NULL,
  `Presupuestos` VARCHAR(255) NULL,
  `Indirectos` VARCHAR(255) NULL,
  `Fecha` DATE NULL,
  `Distinct` INT(1) NULL,
  PRIMARY KEY (`Nombre`));

