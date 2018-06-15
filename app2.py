# code used the starter pack and solution code provided based on error unable to correctly modify.
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
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "products.csv")
    #print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            #print(row["name"], row["price"])
            products.append(dict(row))
    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "products.csv")
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader() # uses fieldnames set above
        for p in products:
            writer.writerow(p)

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)

def auto_incremented_id(products):
   if len(products) == 0:
       return 1
   else:
       product_ids = [int(p["id"]) for p in products]
       return max(product_ids) + 1

def run():
    # First, read products from file...
    products = read_products_from_file()

    # Then, prompt the user to select an operation...
    number_of_products = len(products)
    my_menu = menu(username="JMDORNFELD", products_count=20)
    operation = input(my_menu)
    #print("YOU CHOSE: " + operation)

    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    operation = operation.title()

    if operation == "List":
        print("LISTING PRODUCTS")
        for p in products:
            print("     " + p["id"] + " " + p["name"])

    elif operation == "Show":
        print("SHOWING A PRODUCT")
        product_id = input("What is the identifier  of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        print(matching_product)

    elif operation == "Create":
        new_id = auto_incremented_id(products)
        new_product = {
            "id": new_id,
            "name": "new product name",
            "aisle": "new aisle",
            "department": "new department"
            }
        new_name = input("  Please enter the new product name:   ")
        new_aisle = input("  Please enter the new product aisle:   ")
        new_department = input("   Please enter the new product department:   ")
        new_price = input("   Please enter the new product price:   ")
        products.append(new_product)
        print("---------------------------")
        print("CREATING A NEW PRODUCT")
        print(new_id, new_name, new_aisle, new_department,  new_price)
        print("---------------------------")

    elif operation == "Update":
        product_id = input("What is the identifier of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        print(matching_product)

        update_product = {
            "name": "updated product name",
            "aisle": "new product aisle",
            "department": "new product department",
            "price": "new product price"
            }
        update_name = input("  Please enter the updated product name:   ")
        update_aisle = input("  Please enter the updated product aisle:   ")
        update_department = input("   Please enter the new product department:   ")
        update_price = input("   Please enter the new product price:   ")
        matching_product["price"] = update_price
        print("---------------------------")
        print("UPDATING A PRODUCT")
        print("---------------------------")

    elif operation == "Destroy":
        product_id = input("What is the identifier of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        del products[products.index(matching_product)]
        print("---------------------------")
        print("DELETING A PRODUCT")
        print("---------------------------")

    elif operation == "Reset":
        reset_products_file()
        return # exit the program early to prevent execution of the write_products_to_file() function below (because we don't want to write the original list of products to file in situations where we are instead trying to reset the file)
    else:
        print("---------------------------")
        print("---------------------------")
        print("---------------------------")
        print("OOPS, unrecognized operation, please select one of 'List', 'Show', 'Create', 'Update', 'Destroy' or 'Reset'")

    # Finally, save products to file so they persist after script is done...
    write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
