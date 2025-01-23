-- Create Ingredients Table
CREATE TABLE Ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    expiration_date DATE,
    quantity VARCHAR(50)
);

-- Create Recipes Table
CREATE TABLE Recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    instructions TEXT,
    ingredients JSON
);
