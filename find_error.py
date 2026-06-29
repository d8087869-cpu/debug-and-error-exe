#1 
age = input("Enter your age: ") 
try:
    next_year = int(age) + 1 
except ValueError:
    print('age must be a number')
    exit()
print("Next year you will be", next_year)
