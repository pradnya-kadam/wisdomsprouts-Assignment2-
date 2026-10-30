
#1
# def is_even(n):
#     if n%2==0:
#         print("number is even")
#     else:
#         print("numbre is odd")

# is_even(10)

#2
# def largest_no(num1,num2):
#     if num1>num2:
#         print("num1 is greater")
#     else:
#         print("num2 is greater")
# largest_no(20,30)

#3
#def print_numbers(num):
#    for i in range(1,num):
#        print(i)

#print_numbers(20)



#4
# def sum(num):
#     for i in range(1,num):
#         num+=i
#     print(num)
# sum(5)


#5  
# def mult(num):
#     for i in range(1,11):
#         print(i*num)
# mult(9)
        
#6
# def count_even(num):
#     count=0
#     for nu in num:
#         if nu%2==0:
#             count+=1
#         print(count)
        
# count_even([1,2,3,4,5])

#7
# def max(num):
#     largest=0
#     for i in num:
#         if i>largest:
#             largest=num
#     return largest

# print(max([1,2,3,4,5]))


#11
# def fizz_buzz():
#     for i in range(1,100):
#         print(i)
#     if i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     elif i%3==0 and i%5==0:
#         print("fizzbuzz")

# fizz_buzz()

#12
#palindrome checker 

# def palindrome(str):
#     s=str
#     if s==s[-1]:
#         return True
#     else:
#         return False
# palindrome("nayan")


#13      
# def count_vowel(str):
#     v="AEIOUaeiou"
#     count=0
#     if v in str:
#         count+=1
    
# print(count_vowel("pradnya"))

#14
# def second_largest(num):
#     largest=0
#     s_largest=0
#     for i in num:
#         if i>largest:
#             s_largest=largest
#             largest=i
#         elif i>s_largest and i<largest:
#             s_largest=i
#     return s_largest
            

# print(second_largest([1,2,3,4,5]))
    

#15
# def guessing_game():
#     secret=random.randint(1,10)
#     while True:
#         guess=int(input("guess a number between 1 10"))

#         if guess==secret:
#             return "successfully guessed"
#             break
#         else:
#             return "wrong guessed"
# guessing_game()
  
#16
#def grade(marks):
#    if marks>90:
 #       return "A"
#    elif marks>80:
 #       return "B"
  #  elif marks>70:
   #     return "C"
 #   elif marks>60:
#        return "D"
 #   else:
 #       return "F"

#print(grade(70))
    

    
    
    
    
