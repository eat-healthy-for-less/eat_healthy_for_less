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

INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('floz','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('cup','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('Tbs','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('tsb','volume');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('lb','weight');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('OZ','weight');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('gram','weight');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('count','count');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('bundle','count');
INSERT INTO Measurement(VARCHAR,UnitOf)VALUES ('ear','count');



INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Flour, white, all purpose',0.522,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Rice, white, long grain, uncooked',0.724,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Spaghetti and macaroni',1.286,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Bread, white',11.409,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Bread, whole wheat',2.046,5,'Cereals and bakery products');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Cookies, chocolate chip',3.729,5,'Cereals and bakery products');

INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ground chuck, 100% beef',3.479,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ground beef, 100% beef',3.268,5,'Meats, poultry, fish and eggs');
INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Ground beef, lean and extra lean',4.811,5,'Meats, poultry, fish and eggs');
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

INSERT INTO Ingredient(name,Price,Measurement)VALUES ('Chicken, fresh, whole',3.053,5,'Meats, poultry, fish and eggs');












INSERT INTO inventory(StockNumber,Descrip,OnHandQuan,PackQty,PackCost)VALUES (43512,'10W-30 Motor Oil, Quart',36,12,18.20);
INSERT INTO inventory(StockNumber,Descrip,OnHandQuan,PackQty,PackCost)VALUES (51013,'D Dry Cells 8 Pack',19,12,90.20);
INSERT INTO inventory(StockNumber,Descrip,OnHandQuan,PackQty,PackCost)VALUES (23155,'Shovel Pointed Long Handle',1500,1,9.82);
INSERT INTO inventory(StockNumber,Descrip,OnHandQuan,PackQty,PackCost)VALUES (51001,'AAA Dry Cells 4 Pack ',92,12,9.00);
INSERT INTO inventory(StockNumber,Descrip,OnHandQuan,PackQty,PackCost)VALUES (43111,'White Gas Gallon Can',14,4,14.75); 