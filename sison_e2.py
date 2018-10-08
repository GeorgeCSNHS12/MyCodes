# filename      : sison_e2.py
# author        : George William Sison
# description   : This is a python program that classifies a tropical cyclone
#                 with its sustained winds.

import sys

windIntensity = float(sys.argv[1])

if windIntensity >= 220 :
    print("Super Typhoon")
elif windIntensity >= 118 :
    print("Typhoon")
elif windIntensity >= 89 :
    print("Severe Tropical Storm")
elif windIntensity >= 62 : 
    print("Tropical Storm")
elif windIntensity <= 61 and windIntensity > 0 :
    print("Tropical Depression")
else :
    print("Out of Range")
