-- MySQL Script generated by MySQL Workbench
-- 03/25/15 16:15:43
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema dcs
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dcs
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dcs` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `dcs` ;

-- -----------------------------------------------------
-- Table `dcs`.`auth_user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`auth_user` ;

CREATE TABLE IF NOT EXISTS `dcs`.`auth_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `password` CHAR(128) NOT NULL,
  `email` VARCHAR(128) NOT NULL,
  `is_admin` TINYINT(1) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `modified_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`cart`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`cart` ;

CREATE TABLE IF NOT EXISTS `dcs`.`cart` (
  `id` INT NOT NULL,
  `created_at` VARCHAR(45) NULL,
  `modified_at` VARCHAR(45) NULL,
  `buyer_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cart_user_idx` (`buyer_id` ASC),
  CONSTRAINT `fk_cart_user`
    FOREIGN KEY (`buyer_id`)
    REFERENCES `dcs`.`auth_user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`transaction`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`transaction` ;

CREATE TABLE IF NOT EXISTS `dcs`.`transaction` (
  `id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  `cart_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_transaction_cart1_idx` (`cart_id` ASC),
  CONSTRAINT `fk_transaction_cart1`
    FOREIGN KEY (`cart_id`)
    REFERENCES `dcs`.`cart` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`organisation`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`organisation` ;

CREATE TABLE IF NOT EXISTS `dcs`.`organisation` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`multimedia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`multimedia` ;

CREATE TABLE IF NOT EXISTS `dcs`.`multimedia` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `description` TEXT NULL,
  `price` DECIMAL NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  `image` VARCHAR(120) NULL,
  `organisation_id` INT NOT NULL,
  PRIMARY KEY (`id`))
  CONSTRAINT `fk_multimedia`
    FOREIGN KEY(`organisation_id`)
    REFERENCES `dcs`.`organisation` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`multimedia_content`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`multimedia_content` ;

CREATE TABLE IF NOT EXISTS `dcs`.`multimedia_content` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `multimedia_id` INT NOT NULL,
  `caption` VARCHAR(128) NULL,
  `url` VARCHAR(200) NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_multimedia_content_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_multimedia_content_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcs`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`cart_item`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`cart_item` ;

CREATE TABLE IF NOT EXISTS `dcs`.`cart_item` (
  `id` INT NOT NULL,
  `object_id` VARCHAR(45) NULL,
  `object_type` VARCHAR(45) NULL,
  `cart_id` INT NOT NULL,
  `quantity` INT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  INDEX `fk_cart_item_cart1_idx` (`cart_id` ASC),
  CONSTRAINT `fk_cart_item_cart1`
    FOREIGN KEY (`cart_id`)
    REFERENCES `dcs`.`cart` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`music`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`music` ;

CREATE TABLE IF NOT EXISTS `dcs`.`music` (
  `multimedia_id` INT NOT NULL,
  `duration` INT NULL,
  INDEX `fk_music_multimedia1_idx` (`multimedia_id` ASC),
  PRIMARY KEY (`multimedia_id`),
  CONSTRAINT `fk_music_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcs`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`movie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`movie` ;

CREATE TABLE IF NOT EXISTS `dcs`.`movie` (
  `multimedia_id` INT NOT NULL,
  `duration` INT NULL,
  INDEX `fk_movie_multimedia1_idx` (`multimedia_id` ASC),
  PRIMARY KEY (`multimedia_id`),
  CONSTRAINT `fk_movie_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcs`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`application`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`application` ;

CREATE TABLE IF NOT EXISTS `dcs`.`application` (
  `multimedia_id` INT NOT NULL,
  `version` CHAR(10) NULL,
  INDEX `fk_application_multimedia1_idx` (`multimedia_id` ASC),
  PRIMARY KEY (`multimedia_id`),
  CONSTRAINT `fk_application_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcs`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`person` ;

CREATE TABLE IF NOT EXISTS `dcs`.`person` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`role` ;

CREATE TABLE IF NOT EXISTS `dcs`.`role` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`crew`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`crew` ;

CREATE TABLE IF NOT EXISTS `dcs`.`crew` (
  `id` INT NOT NULL,
  `multimedia_id` INT NOT NULL,
  `person_id` INT NOT NULL,
  `role_id` INT NOT NULL,
  `organisation_id` INT NOT NULL,
  INDEX `fk_multimedia_has_person_person1_idx` (`person_id` ASC),
  INDEX `fk_multimedia_has_person_multimedia1_idx` (`multimedia_id` ASC),
  PRIMARY KEY (`id`),
  INDEX `fk_crew_role1_idx` (`role_id` ASC),
  INDEX `fk_crew_organisation1_idx` (`organisation_id` ASC),
  CONSTRAINT `fk_multimedia_has_person_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcs`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_multimedia_has_person_person1`
    FOREIGN KEY (`person_id`)
    REFERENCES `dcs`.`person` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_crew_role1`
    FOREIGN KEY (`role_id`)
    REFERENCES `dcs`.`role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_crew_organisation1`
    FOREIGN KEY (`organisation_id`)
    REFERENCES `dcs`.`organisation` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`category` ;

CREATE TABLE IF NOT EXISTS `dcs`.`category` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `parent_category_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_category_category1_idx` (`parent_category_id` ASC),
  CONSTRAINT `fk_category_category1`
    FOREIGN KEY (`parent_category_id`)
    REFERENCES `dcs`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`multimedia_category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`multimedia_category` ;

CREATE TABLE IF NOT EXISTS `dcs`.`multimedia_category` (
  `id` INT NOT NULL,
  `multimedia_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_multimedia_has_category_category1_idx` (`category_id` ASC),
  INDEX `fk_multimedia_has_category_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_multimedia_has_category_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcs`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_multimedia_has_category_category1`
    FOREIGN KEY (`category_id`)
    REFERENCES `dcs`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`book`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`book` ;

CREATE TABLE IF NOT EXISTS `dcs`.`book` (
  `multimedia_id` INT NOT NULL,
  `isbn13` CHAR(13) NULL,
  `isbn10` CHAR(10) NULL,
  `published_on` DATE NULL,
  INDEX `fk_book_multimedia1_idx` (`multimedia_id` ASC),
  PRIMARY KEY (`multimedia_id`),
  CONSTRAINT `fk_book_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcs`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`multimedia_review`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`multimedia_review` ;

CREATE TABLE IF NOT EXISTS `dcs`.`multimedia_review` (
  `id` INT NOT NULL,
  `comment` TEXT NOT NULL,
  `rating` INT NULL,
  `multimedia_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_review_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_review_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcs`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`album`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`album` ;

CREATE TABLE IF NOT EXISTS `dcs`.`album` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcs`.`album_music`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dcs`.`album_music` ;

CREATE TABLE IF NOT EXISTS `dcs`.`album_music` (
  `id` INT NOT NULL,
  `album_id` INT NOT NULL,
  `music_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_album_has_music_album1_idx` (`album_id` ASC),
  INDEX `fk_album_music_music1_idx` (`music_id` ASC),
  CONSTRAINT `fk_album_has_music_album1`
    FOREIGN KEY (`album_id`)
    REFERENCES `dcs`.`album` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_album_music_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `dcs`.`music` (`multimedia_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
