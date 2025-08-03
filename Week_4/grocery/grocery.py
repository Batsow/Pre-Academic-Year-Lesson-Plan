grocery = {}

while True:
    try:
        item = input("").strip().upper()
        
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

    except EOFError:
        print("\n")
        break

for item in sorted(grocery):
    print(f"{grocery[item]} {item}")













































# grocery = {}


# while True:
#     try:
#         item = input("").strip().upper()
            
#         if item in grocery:
#             grocery[item] += 1
#         else:
#             grocery[item] = 1

#         for item in grocery:
#             x = list(grocery.keys())
#             x.sort()
#             print(x)
#             #print(f"{grocery[item]} {item}")

#     except EOFError:
#         print("\n")
#         break


# while True:
#     item = dict(input("Item: ")).upper()





