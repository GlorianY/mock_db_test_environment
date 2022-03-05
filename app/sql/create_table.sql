-- Create table
-- This table will be created under postgres-data directory, and newer table versions won't overwrite older ones, unless the whole postgres-data (volume) is removed
CREATE TABLE IF NOT EXISTS product (
  product_id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL,
  brand varchar(250) NOT NULL,
  description varchar(250),
  price INT
);
