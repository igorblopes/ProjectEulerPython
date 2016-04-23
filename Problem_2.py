first = 1
second = 2
aux = 0
sum = 2
while second < 4000000:
    aux = first + second
    if aux % 2 == 0:
        sum += aux
    first = second
    second = aux

print("The sum is", sum)
    
    
    
