array=[1,2,3,4,5]
print(*array)
#output: 1 2 3 4 5
str="sanyam"
print(*str)
#output: s a n y a m
# Path: %2A.py
array=[1,2,3,4,5]
print(array)
#output: [1, 2, 3, 4, 5]
print(*array)
#output: 1 2 3 4 5
# Path: %2A.py
array=[1,2,3,4,5]
print(*array,sep=",")
#output: 1,2,3,4,5
print(*array,sep=" ")
#output: 1 2 3 4 5
print(*array,sep="\n")
#output: 1
#        2
#        3
#        4
#        5

array=[1,2,3,4,5]
print(*array, sep=" ", end=' jai ')

array=["sanyam"]
print(*array)