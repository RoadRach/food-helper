import Link from "next/link";
import IngredientFields from "../components/ingredientFields"

export default function Home() {
  return (
    <div className="bg-white min-h-screen">
      <div>
        <h1>Home</h1>
        <Link href="/recipe">Go to Recipe Page</Link>
        <h1>Enter Recipes here:</h1>
        <div className="flex items-center justify-center  space-x-8">
        <IngredientFields></IngredientFields>
        </div>
      </div>
    </div>
  );
}


