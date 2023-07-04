def average(a,b):
    ''' Function takes two values and returns a single value'''
    ans = (a+b)/2
    print(ans)
    print(average.__doc__)
average(4,7)    
#whenever string literals are present just after the definition of a function,class,or method,they are associated with theie doc attribute
#used to provide document our code
#PEP - python Enhancement proposel provides guidelines and best practices on how to write python code .The prime focus of PEP 8 is to improve the readability of the code