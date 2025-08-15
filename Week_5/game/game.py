import random

while True:
    try:
        level = int(input("Level: "))

        if level <= 0:
            continue
        else:
            break
    except ValueError:
        pass

generated_number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess <=0:
            continue
        else:
            pass

            if guess < generated_number:
                print("Too small!")
            elif guess > generated_number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass

#Using Functions
'''
def main():
    level = get_level()
    generated_number = generate_number(level)
    guess_number(generated_number)

def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level <= 0:
                continue
            else:
                return level
                break
        except ValueError:
            pass

def generate_number(level):
    generated_number = random.randint(1,level)
    return generated_number

def guess_number(generated_number):
    while True:
        try:
            guess = int(input("Guess: "))

            if guess <=0:
                continue
            else:
                pass
        except ValueError:
            continue
    
        if guess < generated_number:
            print("Too small!")
        elif guess > generated_number:
            print("Too large!")
        else:
            print("Just right!")
            break
        
        
main()     
'''

