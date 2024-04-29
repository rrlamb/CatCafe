CREATE DATABASE CatCafeInfo;
USE CatCafeInfo;
DROP USER 'catcafe'@'localhost';
CREATE USER 'catcafe'@'localhost' IDENTIFIED BY 'CoffeeCatSandwich';

CREATE TABLE Customer(
   email VARCHAR(50) PRIMARY KEY,
   first_name VARCHAR(20) NOT NULL,
   last_name VARCHAR(50) NOT NULL,
   points INT UNSIGNED,
   available_reward VARCHAR(20),
   cat_name VARCHAR(20) NOT NULL
   );

   CREATE TABLE Cat(
   cat_name VARCHAR(20) PRIMARY KEY,
   breed VARCHAR(20),
   sex CHAR(1) CHECK (sex IN('F','M','S','N', 'X')),
   age TINYINT UNSIGNED,
   weight TINYINT UNSIGNED NOT NULL,
   adoption_phone_number  CHAR(10) NOT NULL,
   customer_name VARCHAR(50),
   FOREIGN KEY (customer_name) REFERENCES Customer(email)
      ON UPDATE CASCADE
      ON DELETE CASCADE
   );

CREATE TABLE Menu(
	item VARCHAR(25) PRIMARY KEY,
	add_on VARCHAR(25),
	price FLOAT NOT NULL,
	employee_id SMALLINT UNSIGNED NOT NULL
);

CREATE TABLE Employee(
   id SMALLINT UNSIGNED PRIMARY KEY,
   first_name VARCHAR(20) NOT NULL,
   last_name VARCHAR(50) NOT NULL,
   role VARCHAR(30) NOT NULL,
   email VARCHAR(50) UNIQUE NOT NULL,
   age SMALLINT UNSIGNED,
   phone_number CHAR(10),
   bank_account_number VARCHAR(17) NOT NULL
   );

