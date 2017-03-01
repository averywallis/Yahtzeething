"""
Yahtzeething.py
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset
from ggame import ImageAsset, PolygonAsset, Frame, Sound, SoundAsset, TextAsset
import time
import math
import random
import sys

# colors
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
skin =Color(0xFCD15B, 1.0)
wall=Color(0xE8E8E8, 1.0)
orange=Color(0xFFa500,1.0)
platc=Color(0xB9BDBB,1.0)
gooy=Color(0xCDF238,1.0)
white=Color(0xFFFFFF,1.0)
darkblue=Color(0x052099,1.0)

# lines
thinline= LineStyle(1, black)
thickline= LineStyle(5, black)
thickishline= LineStyle(2.5, black)
noline= LineStyle(0, black)
portalline= LineStyle(1, blue)
portalline2= LineStyle(1, orange)

dielist=[]
#dielist=[1,2,3,4,5]
dieremove=[]
for x in range(0,5):
    dielist.append(random.randrange(1,7,1))
dielist.sort()
print("Dies")
print(dielist)
if dielist == list([1,2,3,4,5]) or list([2,3,4,5,6]):
    print("You win!")
remove = list(input("Dice removed (no spaces)"))
l = len(remove)
print(l)
print(remove)


