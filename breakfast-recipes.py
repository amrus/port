# Recipe catalog that keeps track of all my recipes

recipeCatalogList = ["Scrambled Eggs", "Acai Bowl"]

#Ingredients dictionary that stores the list of ingredients for this recipe

ingredientsDict = {
    "Scrambled Eggs" :[
        "eggs: 3",
        "olive oil: 2 TS",
        "grated cheese: 1 TBS",
        "salt: to taste",
        "pepper: to taste",
        "dried thyme: 1 TS"
    ],

    "Acai Bowl" :[
        "Vegan Ingredients",
        "Two 4-ounce packets unsweetened frozen acai puree",
        "1 medium banana",
        "1/2 cup blueberries",
        "1 tablespoon honey",
        "3 tablespoons granola",
        "2 tablespoons pomegranate seeds",
        "1 tablespoon unsweetened coconut flakes",
    ]


}

# The dictionary that stores prep steps
prepStepDict = {
    "Scrambled Eggs" :[
        "1. crack eggs in a bowl and whisk",
        "2.in a pan that's heated pour the egg mixture",
        "3. Once eggs are somewhat cooked, sprinkle salt, pepper, thyme and cheese"
    ],

    "Acai Bowl" :[
        " 1. Break the frozen acai up a little by slapping the sealed packets on the countertop or hitting them with a meal mallet.",
        " 2. Blend the berries with 1/2 the banana, 1/4 cup of the blueberries and the honey in the blender" ,
        " 3. Mix as needed, until it's the consistency of a thick smoothie; transfer to a cereal bowl." ,
        " 4. Slice the remaining 1/2 banana."
        " 5. Arrange the slices, the remaining 1/4 cup blueberries, granola, pomegranate seeds and coconut flakes in neat piles or rows on top of the acai. "
        " 6. Take a photo for Instagram or Snapchat!"

    ]
}

# This function will find and print a recipe
def findRecipe (recipeName) :
    recipeFound = 0
    for recipe, ingredients in ingredientsDict.items():
        if recipe == recipeName:
            recipeFound += 1
            print ("\nThis recipe is for: ", recipeName)
            print ("\nIngredients:")
            for item in ingredients:
                print(item)
# Printing all steps in a recipe
    for recipe, steps in prepStepDict.items():
        if recipe == recipeName:
            recipeFound += 1
            print ("\nPrepartion Steps:")
            for item in steps:
                print(item)
    return recipeFound



# print the list of recipes available
for recipe in recipeCatalogList:
    print (recipe)


# Get input for the recipe that user wants to print
selectedRecipe = input("Please provide a recipe name from the choices above: ")

# Call function to find and print the recipe
result = findRecipe(selectedRecipe)
# Evaluate result and print message acccordingly
if result == 0:
    print ("Oops! Your recipe has not been found!")
elif result < 2:
    print ("Sorry! Your recipe has not been completed.")
else:
    print ("Recipe found and printed successfuly!")

if print ("Recipe found and printed successfuly")

# User adds new recipes
addRecipes = input("Is there any recipe that you want to add?")

#
