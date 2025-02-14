"use client"

import React, { useState } from "react";

const IngredientFields: React.FC = () => {
  const [ingredients, setIngredients] = useState<string[]>([""]); // Initialize with one empty ingredient

  // Function to add a new input field
  const addIngredient = () => {
    setIngredients([...ingredients, ""]); // Add a new empty ingredient
  };

  // Function to handle input changes
  const handleIngredientChange = (index: number, value: string) => {
    const updatedIngredients = [...ingredients];
    updatedIngredients[index] = value; // Update the specific ingredient
    setIngredients(updatedIngredients);
  };

  return (
    <div className="flex flex-col items-center space-y-4">
      <h1 className="text-xl font-bold">Add Ingredients</h1>
      {ingredients.map((ingredient, index) => (
        <div key={index} className="flex items-center space-x-4">
          <input
            type="text"
            className="border border-black px-6 py-2"
            placeholder={`Ingredient ${index + 1}`}
            value={ingredient}
            onChange={(e) => handleIngredientChange(index, e.target.value)}
          />
        </div>
      ))}
      <button
        className="bg-violet-500 hover:bg-violet-600 focus:outline-2 focus:outline-offset-2 focus:outline-violet-500 active:bg-violet-700 rounded-full px-6 py-2 shadow-lg text-white"
      >
        Save Ingredient(s)
      </button>
      <button
        onClick={addIngredient}
        className="bg-violet-500 hover:bg-violet-600 focus:outline-2 focus:outline-offset-2 focus:outline-violet-500 active:bg-violet-700 rounded-full px-6 py-2 shadow-lg text-white"
      >
        Add Ingredient
      </button>
    </div>
  );
};

export default IngredientFields;
