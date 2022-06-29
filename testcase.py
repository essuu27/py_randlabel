# Simple test case program to show the usage of the randlabel function.
# It will output ten randomised label strings, each 16 charactyers long.
import randlabel

for _ in range(1, 10):
    print(randlabel.randlabel(16))
