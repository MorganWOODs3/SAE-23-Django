-- MySQL Script generated by MySQL Workbench
-- Mon Jun 13 20:58:23 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sae23mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sae23mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sae23mydb` DEFAULT CHARACTER SET utf8 ;
USE `sae23mydb` ;

-- -----------------------------------------------------
-- Table `sae23mydb`.`Groupes-etudiant`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae23mydb`.`Groupes-etudiant` (
  `idGroupes-etudiant` INT NOT NULL AUTO_INCREMENT,
  `Nom` VARCHAR(45) NULL,
  PRIMARY KEY (`idGroupes-etudiant`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sae23mydb`.`Etudiants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae23mydb`.`Etudiants` (
  `idEtudiants` INT NOT NULL AUTO_INCREMENT,
  `Nom` VARCHAR(45) NULL,
  `Prenom` VARCHAR(45) NULL,
  `Email` VARCHAR(144) NULL,
  `Photo` LONGTEXT NULL,
  `groupes` INT NOT NULL,
  PRIMARY KEY (`idEtudiants`, `groupes`),
  INDEX `group_idx` (`groupes` ASC),
  CONSTRAINT `group`
    FOREIGN KEY (`groupes`)
    REFERENCES `sae23mydb`.`Groupes-etudiant` (`idGroupes-etudiant`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sae23mydb`.`Enseignants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae23mydb`.`Enseignants` (
  `idEnseignants` INT NOT NULL AUTO_INCREMENT,
  `Nom` VARCHAR(45) NULL,
  PRIMARY KEY (`idEnseignants`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sae23mydb`.`Cours`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae23mydb`.`Cours` (
  `idCours` INT NOT NULL AUTO_INCREMENT,
  `titre cours` VARCHAR(100) NULL,
  `Date` DATETIME NULL,
  `enseignant` INT NOT NULL,
  `Durée` TIME NULL,
  `Groupe` INT NOT NULL,
  PRIMARY KEY (`idCours`, `Groupe`, `enseignant`),
  INDEX `enseignant2_idx` (`enseignant` ASC) VISIBLE,
  INDEX `group2_idx` (`Groupe` ASC) VISIBLE,
  CONSTRAINT `enseignant`
    FOREIGN KEY (`enseignant`)
    REFERENCES `sae23mydb`.`Enseignants` (`idEnseignants`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `groupe`
    FOREIGN KEY (`Groupe`)
    REFERENCES `sae23mydb`.`Groupes-etudiant` (`idGroupes-etudiant`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sae23mydb`.`absences`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae23mydb`.`absences` (
  `idabsences` INT NOT NULL,
  `Etudiant` INT NOT NULL,
  `Cours` INT NOT NULL,
  `justification` LONGTEXT NULL,
  `justifie` SET('oui', 'non') NULL,
  PRIMARY KEY (`idabsences`, `Etudiant`, `Cours`),
  INDEX `etudiant_idx` (`Etudiant` ASC) VISIBLE,
  INDEX `cours_idx` (`Cours` ASC) VISIBLE,
  CONSTRAINT `etudiant`
    FOREIGN KEY (`Etudiant`)
    REFERENCES `sae23mydb`.`Etudiants` (`idEtudiants`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `cours`
    FOREIGN KEY (`Cours`)
    REFERENCES `sae23mydb`.`Cours` (`idCours`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
