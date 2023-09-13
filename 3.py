fib1=fib2=1
n=input ("Номер элемента ряда Фибоначчи:")
n=int(n)
i=0
while i< n-2:
    c=fib1+fib2
    fib1=fib2
    fib2=c
    i=i+1
    print ("Значение этого элемента", fib2)
