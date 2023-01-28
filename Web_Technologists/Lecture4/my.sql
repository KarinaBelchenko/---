-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  age TEXT NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE (name, age, address) VALUES ('Clark', '48', 'Moscow');
INSERT INTO EMPLOYEE (name, age, address) VALUES ('Dave', '21', 'Ufa');
INSERT INTO EMPLOYEE (name, age, address) VALUES ('Ava', '18', 'Moscow');
INSERT INTO EMPLOYEE (name, age, address) VALUES ('Svetlana', '42', 'Rostov-on-Don');
INSERT INTO EMPLOYEE (name, age, address) VALUES ('Mark','20', 'Moscow');

-- fetch 

SELECT * FROM EMPLOYEE WHERE  address = 'Moscow' AND age > 18 AND age < 30;
