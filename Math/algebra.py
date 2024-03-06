#!/usr/bin/env python3
import math
"""
The following python scripts has common Math functions that are used for various reasons
"""




def quadratic(a, b, c):
    """
    This function returns the roots of a quadratic equation
    """
    d = b**2 - 4*a*c
    if d < 0:
        return "No real roots"
    elif d == 0:
        return -b/(2*a)
    else:
        return (-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a)


