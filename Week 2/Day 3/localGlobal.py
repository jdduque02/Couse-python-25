x = 5
def local():
    """
    Print the value of x, which is local to this function.
    """
    x = 10
    print(x)
print(x)
local()