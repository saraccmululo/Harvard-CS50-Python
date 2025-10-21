import sys

def main():
    #command-line argument

    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")

    counter=0

    try:
        #open file
        with open (sys.argv[1], "r") as file:
            #read file
            lines=file.readlines()
            for line in lines:
                row=line.strip()
                if row =='' or row.startswith("#"):
                    continue
                else:
                    counter+=1
            print(counter)

    except FileNotFoundError:
        print("File does not exist")

if __name__=="__main__":
    main()