CREATE TABLE Caretaker(
   cat_name VARCHAR(20),
   employee_id SMALLINT UNSIGNED,
   PRIMARY KEY (cat_name, employee_id),
   FOREIGN KEY (cat_name) REFERENCES Cat(cat_name)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
   FOREIGN KEY (employee_id) REFERENCES Employee(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
   );

CREATE TABLE Inventory(
	inventory_item VARCHAR(25) PRIMARY KEY,
	quantity SMALLINT NOT NULL
);

CREATE TABLE Ingredient(
   menu_item VARCHAR(25),
   inventory_item VARCHAR(25),
   employee_id SMALLINT UNSIGNED,
   PRIMARY KEY (menu_item, inventory_item),
   FOREIGN KEY (menu_item) REFERENCES Menu(item)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
   FOREIGN KEY (inventory_item) REFERENCES Inventory(inventory_item)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
	FOREIGN KEY (employee_id) REFERENCES Employee(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
   );

DROP PROCEDURE IF EXISTS Low_Inventory;
DROP TRIGGER IF EXISTS CustomerReward;

DELIMITER //
CREATE TRIGGER CustomerReward
BEFORE UPDATE
On Customer
FOR EACH ROW
BEGIN
	IF NEW.points >= 1000 THEN
		SET NEW.available_reward = "Turkey Club";
	ELSEIF NEW.points >= 750 THEN
		SET NEW.available_reward = "Chicken Salad";
	ELSEIF NEW.points >= 500 THEN
		SET NEW.available_reward = "Avocado Toast";
	ELSEIF NEW.points >= 250 THEN
		SET NEW.available_reward = "Iced Coffee";
	ELSEIF NEW.points >= 150 THEN
		SET NEW.available_reward = "Hot Coffee";
	ELSE
		SET NEW.available_reward = "Water";
	END IF;
END;
//
DELIMITER ;


DELIMITER //

CREATE PROCEDURE Low_Inventory(IN item_name VARCHAR(25), OUT num_return INT)
BEGIN
    SELECT quantity
    INTO num_return
    FROM Inventory
    WHERE inventory_item = item_name;

    IF num_return <= 5 THEN
		SET num_return = 1;
	ELSE
		SET num_return = 0;
	END IF;
END;//
DELIMITER ;



INSERT IGNORE INTO Customer (email, first_name, last_name, cat_name) VALUES ('john.smith@gmail.com', 'John', 'Smith', 'Garfield');
INSERT IGNORE INTO Customer (email, first_name, last_name, cat_name) VALUES ('jane.ross@gmail.com', 'Jane', 'Ross', 'Blaise');
INSERT IGNORE INTO Customer (email, first_name, last_name, cat_name) VALUES ('adam.lyons@gmail.com', 'Adam', 'Lyons', 'Ember');
INSERT IGNORE INTO Customer (email, first_name, last_name, cat_name) VALUES ('susie.burns@gmail.com', 'Susie', 'Burns', 'Lucy');
INSERT IGNORE INTO Customer (email, first_name, last_name, cat_name) VALUES ('michael.green@gmail.com', 'Michael', 'Green', 'Smokey');

 INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES ('Bread', 50);
 INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES ('Turkey', 50);
 INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES ('Lettuce', 50);
 INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES ('Tomato', 50);
 INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES ('Cheese', 50);
 INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES ('Avocado', 50);
 INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES ('Chicken', 50);
 INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES ('Water', 50);
 INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES ('Coffee', 50);

 INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES ('Turkey Club', 'NULL', 12.25, 0);
 INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES ('Avocado Toast', 'NULL', 8.50, 0);
 INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES ('Chicken Salad', 'NULL', 10.75, 0);
 INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES ('Water Cup', 'NULL', 0, 0);
 INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES ('Iced Coffee', 'NULL', 4.50, 0);
 INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES ('Hot Coffee', 'NULL', 3.50, 0);

INSERT IGNORE INTO Cat (cat_name, breed, sex, age, weight, adoption_phone_number) VALUES ('Garfield', 'American Shorthair', 'M', 4, 9, '3045551234');
INSERT IGNORE INTO Cat (cat_name, breed, sex, age, weight, adoption_phone_number) VALUES ('Blaise', 'Persian', 'M', 2, 8, '3045551234');
INSERT IGNORE INTO Cat (cat_name, breed, sex, age, weight, adoption_phone_number) VALUES ('Lucy', 'British Shorthair', 'F', 4, 7, '3045554567');
INSERT IGNORE INTO Cat (cat_name, breed, sex, age, weight, adoption_phone_number) VALUES ('Ember', 'Devon Rex', 'M', 1, 6, '3045554567');
INSERT IGNORE INTO Cat (cat_name, breed, sex, age, weight, adoption_phone_number) VALUES ('Smokey', 'Russian Blue', 'F', 6, 11, '3045557890');

INSERT IGNORE INTO Employee (id, first_name, last_name, role, email, age, phone_number, bank_account_number) VALUES ('1', 'Amanda', 'Morris', 'Caretaker', 'amandamorris@gmail.com', 55, 3045556789, '11111111111111111');
INSERT IGNORE INTO Employee (id, first_name, last_name, role, email, age, phone_number, bank_account_number) VALUES ('2', 'Tim', 'Snyder', 'Caretaker', 'timsynder@gmail.com', 30, 304551111, '22222222222222222');
INSERT IGNORE INTO Employee (id, first_name, last_name, role, email, age, phone_number, bank_account_number) VALUES ('3', 'Trinity', 'Maynard', 'Manager', 'trinitymaynard@gmail.com', 45, 3045552222, '33333333333333333');
INSERT IGNORE INTO Employee (id, first_name, last_name, role, email, age, phone_number, bank_account_number) VALUES ('4', 'Miles', 'Atlas', 'Cashier', 'milesatlas@gmail.com', 20, 3045553333, '44444444444444444');
INSERT IGNORE INTO Employee (id, first_name, last_name, role, email, age, phone_number, bank_account_number) VALUES ('5', 'Sarah', 'Clemens', 'Cashier', 'sarahclemens@gmail.com', 26, 3045554444, '55555555555555555');


INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Turkey Club', 'Bread', '1');
INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Turkey Club', 'Turkey', '1');
INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Turkey Club', 'Lettuce', '1');
INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Turkey Club', 'Tomato', '1');
INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Turkey Club', 'Cheese', '1');

INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Avocado Toast', 'Bread', '1');
INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Avocado Toast', 'Avocado', '1');

INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Chicken Salad', 'Chicken', '1');
INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Chicken Salad', 'Lettuce', '1');

INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Water Cup', 'Water', '1');

INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Iced Coffee', 'Coffee', '1');

INSERT IGNORE INTO Ingredient (menu_item, inventory_item, employee_id) VALUES ('Hot Coffee', 'Coffee', '1');

INSERT IGNORE INTO Caretaker (cat_name, employee_id) VALUES ('Garfield', '1');
INSERT IGNORE INTO Caretaker (cat_name, employee_id) VALUES ('Blaise', '1');
INSERT IGNORE INTO Caretaker (cat_name, employee_id) VALUES ('Lucy', '2');
INSERT IGNORE INTO Caretaker (cat_name, employee_id) VALUES ('Ember', '2');
INSERT IGNORE INTO Caretaker (cat_name, employee_id) VALUES ('Smokey', '2');