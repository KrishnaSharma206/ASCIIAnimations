'''
Program to make a Donut using ASCII characters.
x = (R2 + R1 * cosθ) * (cosB * cosϕ + sinA * sinB * sinϕ) - (R1 * cosA * sinB * sinθ)
y = (R2 + R1 * cosθ) * (cosϕ * sinB - cosB * sinA * sinϕ) + (R1 * cosA * cosB * sinθ)
z = cosA * (R2 + R1 * cosθ) * sinϕ + (R1 * sinA * sinθ)
x' = K1 * x / (K2 + z)
y' = K2 * y / (K2 + z)
L = cosϕ * cosθ * sinB - cosA * cosθ * sinϕ - sinA * sinθ + cosB * (cosA * sinθ - cosθ * sinA * sinϕ)
K1 = screen_width * K2 * 3 / (8 * (R1 + R2))
'''
from math import *
import numpy as np
from os import system
import time
R1, R2 = 1, 3
K2 = 7
screen_width, screen_height = 40, 40
K1 = screen_width * K2 * 3 / (8 * (R1 + R2))
theta, phi = 0.02, 0.07
output = np.full([screen_width, screen_height], " ")
z_buffer = np.zeros([screen_width, screen_height])

def generate_frame(A, B):
    sA = sin(A)
    cA = cos(A)
    sB = sin(B)
    cB = cos(B)
    for i in np.arange(0, 2 * pi, theta):
        sT = sin(i)
        cT = cos(i)
        for j in np.arange(0, 2 * pi, phi):
            sP = sin(j)
            cP = cos(j)
            x = (R2 + R1 * cT) * (cB * cP + sA * sB * sP) - (R1 * cA * sB * sT)
            y = (R2 + R1 * cT) * (cP * sB - cB * sA * sP) + (R1 * cA * cB * sT)
            z = cA * (R2 + R1 * cT) * sP + (R1 * sA * sT) + K2
            ooz = 1.0 / z
            L = cP * cT * sB - cA * cT * sP - sA * sT + cB * (cA * sT - cT * sA * sP)
            xp = (int)(screen_width / 2 + (float)(K1 * x) * ooz)
            yp = (int)(screen_height / 2 - (float)(K1 * y) * ooz)
            if 0 <= xp < screen_width and 0 <= yp < screen_height:
                if ooz > z_buffer[xp][yp]:
                    z_buffer[xp][yp] = ooz
                    L = (int)(L * 8)
                    L_index = max(0, min(11, L))
                    output[xp][yp] = ".,-~:;=!*#$@"[L_index]
    print("\x1b[H")
    for num in output:
        print("".join(num))
    output.fill(" ")
    z_buffer.fill(0)
system("clear")
i = 0
j = 0
while True:
    generate_frame(i, j)
    j = j + 0.05
    i = i + 0.05
    time.sleep(0.03)