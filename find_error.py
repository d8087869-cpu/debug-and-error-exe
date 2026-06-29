#1 
age = input("Enter your age: ") 
try:
    next_year = int(age) + 1 
except ValueError:
    print('age must be a number')
    exit()
print("Next year you will be", next_year)
#2 
try:
    a = int(input("First number: ")) 
    b = int(input("Second number: ")) 
    print(a / b) 
except ZeroDivisionError:
    print('cannot divide by zero')
except ValueError:
    print('enter int or flaot ')    
#3 
try:
    numbers = [10, 20, 30] 
    index = int(input("Choose index: ")) 
    print(numbers[index])
except IndexError:
    print('index not found ')   
except ValueError:
    print('enter only int numbers ')    