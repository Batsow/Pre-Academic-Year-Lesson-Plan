import sys
from PIL import Image, ImageOps 


if len(sys.argv) == 3:
    
    if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) and sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    if not sys.argv[2].lower().endswith(sys.argv[1].lower().rsplit(".")[-1]):
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(sys.argv[1] ) as before, Image.open("shirt.png") as after:
            #resize and crop
            desired_size = (600, 600)
            before = ImageOps.fit(before, desired_size)
        
            #paste
            before.paste(after, (0,0), after)

            #save
            before.save(sys.argv[2])
        
    except FileNotFoundError:
        sys.exit("Input does not exist")
        
    
        
elif len(sys.argv) >3:
    sys.exit("too many command-line arguments")
else:
    sys.exit("too few command-line arguments")
    
    
#function
'''    
def main():
    if len(sys.argv) == 3:
        input_file = sys.argv[1].lower()
        output_file = sys.argv[2].lower()

        validate_extensions(input_file, output_file)
        edit_image(input_file, output_file)

    elif len(sys.argv) >3:
        sys.exit("too many command-line arguments")
    else:
        sys.exit("too few command-line arguments")
        
def validate_extensions(input_file, output_file):
    if not input_file.endswith((".jpg", ".jpeg", ".png")) and output_file.endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    if not output_file.endswith(input_file.rsplit(".")[-1]):
        sys.exit("Input and output have different extensions")

def edit_image(input_file, output_file):
    try:
        with Image.open(input_file) as before, Image.open("shirt.png") as after:
            #resize and crop
            desired_size = (600, 600)
            before = ImageOps.fit(before, desired_size)
        
            #paste
            before.paste(after, (0,0), after)

            #save
            before.save(output_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
'''