
def list_average(l):

    #Ensure the input is a list and is not empty
    
    list_length = len(l)
    if (list_length == 0):
        raise Warning("List cannot be empty")
        
    sum = 0
    for x in range(list_length):
        if not (isinstance(l[x], float) or isinstance(l[x], int)):
            raise TypeError("List elements must be of type int or float")
        else:
            sum = sum + l[x]

    return sum / list_length
