CREATE TABLE Measurement(
	Id INTEGER PRIMARY KEY,
	Name VARCHAR(50),
	Unitof VARCHAR(10),
);

CREATE TABLE Ingredient(
	Id INTEGER PRIMARY KEY,
	Name VARCHAR(50),
	Price LONG,
	Measurement INTEGER,
	Category VARCHAR(50)
);

INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('fluid oz','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('cups','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('tablespoons','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('teaspoons','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('pounds','weight');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('ounces','weight');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('gram','weight');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('','count');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('bundles','count');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('ears','count');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('cloves','count');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('packages','count');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('galon','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('liter','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('envelope','count');



INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Flour, white, all purpose',0.522,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Rice, white, long grain, uncooked',0.724,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Spaghetti and macaroni',1.286,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Bread, white',11.409,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Bread, whole wheat',2.046,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Cookies, chocolate chip',3.729,5,'Cereals and bakery products');

INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ground chuck, 100% beef',3.479,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ground beef, 100% beef',3.268,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ground beef, lean',4.811,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('All uncooked ground beef',3.823,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Chuck roast, excluding U/P/C',4.125,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ground beef, lean and extra lean',4.811,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Round roast, USDA Choice, boneless',4.633,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Round roast, excluding U/P/C',4.551,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('All Uncooked Beef Roasts',4.689,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Steak, round, USDA Choice, boneless',4.818,5,'Meats, poultry, fish and eggs')
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Steak, round, excluding U/P/C',4.551,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Steak, sirloin, excluding U/P/C',5.527,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Steak, sirloin, USDA Choice, boneless',6.864,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Beef for stew, boneless',4.655,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('All Uncooked Beef Steaks',6.232,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('All Uncooked Other Beef',3.920,5,'Meats, poultry, fish and eggs');

INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Bacon, sliced',4.573,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Chops, center cut',3.655,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Chops, boneless',3.900 ,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('All Pork Chops',3.489,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ham, half, bone-in, smoked',2.085,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ham, boneless, excluding canned',3.800,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('All Ham',2.690,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('All Other Pork',2.496,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('All Other Pork',2.496,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Bologna, all beef or mixed',3.053,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Eggs, grade A, large',1.918,8,'Meats, poultry, fish and eggs');

INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Chicken, fresh, whole',1.473,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Chicken breast, bone-in,',2.996,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Chicken breast, boneless,',4.266,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Chicken legs, bone-in',1.538,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Chicken wings, bone-in',1.138,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('salmon, farmed raised,',3.999,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('tilapia fillets, fresh',2.599,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('shrimp, medium, fresh',7.555,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('crabmeat, medium, fresh',9.555,5,'Meats, poultry, fish and eggs');


INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Butter, salted, grade AA',3.180,5,'Dairy products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('American processed cheese',4.131,5,'Dairy products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Cheddar cheese, natural',5.635,5,'Dairy products');

INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Apples, Red Delicious',1.330,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Bananas',0.597,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Oranges, Navel',0.981,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Oranges, Valencia',0.781,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Cherries',2.992,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Grapefruit',0.953,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Grapes, Thompson Seedless',2.452,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Lemons',1.416,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Peaches',1.566,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Pears, Anjou',1.187,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Strawberries',1.784,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Potatoes',0.619,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Lettuce, iceberg',0.972,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Lettuce, romaine',1.727,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Tomatoes',1.460,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Yellow Onion , medium',1.160,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Red Onion, medium',1.460,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Broccoli florets',1.742,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Cabbage',0.641,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Carrots',0.788,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Celery',0.806,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Green bell pepper',2.191,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Red bell pepper',3.267,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('White Mushroom',2.999,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Brown Mushroom',2.999,5,'Fruits and vegetables');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ginger',4.139,5,'Fruits and vegetables');


INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Beans, dried, any type',1.391,5,'Other foods at home');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Sugar, white',0.656,5,'Other foods at home');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Margarine, stick',1.195,5,'Other foods at home');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Peanut butter, creamy',2.698,5,'Other foods at home');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Coffee, ground roast',5.674,5,'Other foods at home');








