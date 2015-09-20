def fibonacci(sequence_length):
    "Return the Fibonacci sequence of length *sequence_length*"
    sequence = [0,1]
    if sequence_length < 1:
        print("Fibonacci sequence only defined for length 1 or greater")
        return
    elif sequence_length >=3:
        for i in range(2,sequence_length): 
            sequence=sequence+[sequence[i-1]+sequence[i-2]]
    return sequence

def factorial(n):
    "Return the factorial of number *n*"
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
