# this fibonacci() function takes in a positive integer and 
# return the nth fibonacci number. nth fibocacci number is 
# the sum of (n-1)th and (n-2)th fibonacci number. like 0th and 
# first fibonacci numbers are 0 and 1 and thus 2nd fibonacci number
# is 0 + 1 = 1, following the same way 3rd, 4th, 5th numbers are 2, 3, 5
# and so on.

def fibonacci(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    c = 1
    for i in range(n):
        b = c
        c = a + b
        a = b
    return b

n = 10
if __name__ == "__main__":
    print(fibonacci(n))