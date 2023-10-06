"""Estimate the value of Pi with Monte Carlo simulation.
Author:  Finn Fujimura
Credits:  TBD
"""
import random
import doctest
import points_plot


def in_unit_circle(x: float, y: float) -> bool:
    """returns true if and only if (x,y) lies within the circle
    with origin (0,0) and radius 1.0

    >>> in_unit_circle(0.0,0.0)
    True
    >>> in_unit_circle(1.0,1.0)
    False

    >>> in_unit_circle(0.5,-0.5)
    True
    >>> in_unit_circle(-0.9,-0.5)
    False"""
    squared = x**2 + y**2
    if squared < 1.0:
        print(True)
    else:
        print(False)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
