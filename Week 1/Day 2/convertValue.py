def convertValue():
    """
    Select one option from the menu to convert either a string to a number, or a number to a string.
    Options:
    1. convert to String to Number
    2. convert Number to String
    """
    options = int(input('Select one option: \n 1. convert to String to Number \n 2. convert Number to String \n Enter Option: '))
    value = input(' Enter value: ')
    if options == 1:
        return print(' Number: ',int(value), 'Type: ',type(int(value)))
    elif options == 2:
        return print(' Text string: ',str(value), 'Type: ',type(str(value)))
convertValue()