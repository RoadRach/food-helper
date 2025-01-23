-- Insert into Ingredients
INSERT INTO Ingredients (name, category, expiration_date, quantity)
VALUES
('Carrot', 'Vegetable', '2025-02-01', '2 kg'),
('Milk', 'Dairy', '2025-01-25', '1 liter');

-- Insert into Recipes
INSERT INTO Recipes (name, instructions, ingredients)
VALUES
('Carrot Soup', 'Boil carrots and blend with spices.', '[{"name": "Carrot", "quantity": "500g"}]');
