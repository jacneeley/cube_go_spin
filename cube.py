import os
import time
from math import *

run = 1

A = 0
B = 0
C = 0

cubeWidth = 20
xOffSet = 0        
width, height = 160, 44

zBuffer = [0] * (144*60)
buffer = [''] * (144*60)
backgroundASCIICode = ' '
distanceFromCam = 200
xOffSet = 0
k1 = 40

incrementSpeed = 0.6

ooz = 0
x_pos, y_pos = 0, 0
idx = 0

def calculateX(i, j, k):
    return j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) * cos(C) + j * cos(A) * sin(C) + k * sin(A) * sin(C) + i * cos(B) * cos(C)

def calculateY(i, j, k):
    return j * cos(A) * cos(C) + k * sin(A) * cos(C) - j * sin(A) * sin(B) * sin(C) + k * cos(A) * sin(B) * sin(C) - i * cos(B) * sin(C)

def calculateZ(i, j, k):
    return k * cos(A) * cos(B) - j * sin(A) * cos(B) + i * sin(B)

def calculateSurface(cubeX, cubeY, cubeZ, chars):
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam
    
    ooz = 1/z
    
    x_pos = int(width/2 + xOffSet + k1 * ooz * x * 2)
    y_pos = int(height/2 + k1 * ooz * y)
    
    # index
    idx = x_pos + y_pos * width
    if idx >= 0 and idx < width * height:
        if ooz > zBuffer[idx]:
            zBuffer[idx] = max(1, int(ooz))
            buffer[idx] = chars
    

if __name__ == "__main__":
    while run != 0:
        buffer = [backgroundASCIICode] * (width * height)
        zBuffer = bytearray([0] * (width * height * 4))
        print("\x1b[H")
        
        #cube
        for cube_x in range(int(-cubeWidth), int(cubeWidth), max(1,int(incrementSpeed))):
            for cube_y in range(int(-cubeWidth), int(cubeWidth), max(1,int(incrementSpeed))):
                calculateSurface(cube_x, cube_y, -cubeWidth, '@')
                calculateSurface(cubeWidth, cube_y, cube_x, '$')
                calculateSurface(-cubeWidth, cube_y, -cube_x, '~')
                calculateSurface(-cube_x, cube_y, cubeWidth, '#')
                calculateSurface(cube_x, -cubeWidth, -cube_y, ';')
                calculateSurface(cube_x, cubeWidth, cube_y, '+')

        print("\x1b[H")
        for k in range(width * height):
            print(buffer[k] if k % width else '\n', end='')
            
        A += .05
        B += .05
        C += .01
        
        time.sleep(.016)
        
        
        
        