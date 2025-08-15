import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level in (1,2,3):
            return level
        else:
            continue 
        
    
def generate_integer(level):
    for i in range(10):
        if level == 1:
            return random.randint(0,9)

        elif level == 2:
            return random.randint(10,99)
        
        else:
            return random.randint(100,999)
        

def main():
    level = get_level()
    score = 0
    
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0
        
        while attempts < 3:
            try:
                z = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                attempts += 1
                continue

            if z == correct_answer:
                score += 1
                break
            else:
                print("EEE")
                attempts += 1
        
        if attempts == 3:
            print(correct_answer)
            
            
    print(f"Score: {score}")
    
if __name__ == "__main__":
    main()
                
             
        
        
     
    