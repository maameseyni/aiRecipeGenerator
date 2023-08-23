from flask import Flask, render_template,request,redirect
import random

app = Flask(__name__)

ingredients_list = [ 

    {"name": "vegetables", "image": "static/images/vegetables.jpg"},
    {"name": "soy sauce", "image": "static/images/soy sauce.jpg"},
    {"name": "pepper", "image": "static/images/pepper.jpg"},
    {"name": "garlic", "image": "static/images/garlic.jpg"},
    
    {"name": "chicken", "image": "static/images/chicken.jpg"},
    {"name": "onion", "image": "static/images/onion.jpg"},
    {"name": "garlic", "image": "static/images/garlic.jpg"},
    {"name": "ginger", "image": "static/images/ginger.jpg"},
    {"name": "cumin", "image": "static/images/cumin.jpg"},
    {"name": "coriander", "image": "static/images/coriander.jpg"},

    {"name": "vegetables", "image": "static/images/vegetables.jpg"},
    {"name": "soy sauce", "image": "static/images/soy sauce.jpg"},
    {"name": "pepper", "image": "static/images/pepper.jpg"},
    {"name": "garlic", "image": "static/images/garlic.jpg"},
]

# Vous pouvez continuer à ajouter des ingrédients à cette liste si nécessaire.

recipes = [
    {
        "name": "Beef Stir Fry",
        "ingredients": ["beef", "vegetables", "soy sauce", "pepper", "garlic"],
        "steps": [
            "Heat oil in a wok or large skillet over medium-high heat.",
            "Add beef and stir-fry for 5 minutes, or until browned.",
            "Add vegetables and stir-fry for another 5 minutes.",
            "Add soy sauce and stir-fry for another 2 minutes.",
            "Season with pepper and garlic, and stir-fry for an additional 2 minutes.",
            "Serve hot with rice or noodles."
        ]
    },
    {
        "name": "Chicken Curry",
        "ingredients": ["chicken", "onion", "garlic", "ginger", "curry powder", "cumin", "coriander"],
        "steps": [
            "Heat oil in a wok or large skillet over medium-high heat.",
            "Add chicken and stir-fry for 5 minutes, or until browned.",
            "Add onion and garlic, and stir-fry for another 2 minutes.",
            "Add ginger and curry powder, and stir-fry for another 2 minutes.",
            "Add cumin and coriander, and stir-fry for another 2 minutes.",
            "Season with salt and pepper, and stir-fry for an additional 2 minutes.",
            "Serve hot with rice or noodles."
        ]
    },
    {
        "name": "Vegetable Stir Fry",
        "ingredients": ["vegetables", "soy sauce", "pepper", "garlic"],
        "steps": [
            "Heat oil in a wok or large skillet over medium-high heat.",
            "Add vegetables and stir-fry for 5 minutes, or until tender.",
            "Add soy sauce and stir-fry for another 2 minutes.",
            "Season with pepper and garlic, and stir-fry for an additional 2 minutes.",
            "Serve hot with rice or noodles."
        ]
    },
    # Ajoutez plus de recettes ici
]

@app.route('/')
def index():
    return render_template('index.html', ingredients=ingredients_list, recipes=recipes)

@app.route('/generate_recipe')
def generate_recipe():
    random_recipe = random.choice(recipes)
    random_ingredients = random.sample(ingredients_list, 4)
    # return render_template('recipe.html', recipe=random_recipe, ingredient=random_recipe["ingredients"])
    return render_template('recipe.html', recipe=random_recipe, ingredients=random_ingredients)


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',ingredients=ingredients_list, recipes=recipes)


@app.route('/recipe_added', methods=['POST'])
def recipe_added():
    recipe_name = request.form['recipe_name']
    recipe_ingredients = request.form.getlist('recipe_ingredients')
    recipe_steps = request.form.getlist('recipe_steps')
    new_recipe = {
        "name": recipe_name,
        "ingredients": recipe_ingredients,
        "steps": recipe_steps
    }
    recipes.append(new_recipe)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)