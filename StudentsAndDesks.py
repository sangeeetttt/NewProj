'''
5. A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
'''


Astudents = int(input("the no of students in class A: "))
Bstudents = int(input("the no of students in class B: "))
Cstudents = int(input("the no of students in class C: "))

Adesks = int(Astudents//2)
Bdesks = int(Bstudents//2)
Cdesks = int(Cstudents//2)

remA = (Astudents%2)
remB = (Bstudents%2)
remC = (Cstudents%2)
print(f"the remaining students in class A is : {remA}")
print(f"the remaining students in class B is : {remB}")
print(f"the remaining students in class C is : {remC}")

desks = Adesks + Bdesks + Cdesks + remA + remB + remC


print(f"the number of total desks required in A is {Adesks}")
print(f"the number of total desks required in B is {Bdesks}")
print(f"the number of total desks required in C is {Cdesks}")
print(f"the number of total desks required is {desks}")
