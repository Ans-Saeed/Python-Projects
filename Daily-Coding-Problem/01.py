# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def sum2(nums,k):
    seen={} #Initialize an empty dictionary
    for x in nums:  #Loop through the list
        if k-x in seen: #Target - number of a list if found in dictionary return true
            return True 
        
        seen[x]=True    #Store in dictionary if not seen in dictionary

    return False    #Return False if sum not found in List

nums=[10,15,2,5]
k=17

print(sum2(nums,k))