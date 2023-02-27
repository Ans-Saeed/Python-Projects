def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first(a,b):
        return a
    return pair(first)

def cdr(pair):
    def last(a,b):
        return b
    return pair(last)
        
cons = cons(3, 4)
f = car(cons)
l = cdr(cons)
print(f) # Output: 3
print(l) # Output: 4