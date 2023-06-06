import requests
def search_recipes(ingredient, app_id, app_key): # function created to make the API request with the required ingredient
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}' #searching for the ingredient in the database using the API ID And API key
    response = requests.get(url)
    if response.status_code == 200:
        resp = response.json()
        hits = resp.get("hits", [])
        if hits:
            for hit in hits:
                recipe= hit.get("recipe", {})
                recipe_name = recipe.get("label")
                recipe_url = recipe.get("url")

                print(f"Recipe`s name is: {recipe_name}") #display the recipe`s name
                print(f"Recipe`s URL: {recipe_url}") #display the recipe`s link for that search`
                print("\n") #display a new line to separate the results
        else:
            print("No recipes found")
    else:
        print("There has been an error, please try again.")

ingredient = input("What ingredient are you looking for? ") #ask the user to add the name of the ingredient
app_id = " " #this is the Application ID of the Developer
app_key = " " #this is the Application key of the developer

search_recipes(ingredient, app_id, app_key ) #call the function





#recipe="https://www.edamam.com/results/recipes/?search={}".format(ingredient) #another URL for recipes based on the input (you can add multiple ingredients)


