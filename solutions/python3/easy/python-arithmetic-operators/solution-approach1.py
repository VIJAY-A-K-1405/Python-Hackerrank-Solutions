# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
# Problem     Arithmetic Operators
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-18, 11:14 a.m.
# Technique   basic-arithmetic-operations
# Time        O(1)
# Space       O(1)
# Insight     The implementation performs standard arithmetic operations on two input integers and prints the results sequentially as required by the problem statement.
# Interview   Before: "How would you handle arithmetic operations in Python?" After: "I would use the standard +, -, and * operators, which operate in O(1) time and O(1) space, ensuring the output matches the required sum, difference, and product format."
# Pitfalls    (1) Failing to convert input strings to integers using int() before performing arithmetic operations.  (2) Printing the difference as (second - first) instead of the required (first - second) order.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    c = a+ b
    d = a - b
    e = a*b
    
print(c)
print(d)
print(e)
