#My first approach to solve the problem
def palindrome(x)->bool:
    t=str(x)  #Converting integer to string
    l=[]    #Creating new list to store x in reverse order
    m=""    #Creating new string to store reversed list in m
    for i in range(len(t)-1,-1,-1):     #Loop to store string in list
        l.append(t[i])
    for j in range(len(l)):         #Loop to store list in string
        m+=l[j]
    
    if (str(m)==t):     #Compare two strings and return
        return True
    else:
        return False
r=palindrome(111)
if r:
    print("The number is palimdrome.")
else:
    print("The number is not palimdrome.")


#Best approach to solve the problem ;D

def palindrom(x)->bool:
    return str(x)==str(x)[::-1]

r=palindrom(121)
if r:
    print("The number is palimdrome.")
else:
    print("The number is not palimdrome.")