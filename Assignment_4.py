#TUPLES.........

#Q1

t=(1,2,3,"a",[10,20,30])
print(len(t))

#Q2

t1=(20,34,45,10,67,84)
print(max(t1))# for maximum
print(min(t1))#for minimum

#Q3

t2=(4,5,6,7,)
j=1
for i in t2:
    j=i*j
print(j)

#SETS.......

#Q1. Create two set using user defined values.

a=input("enter value")
b=input("enter value")
c=input("enter value")
d=input("enter value")
s1=set([a,b])
print(s1)
s2=set([c,d])
print(s2)

#Q1 Difference between two sets

s1 = {10, 20, 30, 40, 50}
s2 = {100, 30, 80, 40, 60}
s3=s1-s2
print(s3)#elements present in A but not in B

s3=s2-s1
print(s3)#elements present in B but not in A


#Q2 . comparision between two sets

a=set([1,2,3,4,5])
b=set([3,4,5])
print(a>=b)#superset
print (a<=b)#subset


#Q3.Print the result of intersection of two sets.

a=set([1,2,3,4,5])
b=set([3,4,5,6])
print(a&b)


#DICTIONARIES.......

#Q1.Create a dictionary to store name and marks of 10 students by user input.

name=input("enter name of student")
marks=input("enter marks")
D={"name":name,"marks":marks}
print(D)


#Q2 Sort the dictionary created in previous question according to marks

marks={"a":45,"b":33,"c":64,"d":71,"e":29,"f":45,"g":97,"h":81,"i":56,"j":87}
s=sorted(marks.items(),key=lambda t:t[1])
print(dict(s))


#Que.3


l=["M","I","S","S","I","S","I","P","P","I"]
m=l.count("M")
i=l.count("I")
s=l.count("S")
p=l.count("P")
d2={"M":m,"I":i,"S":s,"P":p}
print(d2)






