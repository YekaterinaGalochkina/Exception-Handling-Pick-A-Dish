def select_dish(foods, selected_food):
    if selected_food < 0 or selected_food >= len(foods):
        raise IndexError("Out of bound")
    print(f"Ah, {foods[selected_food]}! An excellent choice!")
    print("yum!")


def your_menu(foods):
    while True:
        try:
            index = 1
            for dish in foods:
                print(f"{index}. {dish}")
                index += 1
    
            selected_choice = int(input("Your order number? "))
            select_dish(foods, selected_choice - 1)
            break
        
        except IndexError as error:
            print(f"{error} was entered.")
            print("Next time try entering something on the menu!")

        except ValueError as error:
            print(f"{error} was entered.")
            print("Next time try entering an integer")
            print("------------------")

menu_items = [
    "Yakisoba",
    "Pho Tai Nam Gan",
    "Chile Verde",
    "Swiss & Mushroom Burger",
    "Saag Paneer",
]

your_menu(menu_items)
