import sys
import os
from PIL import Image, ImageOps

def main():
    #command-line argument

    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")

    valid_exts = (".jpg", ".jpeg", ".png")
    if not sys.argv[1].endswith(valid_exts) or not sys.argv[2].endswith(valid_exts):
        sys.exit("Invalid input")
    if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]: # OR sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]
        sys.exit("Input and output have different extensions")

    try:
        # Open the shirt image (the mask)
        shirt = Image.open("shirt.png")

        # Open the input file
        with Image.open(sys.argv[1]) as photo:

            # Resize and crop input photo to match shirt size
            photo = ImageOps.fit(photo, shirt.size)

            # Paste shirt on top of the resized photo
            photo.paste(shirt, shirt)

            # Save the final image
            photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__=="__main__":
    main()
