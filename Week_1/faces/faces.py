#Ask user for input and then output the same input with emoticons replaced by emojis(real emojies)
def main():
    faces = input().replace(":)","🙂").replace(":(","🙁")
    print(faces)
    
main()