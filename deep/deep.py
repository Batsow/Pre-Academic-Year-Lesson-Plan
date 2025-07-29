# This code checks if the user's input matches the answer to the Great Question of Life, the Universe, and Everything.
# question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# if (question.strip() == "42") or (question.strip().lower().replace("-"," ") == "forty two"):
#     print("Yes")
# else:
#     print("No")

    
# def deep():
#     question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#     if (question.strip() == "42") or (question.strip().lower().replace("-"," ") == "forty two"):
#         print("Yes")
#     else:
#         print("No")
        
# deep()


def deep():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    if (question.strip() == "42") or (question.strip().lower().replace("-"," ") == "forty two"):
        return "Yes"
    else:
        return "No"

results = deep()
print(results)