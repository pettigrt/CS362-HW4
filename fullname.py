def fullname(firstname, lastname):
    #Ensures input is a string
    if (type(firstname) is not str or type(lastname) is not str):
        raise TypeError
    #Ensures input is not an empty string
    if firstname == "" or lastname == "":
        raise Warning("An input string is empty")
    #Ensures input contains only letters
    if not str(firstname).isalpha() or not str(lastname).isalpha():
        raise TypeError("Inputs must be valid strings with no digits")

    return firstname + ' ' + lastname
