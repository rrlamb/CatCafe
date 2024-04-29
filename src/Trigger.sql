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
