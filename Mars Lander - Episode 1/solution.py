import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

maxpower = 4
minpower = 0
mars_g = 3.711
min_v_speed = -40
delta_power = 1

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Check currecnt power
    delta_speed = mars_g / 4 * (power - maxpower)
    next_speed = v_speed + delta_speed
    
    if next_speed < min_v_speed and power < maxpower:
        power = power + delta_power
    elif power > minpower:
        #check for less power
        delta_speed = mars_g / 4 * (power - 1 - maxpower)
        next_speed = v_speed + delta_speed
        if next_speed > min_v_speed:
            power = power - delta_power

    print( "0 {}".format( int(power) ) )

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    # print("0 3")
