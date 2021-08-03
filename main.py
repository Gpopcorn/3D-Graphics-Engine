# public imports
import pygame
import easygui
from math import sin, cos, sqrt
from operator import itemgetter
from copy import deepcopy

# local imports
from colors import *
from objects import *
from matrix import *
from classes import *
from load_obj import *
from functions import *


# ---- PRE LOOP ----

# pre-register variables
prev_mouse = (0, 0)
right_click = False
left_click = False

# pygame window sizes
window_width = 1000
window_height = 700

pygame.init() # initializes pygame

# pygame window setup
pygame.display.set_caption("3D Graphics Engine") # title for the pygame window
display = pygame.display.set_mode((window_width, window_height)) # creates the pygame window and the size of it

# pygame clock setup
clock = pygame.time.Clock() # sets the clock variable

# fonts
freesansbold = pygame.font.Font('freesansbold.ttf', 20)
freesansbold_small = pygame.font.Font('freesansbold.ttf', 10)


# -- BUTTONS --
# buttons rect
toggle_verticies_button_rect = pygame.Rect((928, 630), (60, 60))
toggle_edges_button_rect = pygame.Rect((928, 560), (60, 60))
toggle_faces_button_rect = pygame.Rect((928, 490), (60, 60))
toggle_light_button_rect = pygame.Rect((928, 420), (60, 60))

toggle_cube_button_rect = pygame.Rect((928, 30), (60, 60))
toggle_pyramid_button_rect = pygame.Rect((928, 100), (60, 60))
toggle_sphere_button_rect = pygame.Rect((928, 170), (60, 60))
toggle_custom_shape_button_rect = pygame.Rect((928, 240), (60, 60))


# buttons text
settings_text = freesansbold.render('Settings', True, BLACK)
toggle_verticies_button_text = freesansbold_small.render('Render Verticies', True, BLACK)
toggle_edges_button_text = freesansbold_small.render('Render Edges', True, BLACK)
toggle_faces_button_text = freesansbold_small.render('Render Faces', True, BLACK)
toggle_light_button_text = freesansbold_small.render('Lighting', True, BLACK)

shapes_text = freesansbold.render('Shapes', True, BLACK)
toggle_cube_button_text = freesansbold_small.render('Cube', True, BLACK)
toggle_pyramid_button_text = freesansbold_small.render('Pyramid', True, BLACK)
toggle_sphere_button_text = freesansbold_small.render('Sphere', True, BLACK)
toggle_custom_shape_button_text = freesansbold_small.render('Custom Shape', True, BLACK)


# buttons
toggle_verticies_button = Toggle_Button(toggle_verticies_button_rect, display, 1, False)
toggle_edges_button = Toggle_Button(toggle_edges_button_rect, display, 1, False)
toggle_faces_button = Toggle_Button(toggle_faces_button_rect, display, 1, False)
toggle_light_button = Toggle_Button(toggle_light_button_rect, display, 1, False)

toggle_cube_button = Toggle_Button(toggle_cube_button_rect, display, 1, False)
toggle_pyramid_button = Toggle_Button(toggle_pyramid_button_rect, display, 0, False)
toggle_sphere_button = Toggle_Button(toggle_sphere_button_rect, display, 0, False)
toggle_custom_shape_button = Toggle_Button(toggle_custom_shape_button_rect, display, 0, False)



# -- SLIDERS --
# sliders rect
light_intensity_slider_rect = pygame.Rect((15, 680), (14, 14))
light_radius_slider_rect = pygame.Rect((15, 650), (14, 14))
light_x_slider_rect = pygame.Rect((15, 600), (14, 14))
light_y_slider_rect = pygame.Rect((15, 570), (14, 14))
light_z_slider_rect = pygame.Rect((15, 540), (14, 14))


# sliders text
light_intensity_slider_text = freesansbold_small.render('Light Intensity', True, BLACK)
light_radius_slider_text = freesansbold_small.render('Light Radius', True, BLACK)
light_x_slider_text = freesansbold_small.render('Light X', True, BLACK)
light_y_slider_text = freesansbold_small.render('Light Y', True, BLACK)
light_z_slider_text = freesansbold_small.render('Light Z', True, BLACK)


