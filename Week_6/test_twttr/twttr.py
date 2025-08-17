#Option 1: Original code that removes vowels from a name input
'''
name = input("Name: ")                                  # Asks name from user                      
vowels = "aeiouAEIOU"                                   # Defines vowels to be removed

for i in vowels:                                        #loop runs through each character(i) in vowels
    name = name.replace(i,"")                           # Replaces each vowel in name with an empty string

print(name)
'''
#Option 2: Refined functions practice

def main():
    name = input("Name: ")
    result = shorten(name)
    print(result)
    
def shorten(word):
    vowels = "aeiouAEIOU"
    for i in vowels:
        word = word.replace(i,"")
    return word
    
if __name__ == "__main__":
    main()


#option 3: Functions approach
'''
# def main():
#     vowel_convertor()
#
# def vowel_convertor():
#     name = input("Name: ")
#     vowels = "aeiouAEIOU"

#     for i in vowels:
#         name = name.replace(i,"")

#     print(name)

# main()
'''
