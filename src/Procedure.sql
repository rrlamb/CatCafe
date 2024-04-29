USE CatCafeInfo;

DROP PROCEDURE IF EXISTS Low_Inventory;

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
