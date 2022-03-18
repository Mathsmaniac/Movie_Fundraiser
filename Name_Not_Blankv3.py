def name_not_blank(question):
    while True:
        try:
            name = input(question)
            if name == "" or name.isspace():
                raise ValueError
        except ValueError:
            print("Please ensure you have entered this correctly, and not lef"
                  "t it blank")
        else:
            return name


name_not_blank("\nWhat is your name? ")
