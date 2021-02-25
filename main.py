import pygame
import math
from matrix import multiplyMatrix
from cube_verticies import cube_verticies

white = (255, 255, 255)
black = (0, 0, 0)
grey = (150, 150, 150)
red = (255, 0, 0)

width = 600
height = 400

pygame.init()
pygame.font.init()
pygame.display.set_caption("3D Graphics Engine")
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
frames = 60

charter = pygame.font.SysFont("Charter", 15)

RotX = 0
RotY = 0
RotZ = 0
objPos = [width//2, height//2]
size = 500
points = cube_verticies()
distance = 5
MoveSpeed = 0.05
GrowSpeed = 0.03
RotSpeed = 0.02

def ConnectPoint(x, y, z):
    a = z[x]
    b = z[y]
    pygame.draw.line(display, black, (a[0], a[1]), (b[0], b[1]), 1)

run = True
while run:
    clock.tick(frames)
    fps = clock.get_fps()

    display.fill(white)

    fpsText = charter.render("FPS: " + str(round(fps, 1)), False, grey)
    rotXText = charter.render("X Rotation: " + str(round(RotX, 2)), False, grey)
    rotYText = charter.render("Y Rotation: " + str(round(RotY, 2)), False, grey)
    rotZText = charter.render("Z Rotation: " + str(round(RotZ, 2)), False, grey)
    sizeXText = charter.render("X Size: " + str(round(points[1][0][0], 2)), False, grey)
    sizeYText = charter.render("Y Size: " + str(round(points[2][1][0], 2)), False, grey)
    sizeZText = charter.render("Z Size: " + str(round(points[0][2][0], 2)), False, grey)
    distanceText = charter.render("Distance: " + str(round(distance, 2)), False, grey)
    display.blit(fpsText, (0, 0))
    display.blit(rotXText, (0, 12))
    display.blit(rotYText, (0, 24))
    display.blit(rotZText, (0, 36))
    display.blit(sizeXText, (0, 48))
    display.blit(sizeYText, (0, 60))
    display.blit(sizeZText, (0, 72))
    display.blit(distanceText, (0, 84))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        RotY -= RotSpeed
    if keys[pygame.K_d]:
        RotY += RotSpeed
    if keys[pygame.K_w]:
        RotX -= RotSpeed
    if keys[pygame.K_s]:
        RotX += RotSpeed
    if keys[pygame.K_q]:
        RotZ -= RotSpeed
    if keys[pygame.K_e]:
        RotZ += RotSpeed
    if keys[pygame.K_z]:
        distance -= MoveSpeed
    if keys[pygame.K_x]:
    distance += MoveSpeed
    if keys[pygame.K_f]:
        points[0][2][0] += GrowSpeed
        points[1][2][0] += GrowSpeed
        points[2][2][0] += GrowSpeed
        points[3][2][0] += GrowSpeed
    if keys[pygame.K_r]:
        points[0][2][0] -= GrowSpeed
        points[1][2][0] -= GrowSpeed
        points[2][2][0] -= GrowSpeed
        points[3][2][0] -= GrowSpeed
    if keys[pygame.K_g]:
        points[2][1][0] += GrowSpeed
        points[3][1][0] += GrowSpeed
        points[6][1][0] += GrowSpeed
        points[7][1][0] += GrowSpeed
    if keys[pygame.K_t]:
        points[2][1][0] -= GrowSpeed
        points[3][1][0] -= GrowSpeed
        points[6][1][0] -= GrowSpeed
        points[7][1][0] -= GrowSpeed
    if keys[pygame.K_h]:
        points[1][0][0] += GrowSpeed
        points[2][0][0] += GrowSpeed
        points[5][0][0] += GrowSpeed
        points[6][0][0] += GrowSpeed
    if keys[pygame.K_y]:
        points[1][0][0] -= GrowSpeed
        points[2][0][0] -= GrowSpeed
        points[5][0][0] -= GrowSpeed
        points[6][0][0] -= GrowSpeed
    if keys[pygame.K_c]:
        points[0][2][0] = 1
        points[1][2][0] = 1
        points[2][2][0] = 1
        points[3][2][0] = 1
        points[2][1][0] = 1
        points[3][1][0] = 1
        points[6][1][0] = 1
        points[7][1][0] = 1
        points[1][0][0] = 1
        points[2][0][0] = 1
        points[5][0][0] = 1
        points[6][0][0] = 1
        distance = 5
        RotX = 0
        RotY = 0
        RotZ = 0

    index = 0
    projectedPoints = [p for p in range(len(points))]

    rotationX = [[1, 0, 0], [0, math.cos(RotX), -math.sin(RotX)], [0, math.sin(RotX), math.cos(RotX)]]
    rotationY = [[math.cos(RotY), 0, -math.sin(RotY)], [0, 1, 0], [math.sin(RotY), 0, math.cos(RotY)]]
    rotationZ = [[math.cos(RotZ), -math.sin(RotZ), 0], [math.sin(RotZ), math.cos(RotZ), 0], [0, 0, 1]]

    for point in points:
        rotated = multiplyMatrix(rotationX, point)
        rotated = multiplyMatrix(rotationY, rotated)
        rotated = multiplyMatrix(rotationZ, rotated)

        z = 1/(distance - rotated[2][0])
        projection = [[z, 0, 0], [0, z, 0]]

        projected = multiplyMatrix(projection, rotated)

        x = int(projected[0][0] * size) + objPos[0]
        y = int(projected[1][0] * size) + objPos[1]

        projectedPoints[index] = [x, y]
        pygame.draw.circle(display, red, (x, y), 1)
        index += 1

    for m in range(4):
        ConnectPoint(m, (m+1)%4, projectedPoints)
        ConnectPoint(m + 4, (m+1)%4 + 4, projectedPoints)
        ConnectPoint(m, m+4, projectedPoints)

    pygame.display.update()

pygame.quit()
