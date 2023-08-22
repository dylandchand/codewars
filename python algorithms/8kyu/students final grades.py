# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.

# This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);

# This function should return a number (final grade). There are four types of final grades:

# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases

def final_grade(exam, projects):
    grade = 0
    if exam > 90 or projects > 10:
        grade = 100
    elif exam > 75 and projects >= 5:
        grade = 90
    elif exam > 50 and projects >= 2:
        grade = 75
    return grade