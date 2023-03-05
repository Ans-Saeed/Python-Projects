# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

#Class Node to assign values
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
#Counting number of unival trees and storing Bool values True if unival and False if not unival in _ variable
def count_unival_subtree(root):
    count,_ = count_unival_subtree_helper(root)
    return count
# Count unival helper   
def count_unival_subtree_helper(root):
    if root is None:    #Return 0 and True if root is None as an empty tree is unival
        return 0, True
    left_count, is_left_unival= count_unival_subtree_helper(root.left)  #Counting left Unival trees and checking the status of subtrees if unival or not recursively
    right_count, is_right_unival= count_unival_subtree_helper(root.right)   #Counting right Unival trees and checking the status of subtrees if unival or not recursively

    total_count= left_count+right_count     # Total count will be equal to left count + the right count

    if is_left_unival and is_right_unival:      #Cehcking if left subtree and right subtree is unival or not
        if root.left is not None and root.val!= root.left.val:  #If left is present and left value is not equal to root value return the total count and false as it is not unival tree
            return total_count, False
        if root.right is not None and root.val != root.right.val:   #If right is present and right value is not equal to root value return the total count and false as it is not unival tree
            return total_count, False
        return total_count+1, True  # else total count will be incremented as all other cases are of unival subtree 
    return total_count, False   # at end return the total count of subtrees.
    

# create a binary tree
root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

# count the number of unival subtrees
count = count_unival_subtree(root)

# print the result
print(count)
        