listGlobal = [1,2,3,4,5,6,7,8,9,10]
print(listGlobal)
def editGlobal():
    """Edita el primer elemento de la lista global."""
    listGlobal[0] = 0
    return print(listGlobal)

editGlobal()