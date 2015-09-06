__author__ = 'aaronmsmith'

def median(number_list):

    numbers=list(number_list)
    numbers.sort()
    if len(numbers)%2>0:
        result= numbers[len(numbers)/2]
    else:
        result=(numbers[(len(number_list)/2)-1] + numbers[(len(number_list)/2)])/2.0
    return result

print median ([1,2,3,4])




# def remove_duplicates(number_list):
#     numbers=list(number_list)
#     for i in numbers:
#         print i
#         found=numbers.count(i)
#         print found
#         print " "
#         while found>1:
#             numbers.remove(i)
#             found=numbers.count(i)
#
#     return numbers
#
# print remove_duplicates([4, 5, 5, 4])

# def product(number_list):
#     result=1
#     for i in number_list:
#         result = result * i
#
#     return result


# print product([2,2,2])
#
# def purify(number_list):
#     result=[]
#     for i in number_list:
#         if i % 2==0:
#             result.append(i)
#
#     return result
#
# print purify([1,3,3,4,5,6])


#
# def count(sequence,item):
#     result=0
#     for i in sequence:
#         if i==item:
#             result+=1
#             print result
#
#     return result
#
# print count(["1",2,2,1.3,1],1)


# def censor(text,word):
#     sentence=text
#     r=sentence.find(word)
#     if r>-1:
#       list=sentence.split(word)
#       censor="*" * len(word)
#       new_sentence=censor.join(list)
#
#     return new_sentence
# print censor("this hack is a terrible hack pack", "terrible")



# censored=["hack","wack"]
# sentence="this hack is a hack pack"
# for word in censored:
#     r=sentence.find(word)
#     if r>-1:
#       list=sentence.split(word)
#       censor="*" * len(word)
#       new_sentence="****".join(list)
#
# print new_sentence


# def scrabble_score(word):
#
#     score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#              "x": 8, "z": 10}
#
#     result=0
#     for a in word.lower():
#         result +=score[a]
#
#     return result
#
# print scrabble_score("hello")



# def anti_vowel(word):
#     vowels=["a","e","i","o","u","A","E","I","O","U"]
#     word=word.lower()
#     result=""
#
#
#     for l in word:
#         if vowels.count(l)>0:
#             print l
#         else:
#             result =result + l
#
#     return result
#
# print anti_vowel("This is A test.")



# def reverse(s):
#     result=""
#     x=len(s)
#     while x>0:
#         x-=1
#         result=result + s[x]
#
#     return result
#
# print reverse("ABCD")





#Returns True if x is Prime
# def is_prime(x):
#     y=1
#     primes=[]
#     while y <=(x):
#         if x % y==0:
#            primes.append(y)
#         y+=1
#
#     print primes
#     print len(primes)
#     if len(primes)>2 or x<2:
#         return False
#     else:
#         return True
#
# print is_prime(5)




# def factorial(x):
#     result=1
#     while x>1:
#         print x
#         result = result * x
#         x-=1
#
#     return result
#
# print factorial(3)


# def digit_sum(x):
#     s=str(x)
#     result=0
#     for a in s:
#         result += int(a)
#     return result
#
# print digit_sum(53)