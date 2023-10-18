def palindrome(val):
    # Using the string slicing concept, you can get reverse the string. 
    # ::-1 corresponds to start:stop:step. When you pass -1 as step, 
    # the start point goes to the end and stop at the front.
    rev = val[::-1]
    return val == rev
    
val = input("Enter the value: ")
result = palindrome(val)

if( result ):
    print("Palindrome")
else:
    print("Not Palindrome")