def store_values():
    values = []
    
    while True:
        num = int(input("Enter a number (0 to stop): "))
        
        if num == 0:
            break
        elif num >0:
            values.append(num)
        else:
            print("Please enter a positive number or 0 to stop.")
    print(values)
store_values()