import emoji

def main():
    user_input =  input("Input: ")
    user_input = emoji.emojize(user_input, language = "alias" )
    print(f"Output: {user_input}")
    
main()



#option 2: importing the exact function we want to use
'''
    from emoji import emojize

    def main():
    user_input = input("Input: ")
    user_input = emojize(f"Output: {user_input}", language = "alias")
    print(user_input)

    main()
'''


#option 3: using a helper function
'''
def main():
    text_to_emoji()
    
def text_to_emoji():
    user_input =  input("Input: ")
    user_input = emoji.emojize(f"Output: {user_input}", language = "alias" )
    print(user_input)
    
main()
'''
    
