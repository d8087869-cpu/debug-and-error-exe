#1
''' 
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
'''    
#4 
'''
prices = { 
    "apple": 3, 
    "banana": 5 } 
item = input("Enter item: ") 
try:
    print(prices[item])
except KeyError:
    print('item not found ')    
#5
numbers = [100, 200, 300] 
try:
    index = int(input("Choose index: ")) 
    divider = int(input("Choose divider: ")) 
    result = numbers[index] / divider 
    print(result)
except ZeroDivisionError: 
    print('dont divide by 0 ')
except IndexError:
    print('index not in range ') 
except ValueError:
    print('value not an int ')    
    exit()  
 '''   
#6 
'''
try:
    score = int(input("Enter score: ")) 

    print("Your score is", score) 
except ValueError:
    print('invalid val enter int ')
finally:
    print('check finish ')
'''
#7
''''
name = input("Enter your name: ") 

if name == "admin" :

    print("Welcome admin") 

else: 

    print("Welcome user") 
# was missing : , all the rest of the code was runing good    
'''
#8 
price = 100 

discount = 20 

 

final_price = price - discount / 100 

print(final_price)