-- Create table
CREATE TABLE IF NOT EXISTS product (
  product_id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL,
  description varchar(250),
  price INT
);