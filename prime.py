def prime(n):
    if n<=1 or n == None:
        return "prime number starts from 2"
    #print(f"number inside  is {n} in {prime.__name__}")
    ## intializing a temporary variable with False
    temp = False
    ## We will check if the number is greater than 1 or not
    ## since prime numbers starts from 2
    if n > 1:
        #print(f"inside if condition of {prime.__name__}")
        ## checking the divisors of the number
        for i in range(2, n):
            if (n % i) == 0:
                print(f"for number {n} the divisor found is {i}")
                ## if any divisor is found then set temp to true since it is not prime number
                temp = True
                ## Break the loop if it is not prime
                break
    if(temp):
        return f"The given number {n} is not prime number"
    else:
        return f"The given number {n} is prime number"
