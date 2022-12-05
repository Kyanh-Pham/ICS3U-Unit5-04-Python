#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Nov 2022
# The program finds the volume of a cylinder

import math


def calculate_volume(height: float, radius: float, add: bool) -> float:
    # This function calculates volume
    if height <= 0:
        volume = -1
        return volume
    elif radius <= 0:
        volume = -1
        return volume
    else:
        volume = math.pi * radius**2 * height
        return volume


def main():
    # this function gets the volume

    # Input
    height_str = input("Enter the height of the cylinder(mm): ")
    radius_str = input("Enter the radius of the cylinder(mm): ")

    try:
        height = float(height_str)
        radius = float(radius_str)
        # call functions
        volume = calculate_volume(height, radius)
        if volume == -1:
            print("Invalid Input")
        else:
            print(
                "The volume of this cylinder with the radius of {0} mm and height {1} mm is {2} mm³.".format(
                    radius, height, volume
                )
            )
    except ValueError:
        print("Invalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
