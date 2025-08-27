print('Hello Python for Everybody - Michigan University!')

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        n = int(num)
    except:
        print('Invalid input')
         
    if largest == None:
        largest = n
    if smallest == None:
        smallest = n

    if n > largest:
        largest = n
        
    if n < smallest:
        smallest = n
        
    if num == "done":
        break
print("Maximum is", largest)
print("Minimum is", smallest)

