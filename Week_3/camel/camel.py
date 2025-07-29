# name = input("Type the name in camelCase ")
# new_name = ""

# for i in name:
#     if i.islower():
#         new_name += i
#     else:
#         new_name += "_" + i.lower()
# print(new_name)
        
def main():
    camel_case()

def camel_case():
    name = input("Type the name in camelCase ")
    new_name = ""

    for i in name:
        if i.islower():
            new_name += i
        else:
            new_name += "_" + i.lower()
    print(new_name)

main()