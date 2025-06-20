import array as arr

#ceate an array
array_num=arr.array('i',[1,3,5,7,9,3])
print("Original array is",array_num)

#count the nummber of occurences
print("Number of occurnces of the number 3 in the given array is:"+str(array_num.count(3)))

#reverse the array
array_num.reverse()
print("The reverse order of the given array is")
print(str(array_num))