def print_catalog():
    # Base prices
    item1 = 200.0
    item2 = 400.0
    item3 = 600.0

    # Discounts
    combo_discount = 0.10
    gift_discount = 0.25

    # Calculations
    combo_1_2 = (item1 + item2) * (1 - combo_discount)
    combo_2_3 = (item2 + item3) * (1 - combo_discount)
    combo_1_3 = (item1 + item3) * (1 - combo_discount)
    gift_pack = (item1 + item2 + item3) * (1 - gift_discount)

    # Output
    print("Online Store")
    print("--------------------")
    print("Product(S)\t\t\t\t\tPrice")
    print(f"Item 1\t\t\t\t\t\t{item1}")
    print(f"Item 2\t\t\t\t\t\t{item2}")
    print(f"Item 3\t\t\t\t\t\t{item3}")
    print(f"Combo 1 (Item 1 + 2)\t\t{combo_1_2}")
    print(f"Combo 2 (Item 2 + 3)\t\t{combo_2_3}")
    print(f"Combo 3 (Item 1 + 3)\t\t{combo_1_3}")
    print(f"Combo 4(Item 1 + 2 + 3)\t\t{gift_pack}")
    print("_________________________")
    print("For delivery Contact: 9876467889")
# Call the function
print_catalog()

