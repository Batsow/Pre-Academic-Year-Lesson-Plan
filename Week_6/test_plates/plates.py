def main():
    
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if max_and_min_length(plate) and starts_with_two_aphabets(plate) and is_alphanumeric(plate) and numbers_at_end_and_no_leading_zero(plate):
        return True
    else:
        return False
    
# Check if the length of the plate is between 2 and 6 characters
def max_and_min_length(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        return False
    
# Check if the first two characters are alphabets
def starts_with_two_aphabets(plate):
    if plate[0:2].isalpha():
        return True
    else:
        return False

# Check if the plate contains only alphanumeric characters
def is_alphanumeric(plate):
    if plate.isalnum():
        return True
    else:
        return False

# check that numbers are at the end and do not start with 0
def numbers_at_end_and_no_leading_zero(plate):
    for i in range(len(plate)):
        if plate[i].isdigit():
            if plate[i] == "0":
                return False
            elif plate[i:].isdigit():
                return True
            else:
                return False
    return True
        
if __name__ == "__main__":
    main()
        
    
    
