#send HTTP requests using requests module
import requests

#define the function
def search_recipes(ingredient, cuisine, app_id, app_key):
    url = f'https://api.edamam.com/search?q={ingredient}&cuisineType={cuisine}&app_id={app_id}&app_key={app_key}' # searching for the ingredient and cuisine in the database using the API ID And API key 
    response = requests.get(url)
    
    if response.status_code == 200: #200 means the API call was successfull
        resp = response.json()
        hits = resp.get("hits", [])
        
        if hits:
          # Sort the recipes by weight
          # The key parameter inside the sorted() function uses a lambda function to access the total weight value for each hit.
            sort_hits = sorted(hits, key=lambda x: x["recipe"]["totalWeight"])
            for hit in sort_hits: # loop to display the recipe name and URL in the terminal
                recipe = hit.get("recipe", {})
                recipe_name = recipe.get("label")
                recipe_url = recipe.get("url")
                print(f"Recipe name: {recipe_name}")
                print(f"Recipe URL: {recipe_url}")
                print()
                
            with open("recipes.txt", "w") as file:
                for hit in sort_hits: # loop to write the recipe name and URL in recipes.txt file
                    recipe = hit.get("recipe", {})
                    recipe_name = recipe.get("label")
                    recipe_url = recipe.get("url")
                    file.write(f"Recipe name: {recipe_name}\n")
                    file.write(f"Recipe URL: {recipe_url}\n")
                    file.write("\n")
                    
            print("Recipe information has been saved to 'recipes.txt'")
        else:
            print("No recipes found")
    else:
        print("There was an error. Please try again.")

ingredient = input("What ingredient are you looking for? ") # user is asked to type in the name of the ingredient he/she needs they recipe for
cuisine = input("What cuisine are you interested in? (british, american, asian, easter europe, central europe, greek, world and many more) ") #user is asked to type in the name of the cuisine
app_id = "x" # replace x the Application ID of the Developer
app_key = "x" # replace x with the Application key of the developer

search_recipes(ingredient, cuisine, app_id, app_key)
