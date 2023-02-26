CREATE TABLE `Users`
(
    `User_id`              INT          NOT NULL AUTO_INCREMENT,
    `Program_id`           INT,
    `Diet_id`              INT,
    `User_name`            VARCHAR(255) NOT NULL,
    `User_surname`         VARCHAR(255) NOT NULL,
    Password_hash          VARCHAR(255) NOT NULL,
    `Email`                VARCHAR(255) NOT NULL UNIQUE CHECK (EmaiL RLIKE '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$'),
    `Age`                  INT,
    `Gender`               VARCHAR(1),
    Height                 INT CHECK (Height >= 100 AND Height <= 250),
    `Weight`               INT CHECK ( Weight >= 30 AND Weight <= 160),
    `Physical_activity_id` INT,
    `Metabolism`           INT CHECK (Metabolism >= 500 AND Metabolism <= 9000),
    PRIMARY KEY (`User_id`)

);
CREATE TABLE `Diets`
(
    `Diet_id`            INT         NOT NULL AUTO_INCREMENT,
    `Diet_name`          VARCHAR(50) NOT NULL,
    `Diet_calories`      INT         NOT NULL,
    `Diet_proteins`      INT         NOT NULL,
    `Diet_fats`          INT         NOT NULL,
    `Diet_carbohydrates` INT         NOT NULL,
    PRIMARY KEY (`Diet_id`)
);
CREATE TABLE `Programs`
(
    `Program_id`   INT          NOT NULL AUTO_INCREMENT,
    `Program_name` VARCHAR(255) NOT NULL UNIQUE,
    `Method_id`    INT,
    `Place_id`     INT,
    `Day_id`       INT,
    PRIMARY KEY (`Program_id`)
);


CREATE TABLE `Physical_activities`
(
    `Physical_activity_id`   INT          NOT NULL AUTO_INCREMENT,
    `Physical_activity_name` VARCHAR(255) NOT NULL UNIQUE,
    `Coefficient`            FLOAT        NOT NULL CHECK ( Coefficient > 0 AND Coefficient < 10),
    PRIMARY KEY (`Physical_activity_id`)
);

CREATE TABLE `Days`
(
    `Day_id`    INT          NOT NULL AUTO_INCREMENT,
    `Day_count` VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (`Day_id`)
);

CREATE TABLE `Places`
(
    `Place_id`   INT          NOT NULL AUTO_INCREMENT,
    `Place_name` VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (`Place_id`)
);

CREATE TABLE `Methods`
(
    `Method_id`   INT          NOT NULL AUTO_INCREMENT,
    `Method_name` VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (`Method_id`)
);

CREATE TABLE `Exercises`
(
    `Exercise_id`           INT          NOT NULL AUTO_INCREMENT,
    `Exercise_name`         VARCHAR(255) NOT NULL UNIQUE,
    `Number_of_approaches`  INT          NOT NULL CHECK ( Number_of_approaches > 0 AND Number_of_approaches < 7),
    `Number_of_repetitions` INT          NOT NULL CHECK ( Number_of_repetitions > 0 AND Number_of_repetitions < 25),
    PRIMARY KEY (`Exercise_id`)
);

CREATE TABLE `Products`
(
    `Product_id`            INT          NOT NULL AUTO_INCREMENT,
    `Product_name`          VARCHAR(255) NOT NULL UNIQUE,
    `Product_calories`      INT          NOT NULL CHECK ( Product_calories >= 0 AND Product_calories < 901),
    `Product_proteins`      INT          NOT NULL CHECK ( Product_proteins >= 0 AND Product_proteins < 101),
    `Product_fats`          INT          NOT NULL CHECK ( Product_fats >= 0 AND Product_fats < 101),
    `Product_carbohydrates` INT          NOT NULL CHECK ( Product_carbohydrates >= 0 AND Product_carbohydrates < 101),
    PRIMARY KEY (`Product_id`)
);

CREATE TABLE `Products_Diets`
(
    `Product_id` INT,
    `Diet_id`    INT,
    PRIMARY KEY (`Product_id`, `Diet_id`)
);

CREATE TABLE `Exercises_Programs`
(
    `Exercise_id` INT,
    `Program_id`  INT,
    PRIMARY KEY (`Exercise_id`, `Program_id`)
);

CREATE TRIGGER add_sum_calories_proteins
    AFTER INSERT
    ON Products_Diets
    FOR EACH ROW
BEGIN
    UPDATE Diets
    SET Diet_calories      = Diet_calories + (SELECT Product_calories FROM Products WHERE NEW.Product_id = Product_id),
        Diet_proteins      = Diet_proteins + (SELECT Product_proteins FROM Products WHERE NEW.Product_id = Product_id),
        Diet_fats          = Diet_fats + (SELECT Product_fats FROM Products WHERE NEW.Product_id = Product_id),
        Diet_carbohydrates = Diet_carbohydrates +
                             (SELECT Product_carbohydrates FROM Products WHERE NEW.Product_id = Product_id)
    WHERE Diet_id = NEW.Diet_id;
END;
ALTER TABLE `Users`
    ADD CONSTRAINT `Users_fk0` FOREIGN KEY (`Program_id`) REFERENCES `Programs` (`Program_id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `Users`
    ADD CONSTRAINT `Users_fk1` FOREIGN KEY (`Diet_id`) REFERENCES `Diets` (`Diet_id`) ON UPDATE CASCADE ON DELETE SET NULL;

ALTER TABLE `Users`
    ADD CONSTRAINT `Users_fk2` FOREIGN KEY (`Physical_activity_id`) REFERENCES `Physical_activities` (`Physical_activity_id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `Programs`
    ADD CONSTRAINT `Programs_fk0` FOREIGN KEY (`Method_id`) REFERENCES `Methods` (`Method_id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `Programs`
    ADD CONSTRAINT `Programs_fk1` FOREIGN KEY (`Place_id`) REFERENCES `Places` (`Place_id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `Programs`
    ADD CONSTRAINT `Programs_fk2` FOREIGN KEY (`Day_id`) REFERENCES `Days` (`Day_id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE Products_Diets
    ADD CONSTRAINT `Products-Diets_fk0` FOREIGN KEY (`Product_id`) REFERENCES `Products` (`Product_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Products_Diets
    ADD CONSTRAINT `Products-Diets_fk1` FOREIGN KEY (`Diet_id`) REFERENCES `Diets` (`Diet_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Exercises_Programs
    ADD CONSTRAINT `Exercises-Programs_fk0` FOREIGN KEY (`Exercise_id`) REFERENCES `Exercises` (`Exercise_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Exercises_Programs
    ADD CONSTRAINT `Exercises-Programs_fk1` FOREIGN KEY (`Program_id`) REFERENCES `Programs` (`Program_id`) ON DELETE CASCADE ON UPDATE CASCADE;












