def algorithms(val):
    #1st convert to array
    #2nd use sorted to sort array
    return sorted(list(val))
    
val = input("Enter the value: ")
result = algorithms(val)
print(result)
