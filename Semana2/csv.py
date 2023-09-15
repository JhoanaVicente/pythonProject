import os
import csv


# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
class DictReader:
    pass

def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, "r") as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Process each row in the CSV file
        for row in csv_reader:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string

# Call the function
print(contents_of_file("flowers.csv"))
