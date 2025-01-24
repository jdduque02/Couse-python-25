def studentGrades():
    """
    Prompts the user to enter a student's grade and prints a message 
    based on the grade's classification.

    Grades are classified as follows:
    - "This good" for grades between 4 (exclusive) and 5 (exclusive).
    - "This Excelent" for grades greater than 5.
    - "This basic" for grades between 3.5 (inclusive) and 4 (exclusive).
    - "This bad" for grades less than 3.5.
    """

    grade = float(input('Enter the student grade: '))
    if grade >4 and grade < 5:
        return print('This good')
    elif grade >5:
        return print('This Excelent')
    elif grade < 4 and grade >=3.5:
        return print('This basic')
    else:
        return print('This bad')
studentGrades()