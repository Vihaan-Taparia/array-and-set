#ACTIVITY 1
#DIFF TYPES OF SETS
#SET OF INTEGERS
my_set={1,2,3}
print(my_set)

#set of mixed datatypes
my_set={1.0,"Hello",(1,2,3)}
print(my_set)

#set cannot have duplicates
my_set={1,2,3,3,2,2,1}
print(my_set)

#we can make a set from list
my_set=set[1,2,3,4]
print(my_set,"\n")

#remove a number from set
num_set=set([0,1,2,3,4,5])
print("Original set=",num_set)
num_set.pop()
print("After removing the first element of the set:",num_set)