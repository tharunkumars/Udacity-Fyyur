CREATE TABLE customers (
  customer_id INTEGER,
  first_name VARCHAR(50) , 
  last_name VARCHAR(50) , 
  email VARCHAR(100) , 
  phone_number VARCHAR(20) 
);

Select * from customers;

commit;

-- For Persons table using SQLAlchemy
--insert into persons(id,name) values (2, 'Name2')
Select * from persons