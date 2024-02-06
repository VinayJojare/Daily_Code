python_problems = [
    {
        'title': 'Problem 1 = What will be the output of this code:',
        'description': '''
    def power(base, exponent):
        if exponent == 0:
            return 1
        else:
            return base * power(base, exponent - 1)

    print(power(2, 3))
        ''',
    },
    {
        'title': 'Problem 2 = What will be the output of this code:',
        'description': '''
    def is_palindrome(string):
        if len(string) <= 1:
            return True
        else:
            return string[0] == string[-1] and is_palindrome(string[1:-1])

    print(is_palindrome("radar"))
        ''',
    },
    {
        'title': 'Problem 3 = What will be the output of this code:',
        'description': '''
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    print(gcd(24, 36))
        ''',
    },
    {
        'title': 'Problem 4 = What will be the output of this code:',
        'description': '''
    def sum_of_digits(n):
        if n < 10:
            return n
        else:
            return n % 10 + sum_of_digits(n // 10)

    print(sum_of_digits(123))
        ''',
    },
    {
        'title': 'Problem 5 = What will be the output of this code:',
        'description': '''
    def binary_search(arr, target, low, high):
        if low > high:
            return -1
        else:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return binary_search(arr, target, mid + 1, high)
            else:
                return binary_search(arr, target, low, mid - 1)

    arr = [1, 3, 5, 7, 9]
    print(binary_search(arr, 5, 0, len(arr) - 1))
        ''',
    },
    {
        'title': 'Problem 6 = What will be the output of this code:',
        'description': '''
    def is_prime(n, divisor=2):
        if n <= 2:
            return True if n == 2 else False
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True
        return is_prime(n, divisor + 1)

    print(is_prime(13))
        ''',
    },
    {
        'title': 'Problem 7 = What will be the output of this code:',
        'description': '''
    def reverse_string(string):
        if len(string) == 0:
            return string
        else:
            return reverse_string(string[1:]) + string[0]

    print(reverse_string("hello"))
        ''',
    },
    {
        'title': 'Problem 8 = What will be the output of this code:',
        'description': '''
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    print(fibonacci(6))
        ''',
    },
    {
        'title': 'Problem 9 = What will be the output of this code:',
        'description': '''
    def binary_to_decimal(binary):
        if binary == 0:
            return 0
        else:
            return binary % 10 + 2 * binary_to_decimal(binary // 10)

    print(binary_to_decimal(1010))
        ''',
    },
    {
        'title': 'Problem 10 = What will be the output of this code:',
        'description': '''
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted array:", arr)
        ''',
    },
    {
        'title': 'Problem 11 = What will be the output of this code:',
        'description': '''
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(5))
        ''',
    },
    {
        'title': 'Problem 12 = What will be the output of this code:',
        'description': '''
    def count_vowels(s):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)

    print(count_vowels('hello'))
        ''',
    },
    {
        'title': 'Problem 13 = What will be the output of this code:',
        'description': '''
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])
            return merge(left_half, right_half)

    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    arr = [12, 11, 13, 5, 6, 7]
    print(merge_sort(arr))
        ''',
    },
    {
        'title': 'Problem 14 = What will be the output of this code:',
        'description': '''
    def decimal_to_binary(n):
        if n == 0:
            return ''
        else:
            return decimal_to_binary(n // 2) + str(n % 2)

    print(decimal_to_binary(10))
        ''',
    },
    {
        'title': 'Problem 15 = What will be the output of this code:',
        'description': '''
    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    arr = [4, 6, 8, 10, 12]
    print(linear_search(arr, 8))
        ''',
    },
    {
        'title': 'Problem 16 = What will be the output of this code:',
        'description': '''
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    print("Sorted array:", arr)
        ''',
    },
    {
        'title': 'Problem 17 = What will be the output of this code:',
        'description': '''
    def check_palindrome(s):
        return s == s[::-1]

    print(check_palindrome('madam'))
        ''',
    },
    {
        'title': 'Problem 18 = What will be the output of this code:',
        'description': '''
    def binary_to_decimal(binary):
        decimal = 0
        power = 0
        while binary != 0:
            decimal += (binary % 10) * (2 ** power)
            binary //= 10
            power += 1
        return decimal

    print(binary_to_decimal(1010))
        ''',
    },
    {
        'title': 'Problem 19 = What will be the output of this code:',
        'description': '''
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    print("Sorted array:", arr)
        ''',
    },
    {
        'title': 'Problem 20 = What will be the output of this code:',
        'description': '''
    def exponent(base, exp):
        result = 1
        for _ in range(exp):
            result *= base
        return result

    print(exponent(2, 3))
        ''',
    },





    {
        'title': 'Problem 21',
        'description': 'Write a program to find the sum of all even numbers in a list and check if the output is the sum of even numbers.',
    },
    {
        'title': 'Problem 22',
        'description': 'Write a program to check if a number is a perfect square and check if the output is "Perfect Square" or "Not Perfect Square".',
    },
    {
        'title': 'Problem 23',
        'description': 'Write a program to find the ASCII value of a character and check if the output is the ASCII value.',
    },
    {
        'title': 'Problem 24',
        'description': 'Write a program to find the LCM (Least Common Multiple) of two numbers and check if the output is the LCM.',
    },
    {
        'title': 'Problem 25',
        'description': 'Write a program to find the median of three numbers and check if the output is the median.',
    },
    {
        'title': 'Problem 26',
        'description': 'Write a program to check if a string is an anagram of another string and check if the output is "Anagram" or "Not Anagram".',
    },
    {
        'title': 'Problem 27',
        'description': 'Write a program to find the factorial of a number using recursion and check if the output is the factorial of the number.',
    },
    {
        'title': 'Problem 28',
        'description': 'Write a program to check if a string is a pangram and check if the output is "Pangram" or "Not Pangram".',
    },
    {
        'title': 'Problem 29',
        'description': 'Write a program to find the largest prime factor of a number and check if the output is the largest prime factor.',
    },
    {
        'title': 'Problem 30',
        'description': 'Write a program to find the area of a rectangle and check if the output is the area of the rectangle.',
    },
    {
        'title': 'Problem 31',
        'description': 'Write a program to check if a year is a leap year and check if the output is "Leap Year" or "Not Leap Year".',
    },
    {
        'title': 'Problem 32',
        'description': 'Write a program to find the square root of a number and check if the output is the square root.',
    },
    {
        'title': 'Problem 33',
        'description': 'Write a program to sort a list of dictionaries by a specific key and check if the output is the sorted list.',
    },
    {
        'title': 'Problem 34',
        'description': 'Write a program to check if a number is a strong number and check if the output is "Strong Number" or "Not Strong Number".',
    },
    {
        'title': 'Problem 35',
        'description': 'Write a program to implement a simple calculator with addition, subtraction, multiplication, and division operations and check if the output is correct for given inputs.',
    },
    {
        'title': 'Problem 36',
        'description': 'Write a program to find the sum of digits of a number until it becomes a single-digit number and check if the output is the single-digit sum.',
    },
    {
        'title': 'Problem 37',
        'description': 'Write a program to find the roots of a quadratic equation and check if the output is the roots.',
    },
    {
        'title': 'Problem 38',
        'description': 'Write a program to find the length of the longest substring without repeating characters and check if the output is the length of the substring.',
    },
    {
        'title': 'Problem 39',
        'description': 'Write a program to check if a number is a happy number and check if the output is "Happy Number" or "Not Happy Number".',
    },
    {
        'title': 'Problem 40',
        'description': 'Write a program to find the number of trailing zeroes in the factorial of a number and check if the output is the number of trailing zeroes.',
    },
    {
        'title': 'Problem 41',
        'description': 'Write a program to implement the Sieve of Eratosthenes algorithm for finding prime numbers up to a given limit and check if the output is the list of prime numbers.',
    },
]
