import csv
import os

def menu(username, products_count):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
     INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
        'Reset'   | Reset the CSV file.
    Please select an operation: """
    return menu

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    products = []

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:

            products.append(dict(row))
    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)

#def auto_incremented_id(products):
#    #return int(products[-1]["id"]) + 1
#    if len(products) == 0:
#        return 1
#    else:
#        all_ids = [int(p["id"]) for p in products]
#        max_id = max(all_ids)
#        next_id = max_id + 1
#        return next_id

def run():

    products = read_products_from_file()

    number_of_products = len(products)
    my_menu = menu(username="JMDORNFELD", products_count=20)
    operation = input(my_menu)

    operation = operation.title()

    if operation == "List":
        print("LISTING PRODUCTS")
        for p in products:
            print("     " + p["id"] + " " + p["name"])

    elif operation == "Show":
        print("SHOWING A PRODUCT")
        product_id = input("What is the identifier of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        print(matching_product)

    elif operation == "Create":
        new_id = auto_incremented_id(products)
        new_product = {
            "new_id", "new_product_name", "new_name", "new_aisle", "new_department", "new_price"
        }
        new_id = input("   What is the new product id?   ")
        new_product_name = input("   What is the new product name?   ")
        new_aisle = input("   Where is the new product located (by aisle)?   ")
        new_department = input("   What department is the new product located in?   ")
        new_price = input("  What is the new product's price?   ")
        products.append(new_product)
        print("-----------------------------------")
        print("CREATING A NEW PRODUCT")
        print(new_id, new_product_name, new_aisle, new_department, new_price)
        print("-----------------------------------")

    elif operation == "Update":
        product_id = input("What is the identifier of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        print(matching_product)
        update_product_name = input("   What is the new product name? If no change, please type in the original product name above:   ")
        update_aisle = input("   Where is the new product located (by aisle)?If no change, please type in the original product aisle above:  ")
        update_department = input("   What department is the new product located in? If no change, please type in the original product department above:  ")
        update_price = input("   What is the new product's price? If no change, please type in the original product price above:   ")
        matching_product["name"] = update_product_name
        matching_product["aisle"] = update_aisle
        matching_product["department"] = update_department
        matching_product["price"] = update_price
        print("-----------------------------------")
        print("UPDATING A PRODUCT")
        print("-----------------------------------")
        print(matching_product)

    elif operation == "Destroy":
        product_id = input("What is the identifier of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        del products[products.index(matching_product)]
        print("DELETING A PRODUCT")

    elif operation == "Reset":
        reset_products_file()
        return
    else:
        print("OOPS, unrecognized input, please select one of 'List', 'Show', 'Create', 'Update', 'Destroy' or 'Reset'")


    write_products_to_file(products=products)

if __name__ == "__main__":
    run()
