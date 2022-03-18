def name_not_blank(question, error):
    while True:
        try:
            name = input(question)
            if name == "":
                raise ValueError
        except ValueError:
            print(error)
        else:
            return name


name_not_blank("\nWhat is your name? ", "Please ensure you have entered this "
                                        "correctly, and not left it blank")
