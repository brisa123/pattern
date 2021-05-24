# sort list with bubble sort. dont use sort inbuilt method.

my_list=[5,33,6,8,10]

n=len(my_list)

for i in range(n):
    for j in range(1,n-i-1):
        if my_list[j]>my_list[j+1]:
            my_list[j], my_list[j+1]=my_list[j+1], my_list[j]

print(my_list)
#for i in range(len(my_list)):
#    print(my_list[i], end=" ")
