[![Build Status](https://travis-ci.com/kornkritpawit/unittesting-kornkritpawit.svg?branch=master)](https://travis-ci.com/kornkritpawit/unittesting-kornkritpawit)

## Unit Testing Assignment

by Kritpawit Soongswang.


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| many items same and unsame types, unorders   | list with unsame many items|
| very large list        | list with unsame items|
| non list                |  raised TypeError   |


## Test Cases for Fraction
| Test case (Constructor)             |  Expected Result    |
|------------------------|---------------------|
| positive int nominator and positive int denominator | nominator = int, denominator = int|
| negative int nominator and positive int denominator | nominator = -int, denominator = int|
| positive int nominator and negative int denominator | nominator = -int , denominator = int|
| zero nominator and positive or negative int denominator | nominator = 0 , denominator = 1 |
| zero nominato and zero denominator | nominator = 0, denominator = 0 |
| positive int nominator and zero denominator | nominator = 1, denominator = 0|
| negative int nominator and zero denominator | nominator = -1,  denominator = 0|
| non int as numerator or denominator | TypeError|

| Test case (Based text)             |  Expected Result    |
|------------------------|---------------------|
| numerator > 0, denominator > 0 | int/int |
| numerator < 0, denominator < 0 | int/int |
| numerator < 0, denominator > 0 | -int/int |
| numerator > 0, denominator < 0 | -int/int|
| numerator > 0, denominator = 1 | int |
| numerator < 0, denominator = 1 | -int |
| numerator > 0, denominator = 0 | 1/0 |
| numerator < 0, denominator = 0 | -1/0 |
| numerator = 0, denominator = 0 | 0/0 |
| numerator = 0, denominator != 0 | 0 |

| Test case (Addition)             |  Expected Result    |
|------------------------|---------------------|
| positive fraction + positive fraction | positive fraction |
| positive fraction + negative fraction | positive or negative fraction |
| negative fraction + negative fraction | negative fraction |
| 1/0 + 1/0 | 0/0 or infinity|
| 0/0 + 0/0 | 0/0 or nan |
| 1/0 + -1/0 | 0/0 or nan |
| 1/0 + 0/0 | 0/0 or nan |

| Test case (Subtraction)             |  Expected Result    |
|------------------------|---------------------|
| positive fraction - positive fraction | positive or negative fraction |
| positive fraction - negative fraction | positive fraction |
| negative fraction +-negative fraction | positive or negative fraction |
| 1/0 - 1/0 | 0/0 or nan|
| 0/0 - 0/0 | 0/0 or nan |
| 1/0 - (-1/0)| 0/0 or infinity |
| 1/0 - 0/0 | 0/0 or nan |

| Test case (Multiplication)             |  Expected Result    |
|------------------------|---------------------|
| positive fraction * positive fraction | positive fraction |
| positive fraction * negative fraction | negative fraction |
| negative fraction * negative fraction | positive fraction |
| -1/0 * -1/0 | 1/0 or infinity |
| 1/0 * 1/0 | 1/0 or infinity |
| 0/0 * 0/0 | 0/0 or nan |

| Test case (negation)             |  Expected Result    |
|------------------------|---------------------|
| positive fraction | negative fraction |
| negative fraction | positive fraction |
| 1/0 | -1/0 |
| -1/0 | 1/0 |
| 0/0 | 0/0 |


















