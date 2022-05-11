#!/usr/bin/python3
def roman_to_int(roman_string):
roman_string = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and roman_string[s[i]] > roman_string[s[i - 1]]:
                int_val += roman_string[s[i]] - 2 * roman_string[s[i - 1]]
            else:
                int_val += roman_string[s[i]]
        return int_val
