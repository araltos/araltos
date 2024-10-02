import csv
import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                key = row[key_column_index]
                
                if key in compound_dict:
                    print(f"Duplicate product number found: {key}. Skipping...")
                    continue  
                compound_dict[key] = row
    except FileNotFoundError:
        print("Error: missing file")
        print(f"[Errno 2] No such file or directory: '{filename}'")
        exit(1)
    return compound_dict

def main():
    
    print("Inkom Emporium\n")

    
    products_dict = read_dictionary('products.csv', 0)

    
    try:
        with open('request.csv', newline='') as file:
            reader = csv.reader(file)
            next(reader)  
            print("Ordered Items\n")
            total_items = 0
            subtotal = 0
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                product_details = products_dict.get(product_number)
                if product_details:
                    product_name = product_details[1]
                    product_price = float(product_details[2])
                    print(f"{product_name}: {quantity} @ {product_price:.2f}")
                    total_items += quantity
                    subtotal += quantity * product_price
                else:
                    print(f"Error: unknown product ID in the request.csv file\n'{product_number}'")
            print("\nNumber of Items:", total_items)
            print("Subtotal:", f"{subtotal:.2f}")
            sales_tax = subtotal * 0.06
            print("Sales Tax:", f"{sales_tax:.2f}")
            total_amount_due = subtotal + sales_tax
            print("Total:", f"{total_amount_due:.2f}\n")
            print("Thank you for shopping at the Inkom Emporium.")
            print(datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
            print("\nWe value your feedback! Please complete our online survey at www.inkomemporium.com/survey")
    except FileNotFoundError:
        print("Error: missing file")
        print(f"[Errno 2] No such file or directory: 'request.csv'")
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)

if __name__ == "__main__":
    main()
