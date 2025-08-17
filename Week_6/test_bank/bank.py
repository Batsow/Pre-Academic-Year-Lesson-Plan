def main():
    greeting = input("Greeting: ").strip()
    result = value(greeting)
    print(f"${result}")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()








#option1
'''
greeting = input("Greeting: ")
greeting = greeting.lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
'''

#option 2 practicing functions
'''
def greeting_cost():
    greeting = input("Greeting: ")
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")
        
greeting_cost() #calling the function to execute it
'''


#option 3 practicing functions with return
'''
def greeting_cost():
    greeting = input("Greeting: ")
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"
    
results = greeting_cost()                                    # calling the function to execute it
print(results)                                               # printing the result returned by the function
'''

#option 4 using match
'''
greeting = input("Greeting: ")
greeting = greeting.lower().strip()

match greeting:
    case _ if greeting.startswith("hello"):
        print("$0")
    case _ if greeting.startswith("h"):
        print("$20")
    case _:
        print("$100")
'''