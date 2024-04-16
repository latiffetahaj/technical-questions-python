'''
    17. Letter Combinations of a Phone Number
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below.

    2 -> abc
    3 -> def
    4 -> ghi
    5 -> jkl
    6 -> mno
    7 -> pqrs
    8 -> tuv
    9 -> wxyz


    Note that 1 and 0 don't map to any letters.

    Constraints:
        0 <= digits.length <= 4
        digits[i] is a digit in the range ['2', '9'].


    #LeetCode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

    Time Complexity:
    Space Complexity:
'''

def letter_combinations(digits):
    result = []

    # Map digits to letters
    to_letters = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}


    generate_letter_combinations(digits, [], result, 0, to_letters)

    return result



def generate_letter_combinations(digits, current, result, index, to_letters):
    if len(current) == len(digits):
        result.append(''.join(current.copy()))
        return

    if index >= len(digits):
        return

    current_characters = to_letters[digits[index]]

    for c in current_characters:
        current.append(c)

        generate_letter_combinations(digits, current, result, index + 1, to_letters)

        current.pop()

    return