import math

"""
Given an interger return True if the integer is prime and False if the interger is not prime.

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers
 
Example 1:

Input: num = 5
Output: True
Explanation: 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself.

Example 2:

Input: num = 10
Output: False
Explanation: 10 is not prime because there are several ways of writing 10 as a product, 1 × 10, 2 × 5, 5 × 2, 10 × 1.

O(n) time complexity
"""

def main(num:int):
    if num == 1:
        return False

    for n in range(2, int(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
        
    return True


if __name__ == "__main__":
    print(main(5))
    print(main(10))
    print(main(15))
    print(main(17))