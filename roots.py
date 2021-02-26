#!/usr/bin/env python
#
# Author: Oscar Benjamin
# Date: Feb 2021
# Description:
#   Command line script to find integer roots of polynomials with
#   integer coefficients.


#-------------------------------------------------------------------#
#                                                                   #
#                   Command-line interface                          #
#                                                                   #
#-------------------------------------------------------------------#

PROGRAM_EXPLANATION = """
Usage:
$ python roots.py COEFF1 COEFF2 ...

Find integer roots of a polynomial with integer coefficients.

Example:

Find the roots of x^4 - 3x^3 - 75x^2 + 475x - 750.

$ python roots.py 1 -3 -75 475 -750
-10
3
5
"""


def main(*arguments):
    """Main entry point for the program"""
    if not arguments:
        print(PROGRAM_EXPLANATION)
        return

    poly = parse_coefficients(arguments)
    roots = integer_roots(poly)
    print_roots(roots)


def parse_coefficients(arguments):
    """Convert string arguments to integer

    >>> parse_coefficients(["2", "3"])
    [2, 3]
    """
    return [int(arg) for arg in arguments]


def print_roots(roots):
    """Print the roots one per line if there are any

    >>> print_roots([2, 3])
    2
    3
    """
    if roots:
        roots_str = [str(r) for r in roots]
        print('\n'.join(roots_str))


#-------------------------------------------------------------------#
#                                                                   #
#                      Polynomial functions                         #
#                                                                   #
#-------------------------------------------------------------------#


class BadPolynomialError(Exception):
    """Raised by polynomial routines when the polynomial is invalid.

    A valid polynomial is a list of coefficients like [1, 2, 1]

    The first (leading) coefficient must *not* be zero in a valid polynomial.
    """
    pass


def integer_roots(poly):
    """To find the roots of the polynomial"""
    last_value = poly[-1]
    if len(poly) <= 1:
        possible_root = 0 
        return possible_root
    modulus_range = range(-last_value,last_value + 1)
    for possible_root in modulus_range:
        if is_root(poly,possible_root) == True:

            return possible_root

def evaluate_polynomial(poly, xval):
    """Caluclates the value of polynomial poly at x value xval"""
    
    last_value = poly[0]

    length = len(poly)
    if length == 0:
        last_value = 0
    elif length == 1:
        last_value == poly[0]
    for number in range(1,length):
        last_value = last_value * xval + poly[number]
    return last_value

def is_root(poly, xval):
    """checks if value xval is a root of the polynomial poly""" 
    y = evaluate_polynomial(poly,xval)
    if len(poly) == 0:
        return True
    if len(poly) == 1:
        return False
    if  y == 0:
        return True
    else:
        return False


#-------------------------------------------------------------------#
#                                                                   #
#                           Unit tests                              #
#                                                                   #
#-------------------------------------------------------------------#

#
# Run these tests with pytest:
#
#    $ pytest roots.py
#

def test_evaluate_polynomial():
    assert evaluate_polynomial([], 1) == 0
    assert evaluate_polynomial([1], 2) == 1
    assert evaluate_polynomial([1, 2], 3) == 5
    assert evaluate_polynomial([1, 2, 1], 4) == 25

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: evaluate_polynomial([0], 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial({}, 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial([[1]], 1))


def test_is_root():
    assert is_root([], 1) is True
    assert is_root([1], 1) is False
    assert is_root([1, 1], 1) is False
    assert is_root([1, 1], -1) is True
    assert is_root([1, -1], 1) is True
    assert is_root([1, -1], -1) is False
    assert is_root([1, -5, 6], 2) is True
    assert is_root([1, -5, 6], 3) is True
    assert is_root([1, -5, 6], 4) is False

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: is_root([0], 1))
    raises(BadPolynomialError, lambda: is_root({}, 1))
    raises(BadPolynomialError, lambda: is_root([[1]], 1))


def test_integer_roots():
    # In the case of the zero polynomial every value is a root but we return
    # the empty list because we can't list every possible value!
    assert integer_roots([]) == []
    assert integer_roots([1]) == []
    assert integer_roots([1, 1]) == [-1]
    assert integer_roots([2, 1]) == []
    assert integer_roots([1, -5, 6]) == [2, 3]
    assert integer_roots([1, 5, 6]) == [-3, -2]
    assert integer_roots([1, 2, 1]) == [-1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -3, -75, 475, -750]) == [-10, 3, 5]

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: integer_roots([0]))
    raises(BadPolynomialError, lambda: integer_roots({}))
    raises(BadPolynomialError, lambda: integer_roots([[1]]))


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    main(*arguments)
