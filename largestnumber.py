number = [10, 25, 5, 40, 15]

largest = number[0]

for num in number:
    if num > largest:
        largest = num
print("largest number:",largest)

"""number = [10, 25, 5, 40, 15]
smallest = number[0]

for num in number:
    if num < smallest:
        smallest = num
print("smallest number:", smallest)

#without using max()
numbers = [10, 25, 5, 40, 15]

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None):
        second_largest = num

print("Second largest number:", second_largest)

#with using max()
numbers = [10, 25, 5, 40, 15]
largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print("second largest number in a list:",second_largest)

number = [10, 25, 5, 40, 15]
smallest = min(number)
number.remove(smallest)
second_smallest = min(number)
print("second smallest number in a list:",second_smallest)

#Find the sum of all elements in a list without using sum()

number = [10, 25, 5, 40, 15]
total = 0
for num in number:
    total = total + num
print("sum of digits = ", total)

#Find the average of elements without using sum().

number = [10, 25, 5, 40, 15]
total = 0
for num in number:
    total = total + num
    average = total/len(number)
print("average value = ", average)

#Find the largest and smallest numbers in a single loop

number = [10, 25, 5, 40, 15]

largest = number[0]
smallest = number[0]
for num in number:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print("largest and smallest numbers:",largest,smallest)

#Count how many even and odd numbers are in a list.
numbers = [10, 15, 20, 25, 30, 35]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)

#Find the positive, negative and zero numbers in a list.
numbers = [10, -5, 0, 20, -8, 0, 15]

print("Positive numbers:")
for num in numbers:
    if num > 0:
        print(num)

print("Negative numbers:")
for num in numbers:
    if num < 0:
        print(num)

print("Zeros:")
for num in numbers:
    if num == 0:
        print(num)
#Find the length of a list without using len().

number = [10, 20, 30, 40, 50]
count = 0
for num in number:
    count += 1

print("Length of the list:", count)

#Find duplicate elements in a list.

numbers = [10, 20, 10, 30, 20, 40]

for num in set(numbers):
    if numbers.count(num) > 1:
        print(num)
#Remove duplicates from a list without using set().

a = [10, 20, 10, 30, 20, 40]
b = []
for i in a:
    if i not in b:
       b.append(i)
print(b)

#Find elements that occur more than once.

numbers = [10, 20, 10, 30, 20, 40]

for num in numbers:
    if numbers.count(num) > 1:
        print(num)

#Count the frequency of each element using dictionary
numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)

#Find the element with the highest frequency.

#Find all elements that are common between two lists.

a = [10, 20, 30, 40]
b = [20, 40, 50, 60]

for num in a:
    if num in b:
        print(num)

#Reverse a string without using slicing.

text = "Python"
result = ""
for char in text:
    result = char + result
print(result)

#Check whether a string is a palindrome.
madam

text = "madam"
reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
    
#Count the number of vowels and consonants in a string.
text = "Python"
vowels = 0
consonants = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    else:
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

#Remove duplicate characters from a string.

text = "hello"
result = ""

for char in text:
    if char not in result:
        result = result + char

print(result)

#Reverse each word in a sentence.

text = "I love Python"

for word in text.split():
    print(word[::-1], end=" ")"""