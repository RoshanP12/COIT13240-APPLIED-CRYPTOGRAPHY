'''
Helper functions for classical ciphers on English text

**TODO**
 - add error checking
'''

global charset

charset = "lowercase"


def char_to_num(c):
    '''
    Convert a single character into a number

    Converts a -> 0, b -> 1, c -> 2, ... or 
    if uppercase A -> 0, B -> 1, C -> 2, ...
    '''

    if charset == "lowercase":
        return ord(c) - 97
    else:
        return ord(c) - 65


def num_to_char(n):
    '''
    Convert a number into a single character

    See char_to_num(c) - this is the opposite

    '''

    if charset == "lowercase":
        return chr(n + 97)
    else:
        return chr(n + 65)


def text_to_nums(text):
    '''
    Convert a string into a list of numbers

    :Example:
     - input: str = "abc"
     - output: list = [0, 1, 2]
    '''

    return [char_to_num(c) for c in text]


def nums_to_text(nums):
    '''
    Convert a list of numbers into a string

    See text_to_nums(text) - this is the opposite
    '''

    return ''.join([num_to_char(n) for n in nums])
