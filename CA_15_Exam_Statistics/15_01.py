__author__ = 'aaronmsmith'

def grades_sum(grades):
    running_sum=0.0
    for grade in grades:
        running_sum+=grade

    return running_sum



def print_grades(grades):
    for grade in grades:
        print grade

def grades_average(grades):
    total=grades_sum(grades)
    average=total/float(len(grades))
    return average

def grades_variance(scores):
    variance=0
    average=grades_average(scores)
    for score in scores:
        variance += ((average - score) ** 2)

    result=(variance/float(len(scores)))
    return result

def grades_std_deviation(variance):
    return variance ** .5

print grades_std_deviation(grades_variance([100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]))


