import sys

if len(sys.argv) == 2:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
        
    
    #loads the file and reads it and then stores it in a list    
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Strips whitespace and comments from each line, then counts the lines of code
    count = 0
    for line in lines:
        if line.lstrip().startswith("#"):
            continue
        elif line.strip() == "":
            continue
        else:
            count += 1

    print(count)
    
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")




#functions practice usage:
'''
def main():
    if len(sys.argv) == 2:
        if not sys.argv[1].endswith(".py"):       
            sys.exit("Not a python file")
            
        result = open_file()
        result = read_file(result)
        print(result)
        
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")
    

def open_file():
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        sys.exit("File does not exist")
        
        
        
def read_file(lines):
    count = 0
    for line in lines:
        if line.lstrip().startswith("#"):
            continue
        elif line.strip() == "":
            continue
        else:
            count += 1

    return count

main()
'''
    