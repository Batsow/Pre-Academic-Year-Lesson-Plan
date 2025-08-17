def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
            break
        except (ValueError, ZeroDivisionError):
            pass                                        # If an error occurs, prompt for input again


def convert(fraction):
    x,y = fraction.split("/")
    x,y = int(x),int(y)
            
    if y == 0:
        raise ZeroDivisionError
    elif x < 0 or y < 0:          #reject negatives like -3/4 or 3/-4 where numerator or denominator is negative
        raise ValueError
    elif x > y:                  #reject fractions like 5/4 or 6/5 where numerator is greater than denominator
        raise ValueError
            
    percentage = round((x/y) * 100)
    return percentage
        
        
        

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    
if __name__ == "__main__":
    main()










# def main():
#     percentage = get_int()
#     if percentage <= 1:
#         print("E")
#     elif percentage >= 99:
#         print("F")
#     else:
#         print(f"{percentage}%")

# def get_int():
#     while True:
#         try:
#             fraction = input("Fraction: ")
#             x,y = fraction.split("/")
#             x,y = int(x),int(y)
            
#             if y == 0:
#                 raise ZeroDivisionError
#             elif x < 0 or y < 0:          #reject negatives like -3/4 or 3/-4 where numerator or denominator is negative
#                 raise ValueError
#             elif x > y:                  #reject fractions like 5/4 or 6/5 where numerator is greater than denominator
#                 raise ValueError
            
#             percentage = round((x/y) * 100)
#             return percentage
        
#         except (ValueError, ZeroDivisionError):
#             pass
        

# main()
