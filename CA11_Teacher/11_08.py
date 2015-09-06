lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!


def get_average(student):
    homework=float(sum(student["homework"]))/len(student["homework"])
    quizzes=float(sum(student["quizzes"]))/len(student["quizzes"])
    tests=float(sum(student["tests"]))/len(student["tests"])
    
    weighted_avg=(homework * .1) + quizzes * .3 + tests * .6
    #final_grade=get_letter_grade(weighted_avg)
    return weighted_avg
    

    
def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
    
    
def average(grades):
    avg=0
    count=0
    sum=0
    for grade in grades:
        sum += grade
        count += 1

    avg=float(sum)/count
    return avg
    
def get_class_average(students):
    results=0
    count=0
    for student in students:
        count+=1
        results+=get_average(student)

    return results/count

l=[alice]
print get_class_average(l)