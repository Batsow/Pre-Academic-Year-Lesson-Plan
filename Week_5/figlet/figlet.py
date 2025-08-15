import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
font_list = figlet.getFonts()


if len(sys.argv) == 1:                              #Checks if no extra command-line arguments were given
    user_input = input("Input: ")
    user_font = choice(font_list)
    user_font = figlet.setFont(font = user_font)
    print(figlet.renderText(user_input))
    
    
elif len(sys.argv) == 3:                             #Checks if exactly two extra command-line arguments were given
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
        user_input = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(user_input))
    else:
        sys.exit("Invalid font")
else:
    sys.exit("Too many arguments")


#option 2: using functions
'''
import sys
from pyfiglet import Figlet
from random import choice   

figlet = Figlet()
font_list = figlet.getFonts()
 
def main():
    
    if len(sys.argv) == 1:
        no_argument_font_interpreter()
    elif len(sys.argv) == 3:
        two_argument_font_interpreter()
    else:
        sys.exit("Too many arguments")
        
        

def no_argument_font_interpreter():                             #Checks if no extra command-line arguments were given
    user_input = input("Input: ")
    user_font = choice(font_list)
    user_font = figlet.setFont(font = user_font)
    print(figlet.renderText(user_input))
    
def two_argument_font_interpreter():                             #Checks if exactly two extra command-line arguments were given
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
        user_input = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(user_input))
    else:
        sys.exit("Invalid font")
        
main()
'''

