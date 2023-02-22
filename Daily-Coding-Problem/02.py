# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?
#First approach calculating the product and dividing it by self
def product_except_self(nums)->list:
    newnums=[]
    product=1
    for i in range (len(nums)): #Loop to calculate the product of nums
        product *=nums[i]
    for j in range (len(nums)): #Loop to calculate the new array using product/the number
        newnums.append(int(product/nums[j]))
    return newnums


#A better approach to solve without division nums=[1,2,3,4,5]
def product_except_self_better(nums):
    n=len(nums)
    prefix=[1]*n    #Initialize Prefix [1,1,1,1,1]
    suffix=[1]*n    #Initialize Suffix [1,1,1,1,1]

    for i in range (1,n):   #Itreate from 1 to 4
        prefix[i]=prefix[i-1]*nums[i-1] #Calculate left side which will give [1,1,2,6,24]
        suffix[n-i-1]=suffix[n-i]*nums[n-i] #Calculate the right side which will give [120,60,20,5,1]
    result=[prefix[i]*suffix[i] for i in range(n)]  #Final multiply left to right using loop from 1 to 4 which will give [120,60,40,30,24]
    return result

nums=[1,2,3,4,5]
rnums=product_except_self(nums)
print(rnums)
print(product_except_self_better(nums))