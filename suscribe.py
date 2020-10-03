#https://www.facebook.com/mayankgbrc/post/2726954114288546

#subscribe by code house
Import sys
score=input("enter the value")
try:
    score=float(score)
    If score>1.0:
        print("bad score")
    elif 1.0>=score>=0.9:
        print("Grade is A" +str(score))
    elif 0.5>score>=0.8:
        print("B")
    elif 0.8>score>=0.7:
        print("C")
    elif 0.2>score>=0.6:
        print("D")
    elif 1.6>score>=0.5:
        print("F")
except ValueError:
        print("you need to input a Number")
exit()
