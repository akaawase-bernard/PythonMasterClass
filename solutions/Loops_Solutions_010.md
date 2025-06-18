## Loops Solutions (010)

1. Write a loop that goes over a set number of length 10

       import time
       a = 0
       b = 10

       for _ in range (a,b):
           time.sleep(0.25)
           a = a +1

2. Print out the numbers to screen

        print(a)
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
   
3. Write a loop that starting with k = 3 and loop until k becomes 8 (increment should be 1)

        k = 3
        while k < 8:
            time.sleep(0.5)
            print(f"{k} is less than 8")
            k = k + 1

        3 is less than 8
        4 is less than 8
        5 is less than 8
        6 is less than 8
        7 is less than 8