# sliders
light_intensity_slider = Slider(display, (15, 680), 25, light_intensity_slider_rect)
light_radius_slider = Slider(display, (15, 650), 5, light_radius_slider_rect)
light_x_slider = Slider(display, (15, 600), 78, light_x_slider_rect)
light_y_slider = Slider(display, (15, 570), 75, light_y_slider_rect)
light_z_slider = Slider(display, (15, 540), 75, light_z_slider_rect)


# sliders variables
holding_light_intensity_slider = False
holding_light_radius_slider = False
holding_light_x_slider = False
holding_light_y_slider = False
holding_light_z_slider = False


# sliders rect position changing
pygame.Rect.move_ip(light_intensity_slider_rect, (light_intensity_slider.value, 0))
pygame.Rect.move_ip(light_radius_slider_rect, (light_radius_slider.value, 0))
pygame.Rect.move_ip(light_x_slider_rect, (light_x_slider.value, 0))
pygame.Rect.move_ip(light_y_slider_rect, (light_y_slider.value, 0))
pygame.Rect.move_ip(light_z_slider_rect, (light_z_slider.value, 0))


# render button texts
def render_button_texts():
    display.blit(settings_text, (916, 390))
    display.blit(toggle_verticies_button_text, (917, 620))
    display.blit(toggle_edges_button_text, (923, 550))
    display.blit(toggle_faces_button_text, (923, 480))
    display.blit(toggle_light_button_text, (938, 410))

    display.blit(shapes_text, (920, 0))
    display.blit(toggle_cube_button_text, (945, 20))
    display.blit(toggle_pyramid_button_text, (937, 90))
    display.blit(toggle_sphere_button_text, (941, 160))
    display.blit(toggle_custom_shape_button_text, (923, 230))


# render slider texts
def render_slider_texts():
    display.blit(light_intensity_slider_text, (55, 665))
    display.blit(light_radius_slider_text, (58, 635))
    display.blit(light_x_slider_text, (72, 585))
    display.blit(light_y_slider_text, (72, 555))
    display.blit(light_z_slider_text, (72, 525))


# graphics variables
rotation_x = 0 # cameras rotation on x axis
rotation_y = 0 # cameras rotation on y axis
rotation_z = 0 # cameras rotation on z axis

