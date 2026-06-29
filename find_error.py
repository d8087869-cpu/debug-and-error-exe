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
'''
price = 100 

discount = 20 

print(         )

#final_price = price - discount / 100 
final_price = price - price /100* discount 

print(final_price)

#99.8 , expected =80 , 

#9
password = "abc123" 

guess = input("Enter password: ") 

 

if guess == password: 

    print("Login successful") 

else: 

    print("Wrong password") 
#Enter password: 1
#Login successful   
# != / correct ==  
#10
try:
    num1 = int(input("Number 1: ")) 

    op = input("Operator: ") 

    num2 = int(input("Number 2: ")) 
    
    print ('there is no such val')  
         
    if op == "+": 

        print(num1 + num2) 

    elif op == "-": 

        print(num1 - num2) 

    elif op == "*": 

        print(num1 * num2) 

    elif op == "/": 
        
            print(num1 / num2)
            
            print('cant divide by 0 ')    
    else:
        print('invalid opritor')
except ZeroDivisionError:
     print('cant divide by 0 ')
except ValueError:     
     print('except ValueError : ')    
finally:
        print(" calculater closed ")    
'''
#part 2 
#1 
'''
try:
    celsius = input("Celsius: ") 

    fahrenheit = int(celsius) * 9 / 5 + 32 

    print(fahrenheit) 
except ValueError:
    print(" Temperature must be a number. ")    

#2 
try:
    word = input("Enter word: ") 

    print(word[0]) 
except   IndexError:
    print('enter rigth index') 
'''
#3
'''
scores = [90, 80, 100] 

total = 0 

for score in scores: 
#total=score
    total += score 

 
average = total / len(scores) 

print(average)
#33.333336 , correct 90 , bug type loogi 

#4

products = { 
    "pen": 4, 
    "notebook": 12} 
try:
    print()
    product = input("Product: ")



    amount = int(input("Amount: ")) 
    print(products[product] * amount)
except ValueError:    
    print('enter int number')
    exit()
except KeyError:
    print('not in the key options ')    
    exit()
'''
#5 
'''
files = ["data.txt", "users.csv", "notes.txt"] 
try:

 

    choice = int(input("Choose file number: ")) 

    print(files[choice]) 
except ValueError:
    print('only giving val ')
except IndexError:
    print('put a valid index')   
'''

#6 
'''
numbers = [4, 10, 2, 8] 

maximum = 0 

for number in numbers: 
#number < maximum:
    if number > maximum:

        maximum = number 
print(maximum) 
# worng 0 
#10

#7 

user = { 
    "name": "Dana", 
    "age": 25 }
try: 
    field = input("Choose field: ") 
    print(user[field].upper()) 
except KeyError:
    print('in valid key option ')    
'''
#8    
'''
try:
    price = int(input("Price: ")) 
    amount = int(input("Amount: ")) 
except ValueError:
    print('please enter int value ')
total = price * amount 
if amount > 3: 
#amount <3
    total = total - total / 100 * 10
    print(total) 

'''

#9 
try:
    grade = int(input("Grade: ")) 
except ValueError:
    print(" enter a int value")
    exit()
if grade >= 90: 

    print("Excellent") 

elif grade >= 70: 

    print("Good") 

elif grade >= 55: 

    print("Pass") 

else: 

    print("Fail") 
#out put was rigth beqouse the condition start agin evry time 

#10 
try:
    balance = 100 

    action = input("Action: ") 

    amount = int(input("Amount: ")) 

    if action == "deposit": 

        balance = balance + amount 

    elif action == "withdraw": 
        if balance < amount :
            print('not enough money')
        else:
            balance = balance - amount 
    else:
        print('unknown action')

    print("Balance:", balance) 
except ValueError:
    print('enter int value ')
finally:
    print('bank action finished ')    