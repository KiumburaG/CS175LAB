#Restaurant Specifications

searches = str(input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end): "))
while searches == 'Yes':
    vegetarian = str(input("Is anyone in your party vegeterian? "))
    vegan = str(input("Is anyone in your vegan? "))
    gluten_free = str(input("Is anyone in your party gluten-free? "))

    if vegetarian == 'No' and vegan == 'No' and gluten_free == 'No':
            print('')
            print("Here are your restaurant choices.")
            print("Joe's Gourmet Burgers")
            print("Corner Café")
            print("The Chef's Kitchen")
            print("Main Street Pizza Company")
            print("Mama's Fine Italian")
            exit()
    elif vegetarian == 'No' and vegan == 'Yes' and gluten_free == 'No':
            print('')
            print("Here are your restaurant choices.")
            print("Corner Café")
            print("The Chef's Kitchen")
            exit()
    elif vegetarian == 'No' and vegan == 'No' and gluten_free == 'Yes':
            print('')
            print("Here are your restaurant choices.")
            print("Corner Café")
            print("The Chef's Kitchen")
            exit()
    elif vegetarian == 'No' and vegan == 'Yes' and gluten_free == 'Yes':
            print('')
            print("Here are your restaurant choices.")
            print("Corner Café")
            print("The Chef's Kitchen")
            exit()
    elif vegetarian == 'Yes' and vegan == 'No' and gluten_free == 'No':
            print('')
            print("Here are your restaurant choices.")
            print("Mama's Fine Italian")
            print("Corner Café")
            print("The Chef's Kitchen")
            exit()
    elif vegetarian == 'Yes' and vegan == 'Yes' and gluten_free == 'No':
            print('')
            print("Here are your restaurant choices.")
            print("Corner Café")
            print("The Chef's Kitchen")
            exit()
    elif vegetarian == 'Yes' and vegan == 'No' and gluten_free == 'Yes':
            print('')
            print("Here are your restaurant choices.")
            print("Main Street Pizza Company")
            print("Corner Café")
            print("The Chef's Kitchen")
            exit()
    elif vegetarian == 'Yes' and vegan == 'Yes' and gluten_free == 'Yes':
            print('')
            print("Here are your restaurant choices.")
            print("Corner Café")
            print("The Chef's Kitchen")
            exit()

while searches == 'No':
        exit()