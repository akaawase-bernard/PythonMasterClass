## Functions Solutions (006)

1. Create simple math function with doc string

       def sum(a,b):
            '''
            Function adds any two values together and produces the sum as a result.
        
            Example:
            sum(1,2)
            output = 3
            '''
            return print(a+b)

       sum (1,2)
       3

       sum (1100,2345)
       3445

       sum (2**2,3**3)
       31

2. Use help function on the doc string

       help(sum)

       Help on function sum in module __main__:
        
        sum(a, b)
        Function adds any two values together and produces the sum as a result.
        
        Example:
        sum(1,2)
        output = 3