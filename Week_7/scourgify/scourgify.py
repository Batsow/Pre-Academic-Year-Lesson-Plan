import sys
import csv

if len(sys.argv) == 3:
    try:
        with open(sys.argv[1], "r") as before, open(sys.argv[2], "w") as after:
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames = ["first"] + ["last"] + ["house"])
            writer.writeheader()
            
            for row in reader:
                last, first = row["name"].split(",")
                writer.writerow(
                    {
                        "first": first, 
                        "last": last, 
                        "house": row["house"]
                    }
                )
                
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")
    
    







#functions
'''
import sys
import csv

def main():
    if len(sys.argv) == 3:
        reader = read_file()
        write_on_file(reader)
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def read_file():
    try:
        before = open(sys.argv[1], "r")
        return csv.DictReader(before)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def write_on_file(reader):
    with open(sys.argv[2], "w") as after:
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow(
                {
                    "first": first,
                    "last": last,
                    "house": row["house"]
                }
            )


main()
'''