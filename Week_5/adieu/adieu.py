import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        print("\n")
        break

names = p.join(names)
print(f"Adieu, adieu, to {names}" )




#option 2: using functions
'''
# def main():
#     names = get_names()
#     names = p.join(names)
#     print(f"Adieu, adieu, to {names}")

# def get_names():
#     names = []
#     while True:
#         try:
#             name = input("Name: ")
#             names.append(name)
            
#         except EOFError:
#             print("\n")
#             break
#     return names
    
# main()