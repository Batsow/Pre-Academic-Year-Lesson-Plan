def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


#takes user input and removes any whitespace and replaces $ with nothing
def dollars_to_float(d):
    d = float(d.strip().replace("$", ""))
    return d

#takes user input and removes any whitespace and replaces % with nothing and turns the percentage into a decimal
def percent_to_float(p):
    p = float(p.strip().replace("%", ""))
    return p / 100


main()