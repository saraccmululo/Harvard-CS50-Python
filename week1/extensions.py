user_input = input("File name: ").strip().lower()
filename = user_input.split(".")[-1]

match filename:
    case("gif"):
        print("image/gif")
    case("png"):
        print("image/png")
    case("jpeg"|"jpg"):
        print("image/jpeg")
    case("pdf"):
        print("application/pdf")
    case("txt"):
        print("text/plain")
    case("zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")
