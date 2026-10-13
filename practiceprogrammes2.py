"""#1. Reverse a string
Reverse text without relying on a built-in reverse operation.

word = "arshiya"
reverse =""

for char in word:
    reverse = char + reverse
print("reverse string:", reverse)

2. Check a palindrome
Compare a word or number with its reverse.

word = input("enter string:",)
reverse = ""
for char in word:
    reverse = char + reverse
if word == reverse:
   print("palindrome")
else:
   print("not palindrome")

   3. Count vowels and consonants
Scan text and classify alphabetic characters.

word = input("enter a string: ")
vowels = 0
consonents = 0
for char in word:
   if char.isalpha():
       if char.lower() in "aeiou":
           vowels = vowels + 1
       else:
           consonents = consonents + 1
print("vowels:", vowels)
print("consonents:", consonents)

4. Count character frequency
Use a dictionary to count each character

word = input("enter a string: ")
frequency = {}
for char in word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

5. Find factorial
Implement an iterative solution and understand recursion


n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)

6. Generate Fibonacci numbers
Produce a sequence using previous values.

n = int(input("Enter a number:"))
a = 0
b = 1
for i in range(n):
    print(a,end="")
    c = a + b
    a = b
    b = c

    #prime numbers(number which diving by 1 and itself)
    7. Check prime number
Use divisibility and the square-root optimization.

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

    8. Print primes in a range
Reuse a prime-checking function
    
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n, end=" ")

        11. Find the largest and second largest
Handle duplicate values and missing answers.

number = [10,20,30,40,16]

largest = number[0]
second_largest = None

for num in number:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None):
         second_largest = num
print("Second largest number is:", second_largest)


12. Find the missing number
Use arithmetic sums or XOR.


numbers = [1, 2, 3, 5, 6]

n = 6
total = n * (n + 1) // 2
missing = total - sum(numbers)

print("Missing number:", missing)

14. Find common elements
Use sets while considering ordering and duplicates.

a = [1, 2, 7, 4, 5, 6]
b = [2, 3, 5, 6, 7, 8]

common = set(a) & set(b)

print("Common elements in both set:", common)

16. Sort without sort()
Implement bubble sort, then analyze its complexity.


numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

15. Merge two sorted lists
Use two pointers.


numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

17. Count words in a sentence
Normalize and tokenize text.

text = input("enter string: ")
word = text.split()
print("word count:",len(word))

18. Check anagrams
Compare character frequencies.


a = input("Enter first word: ").lower()
b = input("Enter second word: ").lower()

if sorted(a) == sorted(b):
    print("Anagrams")
else:
    print("Not anagrams")"""
