#Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

def listfunction():
    total=0

    my_list=list(input().split())

    for x in my_list:
        y=x.upper()
        letters = []
        count=0
        for j in y:

            letters.append(j)

            count=count+1
        if letters[0]==letters[-1] and count>=2:
            total=total+1
    print(total)



if __name__ == '__main__':
        listfunction()








