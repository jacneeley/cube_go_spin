# cube_go_spin
![gif of my ascii cube spinning](./spin.gif)

## Math
The trick for this one is the applying the math.
![basic rotation matrix](./basic_3D_rotation.png)
![basic rotation matrix distributed across "i, j, k"](./distributed_rotation_xyz_equation.png)


`def calculateX(i, j, k):
    return j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) * cos(C) + j * cos(A) * sin(C) + k * sin(A) * sin(C) + i * cos(B) * cos(C)`

`def calculateY(i, j, k):
    return j * cos(A) * cos(C) + k * sin(A) * cos(C) - j * sin(A) * sin(B) * sin(C) + k * cos(A) * sin(B) * sin(C) - i * cos(B) * sin(C)`
    
`def calculateZ(i, j, k):
    return k * cos(A) * cos(B) - j * sin(A) * cos(B) + i * sin(B)`