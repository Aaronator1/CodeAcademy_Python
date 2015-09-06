__author__ = 'aaronmsmith'

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results=[]

    for list in lists:
        for number in list:
            results.append(number)
    return results



print flatten(n)