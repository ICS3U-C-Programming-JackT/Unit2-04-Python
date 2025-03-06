#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: March 6th, 2025

# This program calculates the area and circumference of a circle

import math

PI = math.pi


def main():
    radius = float(input("Enter the radius of your circle in cm: "))
    area = PI * (radius**2)
    circumference = radius * 2 * PI
    print("The area of your circle is: " + str(area) + "cm^2")
    print("The circumference of your circle is: " + str(circumference) + "cm")


if __name__ == "__main__":
    main()
