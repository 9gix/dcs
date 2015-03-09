-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema dcb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dcb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dcb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `dcb` ;

-- -----------------------------------------------------
-- Table `dcb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`user` (
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
-- Table `dcb`.`cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`cart` (
  `id` INT NOT NULL,
  `created_at` VARCHAR(45) NULL,
  `modified_at` VARCHAR(45) NULL,
  `buyer_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cart_user_idx` (`buyer_id` ASC),
  CONSTRAINT `fk_cart_user`
    FOREIGN KEY (`buyer_id`)
    REFERENCES `dcb`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`transaction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`transaction` (
  `id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  `cart_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_transaction_cart1_idx` (`cart_id` ASC),
  CONSTRAINT `fk_transaction_cart1`
    FOREIGN KEY (`cart_id`)
    REFERENCES `dcb`.`cart` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`content`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`content` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `caption` VARCHAR(128) NULL,
  `url` VARCHAR(200) NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`cart_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`cart_item` (
  `id` INT NOT NULL,
  `object_id` VARCHAR(45) NULL,
  `object_type` VARCHAR(45) NULL,
  `cart_id` INT NOT NULL,
  `quantity` INT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  INDEX `fk_cart_item_cart1_idx` (`cart_id` ASC),
  CONSTRAINT `fk_cart_item_cart1`
    FOREIGN KEY (`cart_id`)
    REFERENCES `dcb`.`cart` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`multimedia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`multimedia` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`music`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`music` (
  `id` INT NOT NULL,
  `multimedia_id` INT NOT NULL,
  `duration` INT NULL,
  `created_at` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_music_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_music_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcb`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`movie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`movie` (
  `id` INT NOT NULL,
  `duration` VARCHAR(45) NULL,
  `multimedia_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_movie_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_movie_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcb`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`application`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`application` (
  `id` INT NOT NULL,
  `multimedia_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  `version` CHAR(10) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_application_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_application_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcb`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`person` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`role` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`organisation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`organisation` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`crew`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`crew` (
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
    REFERENCES `dcb`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_multimedia_has_person_person1`
    FOREIGN KEY (`person_id`)
    REFERENCES `dcb`.`person` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_crew_role1`
    FOREIGN KEY (`role_id`)
    REFERENCES `dcb`.`role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_crew_organisation1`
    FOREIGN KEY (`organisation_id`)
    REFERENCES `dcb`.`organisation` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`multimedia_content`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`multimedia_content` (
  `id` INT NOT NULL,
  `multimedia_id` INT NOT NULL,
  `content_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_multimedia_has_content_content1_idx` (`content_id` ASC),
  INDEX `fk_multimedia_has_content_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_multimedia_has_content_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcb`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_multimedia_has_content_content1`
    FOREIGN KEY (`content_id`)
    REFERENCES `dcb`.`content` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`category` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `parent_category_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_category_category1_idx` (`parent_category_id` ASC),
  CONSTRAINT `fk_category_category1`
    FOREIGN KEY (`parent_category_id`)
    REFERENCES `dcb`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`multimedia_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`multimedia_category` (
  `id` INT NOT NULL,
  `multimedia_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_multimedia_has_category_category1_idx` (`category_id` ASC),
  INDEX `fk_multimedia_has_category_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_multimedia_has_category_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcb`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_multimedia_has_category_category1`
    FOREIGN KEY (`category_id`)
    REFERENCES `dcb`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`book`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`book` (
  `id` INT NOT NULL,
  `multimedia_id` INT NOT NULL,
  `isbn13` CHAR(13) NULL,
  `isbn10` CHAR(10) NULL,
  `published_on` DATE NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_book_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_book_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcb`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`multimedia_review`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`multimedia_review` (
  `id` INT NOT NULL,
  `comment` TEXT NOT NULL,
  `rating` INT NULL,
  `multimedia_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_review_multimedia1_idx` (`multimedia_id` ASC),
  CONSTRAINT `fk_review_multimedia1`
    FOREIGN KEY (`multimedia_id`)
    REFERENCES `dcb`.`multimedia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`album`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`album` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dcb`.`album_music`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dcb`.`album_music` (
  `id` INT NOT NULL,
  `album_id` INT NOT NULL,
  `music_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_album_has_music_music1_idx` (`music_id` ASC),
  INDEX `fk_album_has_music_album1_idx` (`album_id` ASC),
  CONSTRAINT `fk_album_has_music_album1`
    FOREIGN KEY (`album_id`)
    REFERENCES `dcb`.`album` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_album_has_music_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `dcb`.`music` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