objPos = [window_width//2, window_height//2] # where the object should be pointed on the screen
fov = 500 # field of view (I think)
distance_from_object = 10 # cameras distance from the objects

light_enabled = True

points = 'placeholder'
edges = 'placeholder'
original_faces = 'placeholder'
current_shape = 'placeholder'
current_obj_file = 'placeholder'
# objects to render
def change_shape(shape, file=None, reset_camera=True):
    global points
    global edges
    global original_faces

    global current_shape
    global current_obj_file

    global distance_from_object
    global rotation_x
    global rotation_y
    global rotation_z

    if shape == 0:
        points = cube()[0] # gets the points that will be rendered
        edges = cube()[1] # gets the edges that will be rendered
        original_faces = cube()[2] # gets the faces that will be rendered
        current_shape = 0
    elif shape == 1:
        points = pyramid()[0] # gets the points that will be rendered
        edges = pyramid()[1] # gets the edges that will be rendered
        original_faces = pyramid()[2] # gets the faces that will be rendered
        current_shape = 1
    elif shape == 2:
        points = sphere()[0] # gets the points that will be rendered
        edges = sphere()[1] # gets the edges that will be rendered
        original_faces = sphere()[2] # gets the faces that will be rendered
        current_shape = 2
    elif shape == 3:
        points = load_obj(file)[0]
        edges = []
        original_faces = load_obj(file)[1]
        current_shape = 3
        current_obj_file = file

    for face in original_faces:
        tuple_exists = False
        for item in face:
            if type(item) is tuple:
                tuple_exists = True
        if tuple_exists == False:
            if light_enabled == True:
                face.append(GRAY)
            else:
                face.append(random_color())

    auto_zoom_list = []
    for point in points:
        for item in point:
            auto_zoom_list.append(item[0])

    if reset_camera == True:
        distance_from_object = max(auto_zoom_list) + 2 * 3
        rotation_x = 0
        rotation_y = 0
        rotation_z = 0

change_shape(0)


# load sprites
light_pos = [[light_x_slider.value - 75], [light_y_slider.value - 75], [light_z_slider.value - 75]]
light_radius = light_radius_slider.value
light_intensity = light_intensity_slider.value * 10
light_bulb = pygame.image.load('sprites/light_bulb.png')

light = Light(light_pos, light_radius, light_intensity, light_bulb)

# in-engine toggleable variables
do_render_faces = True
do_render_edges = True
do_render_verticies = True

# adjustable variables
sensitivity = 0.02 # how sensitive the movement is
scroll_sensitivity = 0.5 # how sensitive the camera is
max_fps = 165 # sets the frames per second (based on my monitors hertz)
max_distance = 250 # max distance the user can go away from the objects
min_distance = 2 # minimum distance the user can go close to the objects



# ---- MAIN LOOP ----
run = True
while run:
    # clock things
    clock.tick(max_fps)
    fps = clock.get_fps() # sets the fps variable to the current fps

    display.fill(WHITE) # fills the screen with white

    mouse_buttons = pygame.mouse.get_pressed() # gets the mouse buttons pressed
    if mouse_buttons[2]: # if that mouse button is pressed
        right_click = True # sets right_click to True
    else:
        right_click = False # sets right_click to False

    if mouse_buttons[0]:
        left_click = True
    else:
        left_click = False


    # pygame event detections
    for event in pygame.event.get(): # detects if theres an event in the frame
        if event.type == pygame.QUIT: # if the event is exitting out of pygame
            run = False # exits out of the loop


        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            move_amount = (prev_mouse[0] - pos[0], prev_mouse[1] - pos[1])
            if right_click == True: # if right click is being held down
                rotation_x += move_amount[1] * sensitivity
                rotation_y += move_amount[0] * sensitivity

            if holding_light_intensity_slider == True:
                light_intensity_slider.value -= move_amount[0]
                if light_intensity_slider.value > 150:
                    light_intensity_slider.value = 150
                elif light_intensity_slider.value < 0:
                    light_intensity_slider.value = 0

                light_intensity_slider_rect = pygame.Rect((light_intensity_slider.position[0] + light_intensity_slider.value - 10, light_intensity_slider.position[1]), (20, 20))
                light.intensity = light_intensity_slider.value * 10

            if holding_light_radius_slider == True:
                light_radius_slider.value -= move_amount[0]
                if light_radius_slider.value > 150:
                    light_radius_slider.value = 150
                elif light_radius_slider.value < 0:
                    light_radius_slider.value = 0

                light_radius_slider_rect = pygame.Rect((light_radius_slider.position[0] + light_radius_slider.value - 10, light_radius_slider.position[1]), (20, 20))
                light.radius = light_radius_slider.value

            if holding_light_x_slider == True:
                light_x_slider.value -= move_amount[0]
                if light_x_slider.value > 150:
                    light_x_slider.value = 150
                elif light_x_slider.value < 0:
                    light_x_slider.value = 0

                light_x_slider_rect = pygame.Rect((light_x_slider.position[0] + light_x_slider.value - 10, light_x_slider.position[1]), (20, 20))
                light.position[0][0] = light_x_slider.value - 75

            if holding_light_y_slider == True:
                light_y_slider.value -= move_amount[0]
                if light_y_slider.value > 150:
                    light_y_slider.value = 150
                elif light_y_slider.value < 0:
                    light_y_slider.value = 0

                light_y_slider_rect = pygame.Rect((light_y_slider.position[0] + light_y_slider.value - 10, light_y_slider.position[1]), (20, 20))
                light.position[1][0] = light_y_slider.value - 75

            if holding_light_z_slider == True:
                light_z_slider.value -= move_amount[0]
                if light_z_slider.value > 150:
                    light_z_slider.value = 150
                elif light_z_slider.value < 0:
                    light_z_slider.value = 0

                light_z_slider_rect = pygame.Rect((light_z_slider.position[0] + light_z_slider.value - 10, light_z_slider.position[1]), (20, 20))
                light.position[2][0] = light_z_slider.value - 75

            prev_mouse = pos


        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                holding_light_intensity_slider = False
                holding_light_radius_slider = False
                holding_light_x_slider = False
                holding_light_y_slider = False
                holding_light_z_slider = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() # gets the position of the mouse

            if event.button == 4: # scroll up
                if distance_from_object >= min_distance:
                    distance_from_object -= scroll_sensitivity # go towards object
            if event.button == 5: # scroll down
                if distance_from_object <= max_distance:
                    distance_from_object += scroll_sensitivity # go away from the object

            if event.button == 1: # left click
                if light_intensity_slider_rect.collidepoint(pos[0], pos[1]):
                    holding_light_intensity_slider = True

                if light_radius_slider_rect.collidepoint(pos[0], pos[1]):
                    holding_light_radius_slider = True

                if light_x_slider_rect.collidepoint(pos[0], pos[1]):
                    holding_light_x_slider = True

                if light_y_slider_rect.collidepoint(pos[0], pos[1]):
                    holding_light_y_slider = True

                if light_z_slider_rect.collidepoint(pos[0], pos[1]):
                    holding_light_z_slider = True

                if toggle_verticies_button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if toggle_verticies_button.disabled == False:
                        if toggle_verticies_button.clicked():
                            do_render_verticies = True
                        else:
                            do_render_verticies = False
                
                if toggle_edges_button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if toggle_edges_button.disabled == False:
                        if toggle_edges_button.clicked():
                            do_render_edges = True
                        else:
                            do_render_edges = False

                if toggle_faces_button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if toggle_faces_button.disabled == False:
                        if toggle_faces_button.clicked():
                            do_render_faces = True
                        else:
                            do_render_faces = False

                if toggle_light_button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if toggle_light_button.disabled == False:
                        if toggle_light_button.clicked():
                            light_enabled = True
                            change_shape(current_shape, current_obj_file, False)
                        else:
                            light_enabled = False
                            change_shape(current_shape, current_obj_file, False)

                
                if toggle_cube_button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if toggle_cube_button.disabled == False:
                        if toggle_cube_button.toggle == 0:
                            toggle_cube_button.clicked()
                            change_shape(0)
                            toggle_pyramid_button.toggle = 0
                            toggle_sphere_button.toggle = 0
                            toggle_custom_shape_button.toggle = 0

                if toggle_pyramid_button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if toggle_pyramid_button.disabled == False:
                        if toggle_pyramid_button.toggle == 0:
                            toggle_pyramid_button.clicked()
                            change_shape(1)
                            toggle_cube_button.toggle = 0
                            toggle_sphere_button.toggle = 0
                            toggle_custom_shape_button.toggle = 0

                if toggle_sphere_button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if toggle_sphere_button.disabled == False:
                        if toggle_sphere_button.toggle == 0:
                            toggle_sphere_button.clicked()
                            change_shape(2)
                            toggle_cube_button.toggle = 0
                            toggle_pyramid_button.toggle = 0
                            toggle_custom_shape_button.toggle = 0

                if toggle_custom_shape_button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if toggle_custom_shape_button.disabled == False:
                        if toggle_custom_shape_button.toggle == 0:
                            file = easygui.fileopenbox(default = './obj_files/*.obj')
                            change_shape(0)
                            toggle_custom_shape_button.clicked()
                            change_shape(3, file)
                            toggle_cube_button.toggle = 0
                            toggle_pyramid_button.toggle = 0
                            toggle_sphere_button.toggle = 0


    faces = deepcopy(original_faces)

    # -- VERTEX MATHS --

    projected_points = [p for p in range(len(points))] # gets the a list of point id's

    # matrices that we will be multiplying for 3d rotation math
    rotation_x_matrix = [[1, 0, 0], [0, cos(rotation_x), -sin(rotation_x)], [0, sin(rotation_x), cos(rotation_x)]]
    rotation_y_matrix = [[cos(rotation_y), 0, -sin(rotation_y)], [0, 1, 0], [sin(rotation_y), 0, cos(rotation_y)]]
    rotation_z_matrix = [[cos(rotation_z), -sin(rotation_z), 0], [sin(rotation_z), cos(rotation_z), 0], [0, 0, 1]]

    pointsZ = [] # list of the points distance from the camera
    for index, point in enumerate(points): # loops through the list of points
        # rotation math
        rotated = multiply_matrix(rotation_x_matrix, point)
        rotated = multiply_matrix(rotation_y_matrix, rotated)
        rotated = multiply_matrix(rotation_z_matrix, rotated)

        # projection math
        if distance_from_object != 0:
            z = 1/(distance_from_object - rotated[2][0])
        else:
            z = 0
        projection = [[z, 0, 0], [0, z, 0]]

        projected = multiply_matrix(projection, rotated)

        x = projected[0][0] * fov + objPos[0]
        y = projected[1][0] * fov + objPos[1]

        projected_points[index] = [x, y]

        pointsZ.append(z) # appends the points distance from the camera

    # -- SPRITE MATHS --
    rotated = multiply_matrix(rotation_x_matrix, light.position)
    rotated = multiply_matrix(rotation_y_matrix, rotated)
    rotated = multiply_matrix(rotation_z_matrix, rotated)

    if distance_from_object != 0:
        z = 1/(distance_from_object - rotated[2][0])
    else:
        z = 0
    projection = [[z, 0, 0], [0, z, 0]]
    projected = multiply_matrix(projection, rotated)
    light_bulb_x = projected[0][0] * fov + objPos[0]
    light_bulb_y = projected[1][0] * fov + objPos[1]



    for face in faces: # for every face that needs to be rendered (this one gets the avg z value of the face)
        faceZ = []
        for value in face:
            if isinstance(value, int) == True:
                faceZ.append(pointsZ[value])
        face.append(faceZ)
        if len(face) == 6:
            face.append(sum([face[5][0], face[5][1], face[5][2], face[5][3]]) / 4)
        elif len(face) == 5:
            face.append("placeholder")
            face.append(sum([face[4][0], face[4][1], face[4][2]]) / 3)
    faces.sort(key=itemgetter(6)) # sorts our list of faces by the average z value
    for index, face in enumerate(faces):
        if "placeholder" in face:
            face.remove("placeholder")

        if light_enabled == True:
            face_point_list = []
            for point in face:
                if type(point) == int:
                    face_point_list.append(points[point])

            x_list = []
            y_list = []
            z_list = []
            for point in face_point_list:
                x_list.append(point[0][0])
                y_list.append(point[1][0])
                z_list.append(point[2][0])

            if len(x_list) == 4:
                face_point_average = [[(x_list[0] + x_list[1] + x_list[2] + x_list[3]) / 4], [(y_list[0] + y_list[1] + y_list[2] + y_list[3]) / 4], [(z_list[0] + z_list[1] + z_list[2] + z_list[3]) / 4]]
            elif len(x_list) == 3:
                face_point_average = [[(x_list[0] + x_list[1] + x_list[2]) / 3], [(y_list[0] + y_list[1] + y_list[2]) / 3], [(z_list[0] + z_list[1] + z_list[2]) / 3]]

            if in_range(face_point_average, light.position, light.radius) == True:
                distance_between = sqrt((light.position[0][0] - face_point_average[0][0]) ** 2 + (light.position[1][0] - face_point_average[1][0]) ** 2 + (light.position[2][0] - face_point_average[2][0]) ** 2)
                if distance_between == 0:
                    distance_between = 0.01
                change = light.intensity / distance_between
                if len(x_list) == 4:
                    faces[index][4] = (face[4][0] + change, face[4][1] + change, face[4][2] + change)
                elif len(x_list) == 3:
                    faces[index][3] = (face[3][0] + change, face[3][1] + change, face[3][2] + change)

            if len(x_list) == 4:
                if faces[index][4][0] > 255:
                    faces[index][4] = (255, 255, 255)
                elif faces[index][4][0] < 0:
                    faces[index][4] = (0, 0, 0)
            elif len(x_list) == 3:
                if faces[index][3][0] > 255:
                    faces[index][3] = (255, 255, 255)
                elif faces[index][3][0] < 0:
                    faces[index][3] = (0, 0, 0)


    # DRAWING TO THE PYGAME WINDOW


    def render_faces():
        for index, face in enumerate(faces): # for every face that needs to be rendered (this one renders the face based on teh average z value)
            a = (projected_points[face[0]][0], projected_points[face[0]][1])
            b = (projected_points[face[1]][0], projected_points[face[1]][1])
            c = (projected_points[face[2]][0], projected_points[face[2]][1])
            if len(face) == 7:
                d = (projected_points[face[3]][0], projected_points[face[3]][1])
                e = face[4]
                pygame.draw.polygon(display, e, (a, b, c, d))
            else:
                e = face[3]
                pygame.draw.polygon(display, e, (a, b, c))

    def render_edges():
        for edge in edges: # for every edge that needs to be rendered
            a = (projected_points[edge[0]][0], projected_points[edge[0]][1])
            b = (projected_points[edge[1]][0], projected_points[edge[1]][1])

            pygame.draw.line(display, BLACK, a, b, 2) # renders the edge

    def render_verticies():
        for point in projected_points:
            pygame.draw.circle(display, RED, (int(point[0]), int(point[1])), 4)

    if do_render_faces == True:
        render_faces()
    if do_render_edges == True:
        render_edges()
    if do_render_verticies == True:
        render_verticies()


    # draw light bulb
    if light_enabled == True:
        display.blit(light.sprite, (light_bulb_x - 12, light_bulb_y - 12))


    if edges == []:
        toggle_edges_button.disabled = True
    else:
        toggle_edges_button.disabled = False

    # BUTTON RENDERING
    toggle_verticies_button.draw()
    toggle_edges_button.draw()
    toggle_faces_button.draw()
    toggle_light_button.draw()
    
    toggle_cube_button.draw()
    toggle_pyramid_button.draw()
    toggle_sphere_button.draw()
    toggle_custom_shape_button.draw()


    # SLIDER RENDERING
    if light_enabled == True:
        light_intensity_slider.draw()
        light_radius_slider.draw()
        light_x_slider.draw()
        light_y_slider.draw()
        light_z_slider.draw()


    # TEXT REGISTERING
    fps_text = freesansbold.render('FPS: ' + str(round(fps, 2)), True, BLACK)
    hint_text = freesansbold_small.render('(Hold Right-Click to Rotate the Camera)', True, BLACK)

    light_intensity_value_text = freesansbold.render(str(light.intensity), True, BLACK)
    light_radius_value_text = freesansbold.render(str(light.radius), True, BLACK)
    light_x_value_text = freesansbold.render(str(light.position[0][0]), True, BLACK)
    light_y_value_text = freesansbold.render(str(light.position[1][0]), True, BLACK)
    light_z_value_text = freesansbold.render(str(light.position[2][0]), True, BLACK)

    # TEXT RENDERING
    display.blit(fps_text, (0, 0))
    display.blit(hint_text, (400, 0))

    render_button_texts()

    if light_enabled == True:
        render_slider_texts()

        display.blit(light_intensity_value_text, (175, 675))
        display.blit(light_radius_value_text, (175, 645))
        display.blit(light_x_value_text, (175, 595))
        display.blit(light_y_value_text, (175, 565))
        display.blit(light_z_value_text, (175, 535))


    pygame.display.update() # updates the pygame display


# ---- POST LOOP ----
pygame.quit() # quits out of the pygame window
