__author__ = 'aaronmsmith'
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

students=[lloyd, alice, tyler]



def average(grades):
    avg=0
    count=0
    sum=0
    for grade in grades:
        sum += grade
        count += 1

    avg=float(sum)/count
    return avg

def average2(grades):
    total= float(sum(grades))
    avg=total/len(grades)
    return avg

for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]


print average(lloyd["homework"])
print average2(lloyd["homework"])