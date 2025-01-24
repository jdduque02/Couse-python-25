import time
def countdown():
    """Print numbers from 10 to 1, with a 0.5s pause
    between each number, and then print 'Blastoff!'.
    """
    for i in range(10, 0, -1):
        print(i)
        time.sleep(0.5)
    print('Blastoff!')
countdown()