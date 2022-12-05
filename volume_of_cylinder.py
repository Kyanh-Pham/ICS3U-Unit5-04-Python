#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Nov 2022
# The program finds the volume of a cylinder

import math


def calculate_volume(height: int, radius: int) -> float:
    # This function calculates volume
    if height <= 0 or radius <= 0:
        volume = -1
        return volume
    else:
        volume = math.pi * radius ** 2 * height
        return float(volume)


def main():
    # This function gets the volume

    # Input
    height_from_user = input("Enter the height of the cylinder(mm): ")
    radius_from_user = input("Enter the radius of the cylinder(mm): ")

    try:
        height_from_user = float(height_from_user)
        radius_from_user = float(radius_from_user)
        # call functions
        final_volume = calculate_volume(height_from_user, radius_from_user)
        if final_volume == -1:
            print("Invalid Input")
        else:
            print(
                "The volume of this cylinder with the radius of {0} mm and height {1} mm is {2} mm³.".format(
                    radius_from_user, height_from_user, final_volume
                )
            )
    except ValueError:
        print("Invalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
