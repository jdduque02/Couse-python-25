def maxMinValue ():
    """
    This function finds the maximum and minimum values in a given list of numbers.
    
    Parameters:
    None
    
    Returns:
    A printed statement showing the maximum and minimum values of the list.
    
    """
    numbersList = [1,2,4,5,6,7,8,12,13,53,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    """  max = 0
    min = numbersList[0]
    for i in numbersList:
        if numbersList[i] > max:
            max = numbersList[i]
        if numbersList[i] < min:
            min = numbersList[i]
    return print(f"Max: {max}, Min: {min}") """
    return print(f"Max: {max(numbersList)}, Min: {min(numbersList)}")
maxMinValue ()