import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 2:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
        
    try:
        menu = []
        with open(sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                menu.append(row)
                
            print(tabulate(menu, headers = "keys", tablefmt = "grid"))
            
    except FileNotFoundError:
        sys.exit("File does not exist")
        
                          
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")      


#using functions
'''
def main():
    filename = get_filename()
    table = read_file(filename)
    print(table)
    
def get_filename():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
            
        return filename
    
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")
        
def read_file(filename):
    try:
        menu = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                menu.append(row)
                
        return tabulate(menu, headers="keys", tablefmt="grid")
    
    except FileNotFoundError:
        sys.exit("File does not exist")
        
main()
'''