import socket
import sys
import pygame
import time
from moviepy.editor import VideoFileClip
# Load the MP4 file
clip = VideoFileClip('/home/noam/hacking_game/hacked_bank1.mp4')

# Play the video on full screen
#clip.preview(fullscreen=True)#fullscreen=True


# Set up the client
host = '127.0.0.1'
port = 5976

# colors
white = (255, 255, 255)
red = (250, 0, 0)
blue = (19, 89, 194)
black = (0, 0, 0)
gray = (128, 128, 128)

back = '/home/noam/hacking_game/Back.png'

def clans():
    def refresh():
        global clan, balances
        host = '127.0.0.1'
        port = 5976

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        message = f'3'
        client.sendall(message.encode('utf-8'))

        data = client.recv(1024)
        response = data.decode('utf-8')
        print(f'Received response: {response}')
        balances = [item.split(":")[1] for item in response.split(", ")]
        clan = [item.split(":")[0] for item in response.split(", ")]
        print(clan)
        print(balances)

    # Initialize Pygame
    pygame.init()

    refresh()

    img1 = '/home/noam/hacking_game/button3.jpeg'

    # Set up the screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = screen.get_size()

    # Define the font size and spacing
    font_size = 100
    spacing = 30

    font = pygame.font.SysFont(None, font_size)

    # Calculate the size of the scrolling list
    num_fonts = len(clan)
    list_height = (font_size + spacing) * num_fonts

    # Define the position of the top of the scrolling list
    list_top = -150

    # Load the button image and create the button object
    img1 = pygame.image.load(img1)
    button1_size = (width / 2, 100)
    button1_image = pygame.transform.scale(img1, button1_size)
    button1_rect = pygame.Rect(width / 500, height / 500, button1_size[0], button1_size[1])

    # Load the button image and create the button object
    img2 = pygame.image.load(back)
    button2_size = (width / 8, height / 8)
    button2_image = pygame.transform.scale(img2, button2_size)
    button2_rect = pygame.Rect(width / 150 - 50, height / 1.17, button2_size[0], button2_size[1])

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    list_top -= font_size + spacing
                elif event.key == pygame.K_DOWN:
                    list_top += font_size + spacing
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    list_top -= font_size + spacing
                elif event.button == 5:  # Scroll down
                    list_top += font_size + spacing
                elif button1_rect.collidepoint(event.pos):
                    print("button clan clicked!")
                elif button2_rect.collidepoint(event.pos):
                    main_screen()

        if list_top > list_height - 1000:
            list_top = list_top - font_size - spacing
        elif list_top < -140:
            list_top = -150
        # Draw the background, number, and arrows
        screen.fill((60, 67, 75))
        for i, font_name in enumerate(clan):
            font_surface = font.render(font_name, True, (0, 0, 0))
            font_rect = font_surface.get_rect()
            font_rect.midtop = (width / 2, i * (font_size + spacing) - list_top)
            screen.blit(font_surface, font_rect)

            balance_surface = font.render(balances[i], True, (0, 0, 0))
            balance_rect = balance_surface.get_rect()
            balance_rect.midtop = (width / 1.3, i * (font_size + spacing) - list_top)
            screen.blit(balance_surface, balance_rect)

            screen.blit(button1_image, button1_rect)
            screen.blit(button2_image, button2_rect)
        # Update the screen
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

def levels():#Initialize Pygame
    bg_num = 0
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = screen.get_size()

    bg_img1 = pygame.image.load('/home/noam/hacking_game/around_the_world.jpg')
    bg_img2 = pygame.image.load('/home/noam/hacking_game/background.jpg')
    bg_img3 = pygame.image.load('/home/noam/hacking_game/TCP.png')

    back_list = [bg_img1, bg_img2]

    # Set up the font
    font = pygame.font.Font(None, 80)

    # Set up the initial number and its position
    num = 1

    arrow_font = pygame.font.Font(None, 100)

    # Set up the > button
    right_text = arrow_font.render(">", True, (255, 255, 255))
    right_rect = right_text.get_rect(center=(width / 1.05, height / 2))

    # Set up the > button
    left_text = arrow_font.render("<", True, (255, 255, 255))
    left_rect = left_text.get_rect(center=(width / 15, height / 2))

    # Load the button image and create the button object
    img2 = pygame.image.load(back)
    button2_size = (width / 8, height / 8)
    button2_image = pygame.transform.scale(img2, button2_size)
    button2_rect = pygame.Rect(width / 150 - 50, height / 1.17, button2_size[0], button2_size[1])

    # Main loop
    x_pos = width / 2
    moving = False
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    if num >= 2:
                        moving = 'left'
                elif event.key == pygame.K_RIGHT:
                    moving = 'right'
                    bg_num += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_rect.collidepoint(event.pos):
                    if num >= 2:
                        moving = 'left'
                elif right_rect.collidepoint(event.pos):
                    moving = 'right'
                elif button2_rect.collidepoint(event.pos):
                    main_screen()

        if moving == 'left':
            x_pos += 20
        if moving == 'right':
            x_pos -= 20
        # If the text has moved off the screen to the left, reset its position to the right
        if x_pos < -50:
            x_pos = width
            num += 1
            if bg_num != len(back) - 1:
                bg_num = 1
            else:
                bg_num = 0
        if x_pos > width:
            x_pos = 0
            num -= 1
            if bg_num == len(back) - 1:
                bg_num = 0
            else:
                bg_num = 1

        if x_pos == width / 2:
            moving = False

        # Load the background image and scale it to fit the screen
        bg_img = pygame.transform.scale(back_list[bg_num], (width, height))

        # Update the number and its position
        num_text = font.render(str(num), True, (255, 255, 255))
        num_rect = num_text.get_rect(center=(x_pos, height / 2))

        # Draw the background, number, and arrows
        screen.blit(bg_img, (0, 0))
        # screen.fill((0, 0, 0))
        screen.blit(num_text, num_rect)
        screen.blit(right_text, right_rect)
        screen.blit(left_text, left_rect)
        screen.blit(button2_image, button2_rect)
        # Update the screen
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
def main_screen():
    # Create some colors
    gray = (60, 67, 75)

    img1 = '/home/noam/hacking_game/sound_x.png'
    low_sound = '/home/noam/hacking_game/sound1.png'
    fine_sound = '/home/noam/hacking_game/sound2.png'
    hight_sound = '/home/noam/hacking_game/sound.png'
    img2 = '/home/noam/hacking_game/Question_Mark.png'
    img3 = '/home/noam/hacking_game/binary_bucks.png'
    img4 = '/home/noam/hacking_game/logo_red.png'
    img5 = '/home/noam/hacking_game/profile.png'
    img6 = '/home/noam/hacking_game/play.png'
    img7 = '/home/noam/hacking_game/defend.png'
    img8 = '/home/noam/hacking_game/Attack1.png'
    img9 = '/home/noam/hacking_game/Back.png'
    clan_image = '/home/noam/hacking_game/clans.png'

    sounds = [hight_sound, fine_sound, low_sound, img1]

    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = pygame.display.get_surface().get_size()

    # Create font object
    font = pygame.font.Font(None, 100)

    # Render the "hello" text onto a surface object
    text_surface = font.render(balance, True, red)
    text_rect = pygame.Rect(width / 2.3 - 40, height / 35, 0, 0)

    # Load the button image and create the button object
    img1 = pygame.image.load(img1)
    button1_size = (100, 100)
    button1_rect = pygame.Rect(width / 1, height / 1.12, button1_size[0], button1_size[1])

    # Load the second button image and create the button object
    img2 = pygame.image.load(img2)
    button2_size = (170, 100)
    button2_rect = pygame.Rect(width / 1 - 50, height / 1.12, button2_size[0], button2_size[1])

    # Load the 3rd button image and create the button object
    img3 = pygame.image.load(img3)
    button3_size = (120, 120)
    button3_rect = pygame.Rect(width / 2 - 50, height / 80, button3_size[0], button3_size[1])

    # Load the 4th button image and create the button object
    img4 = pygame.image.load(img4)
    button4_size = (1400, 800)
    button4_image = pygame.transform.scale(img4, button4_size)
    button4_rect = pygame.Rect(width / 8, height / 7, button1_size[0], button1_size[1])

    # Load the 5th button image and create the button object
    img5 = pygame.image.load(img5)
    button5_size = (500, 200)
    button5_rect = pygame.Rect(width / 8, height / 700, button5_size[0], button5_size[1])

    # Load the 6th button image and create the button object
    img6 = pygame.image.load(img6)
    button6_size = (500, height)
    button6_image = pygame.transform.scale(img6, button6_size)
    button6_rect = pygame.Rect(width / 8, height / 9999, button6_size[0], button6_size[1])

    # Load the 7th button image and create the button object
    img7 = pygame.image.load(img7)
    button7_size = (400, 125)
    button7_rect = pygame.Rect(width / 8, height / 3.15, button7_size[0], button7_size[1])

    # Load the 8th button image and create the button object
    img8 = pygame.image.load(img8)
    button8_size = (385, 110)
    button8_rect = pygame.Rect(width / 8, height / 6, button8_size[0], button8_size[1])

    # Load the 8th button image and create the button object
    img9 = pygame.image.load(img9)
    button9_size = (400, 100)
    button9_rect = pygame.Rect(width / 150 - 50, height / 2, button9_size[0], button9_size[1])

    # Load the clans button image and create the button object
    img10 = pygame.image.load(clan_image)
    clans_size = (400, 225)
    clans_rect = pygame.Rect(width / 8, height / 1.14, clans_size[0], clans_size[1])

    #set up the binary bucks box
    bucks_box_font = pygame.font.Font(None, 30)
    bucks_box_text = bucks_box_font.render("this is the binary bucks with them you can attack, defend, get spaciel levels and make clans", True, (255, 255, 255))
    bucks_box_rect = bucks_box_text.get_rect(center=(width/2, height/2))
    bucks_box_surface = pygame.Surface((bucks_box_rect.width+20, bucks_box_rect.height+20))
    bucks_box_surface.fill((255, 0, 0))
    bucks_box_surface.blit(bucks_box_text, bucks_box_text.get_rect(center=(bucks_box_surface.get_width()/2, bucks_box_surface.get_height()/2)))
    bucks_box_rect = bucks_box_surface.get_rect(center=(width/2, height/2))

    # set up the profile box
    profile_box_font = pygame.font.Font(None, 30)
    profile_box_text = profile_box_font.render(f'your username: {text1}', True, (255, 255, 255))
    profile_box_text1 = profile_box_font.render(f'your balance: {balance}', True, (255, 255, 255))
    profile_box_rect = profile_box_text.get_rect(center=(width / 8, height / 700))  # Move the box up by 20 pixels
    profile_box_surface = pygame.Surface((profile_box_rect.width + 100, profile_box_rect.height + 60))  # Increase the height of the box by 60 pixels
    profile_box_surface.fill((255, 0, 0))
    profile_box_surface.blit(profile_box_text, profile_box_text.get_rect(center=(profile_box_surface.get_width() / 2, profile_box_surface.get_height() / 4)))
    profile_box_surface.blit(profile_box_text1, profile_box_text1.get_rect(center=(profile_box_surface.get_width() / 2, profile_box_surface.get_height() * 3 / 4)))  # Add a new line for the balance variable
    profile_box_rect = profile_box_surface.get_rect(center=(width / 8, height / 4))  # Move the box up by 20 pixels

    # Set up the X button
    x_font = pygame.font.Font(None, 40)
    x_text = x_font.render("X", True, (255, 255, 255))
    x_rect = x_text.get_rect(topright=bucks_box_rect.move(5, -5).topleft)

    # Run the game loop
    sound_variable = 4
    running = True
    show_box = False
    show_box_profile = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # Check if the image was clicked
                if button1_rect.collidepoint(event.pos):
                    if sound_variable > len(sounds) - 1:
                        sound_variable = 0
                    if sound_variable != 3:
                        button1_size = (175, 100)
                    else:
                        button1_size = (100, 100)
                    img1 = pygame.image.load(sounds[sound_variable])
                    button1_image = pygame.transform.scale(img1, button1_size)
                    sound_variable += 1
                    print("working: button 1")
                elif button8_rect.collidepoint(event.pos):
                    print("attack button was pressed")
                    running = False
                    levels()
                    break
                elif button2_rect.collidepoint(event.pos):
                    print("working: button 2")
                elif button9_rect.collidepoint(event.pos):
                    print("working: button 9")
                    login_page()
                    running = False
                elif button5_rect.collidepoint(event.pos):
                    print(text1)
                    show_box_profile = True
                elif button7_rect.collidepoint(event.pos):
                    clans()
                elif clans_rect.collidepoint(event.pos):
                    clans()
                elif button3_rect.collidepoint(event.pos):
                    show_box = True
                else:
                    show_box_profile = False
                    show_box = False
            elif event.type == pygame.MOUSEMOTION:
                if button8_rect.collidepoint(event.pos):
                    button8_size = (440, 115.5)
                elif button7_rect.collidepoint(event.pos):
                    button7_size = (440, 154)
                elif button5_rect.collidepoint(event.pos):
                    button5_size = (550, 220)
                elif button3_rect.collidepoint(event.pos):
                    button3_size = (132, 132)
                elif button2_rect.collidepoint(event.pos):
                    button2_size = (187, 110)
                elif button1_rect.collidepoint(event.pos):
                    button1_size = (110, 110)
                elif button9_rect.collidepoint(event.pos):
                    #button9_size = (264, 148.5)
                    pass
                elif clans_rect.collidepoint(event.pos):
                    clans_size = (440, 137.5)
                else:
                    button8_size = (400, 105)
                    button7_size = (400, 140)
                    button5_size = (500, 200)
                    button3_size = (120, 120)
                    button2_size = (170, 100)
                    button1_size = (100, 100)
                    button9_size = (240, 135)
                    clans_size = (400, 125)
        # clear the screen between frames
        screen.fill(gray)
        button8_image = pygame.transform.scale(img8, button8_size)
        button8_rect = pygame.Rect(width / 8, height / 6, button8_size[0], button8_size[1])

        button7_image = pygame.transform.scale(img7, button7_size)
        button7_rect = pygame.Rect(width / 8, height / 3.15, button7_size[0], button7_size[1])

        button5_image = pygame.transform.scale(img5, button5_size)
        button5_rect = pygame.Rect(width / 8, height / 700, button5_size[0], button5_size[1])

        button3_image = pygame.transform.scale(img3, button3_size)
        button3_rect = pygame.Rect(width / 2 - 50, height / 80, button3_size[0], button3_size[1])

        button2_image = pygame.transform.scale(img2, button2_size)
        button2_rect = pygame.Rect(width / 1 - 50, height / 1.12, button2_size[0], button2_size[1])

        button1_image = pygame.transform.scale(img1, button1_size)
        button1_rect = pygame.Rect(width / 1, height / 1.12, button1_size[0], button1_size[1])

        button9_image = pygame.transform.scale(img9, button9_size)
        button9_rect = pygame.Rect(width / 8, height / 1.17, button9_size[0], button9_size[1])

        clan_image = pygame.transform.scale(img10, clans_size)
        clans_rect = pygame.Rect(width / 8, height / 2, clans_size[0], clans_size[1])

        # Draw the buttons
        button3_rect.x = width / 2.3 - 100 - 120 / 2  # x position of the button(3)
        screen.blit(button3_image, button3_rect)
        button4_rect.x = width / 2.5 - button4_size[0] / 2  # x position of the button(4)
        screen.blit(button4_image, button4_rect)
        button5_rect.x = width / 7.5 - 500 / 2  # x position of the button(5)
        screen.blit(button5_image, button5_rect)
        button6_rect.x = width / 1.15 - button6_size[0] / 2  # x position of the button(6)
        screen.blit(button6_image, button6_rect)
        button7_rect.x = width / 1.145 - 350 / 2  # x position of the button(7)
        screen.blit(button7_image, button7_rect)
        button8_rect.x = width / 1.15 - 350 / 2  # x position of the button(8)
        screen.blit(button8_image, button8_rect)
        button9_rect.x = width / 150 - 50  # x position of the button(9)
        screen.blit(button9_image, button9_rect)
        button1_rect.x = width / 1.035 - 100 / 2 # x position of the button(1)
        screen.blit(button1_image, button1_rect)
        button2_rect.x = width / 1.11 - 170 / 2  # x position of the button(2)
        screen.blit(button2_image, button2_rect)
        clans_rect.x = width / 1.14 - 350 / 2  # x position of the button(clans)
        screen.blit(clan_image, clans_rect)

        #draw the binary buck balance
        screen.blit(text_surface, text_rect)

        if show_box:
            screen.blit(bucks_box_surface, bucks_box_rect)
            pygame.draw.rect(screen, (0, 0, 0), bucks_box_rect, 3)
            screen.blit(x_text, x_rect)

        if show_box_profile:
            screen.blit(profile_box_surface, profile_box_rect)
            pygame.draw.rect(screen, (0, 0, 0), profile_box_rect, 3)
            #screen.blit(x_text, x_rect)

        # Update the display
        pygame.display.flip()

    # Clean up
    pygame.quit()

def login_page():
    global text1, text2, balance
    pygame.init()

    # Define the window size and load the background image
    size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    background_image = pygame.image.load("/home/noam/hacking_game/login_page1.jpg")
    background_image = pygame.transform.scale(background_image, (width, height))

    # Create the font
    font = pygame.font.SysFont('freeserif', 60)

    # Create the text input objects
    input_box1 = pygame.Rect(width / 1.685 , height / 3 - 50, 600, 80)
    input_box2 = pygame.Rect(width / 1.685, height / 3 + 50, 600, 80)
    color_inactive = red
    color_active = white
    color1 = color_inactive
    color2 = color_inactive
    active = 0
    text1 = 'enter user name'
    text2 = 'enter strong password'

    # Load the button image and create the button object
    button_image = pygame.image.load("/home/noam/hacking_game/button3.jpeg")
    button_size = (300, 130)
    button_image = pygame.transform.scale(button_image, button_size)
    button_rect = pygame.Rect(width / 2 - 50, height / 2.5 + 80, button_size[0], button_size[1])

    # Load the login button image and create the button object
    login_image = pygame.image.load("/home/noam/hacking_game/login.png")
    login_size = (119, 62)
    login_image = pygame.transform.scale(login_image, login_size)
    login_rect = pygame.Rect(width / 2 - 50, height / 1.075, login_size[0], login_size[1])

    # Load the login button image and create the button object
    login_image1 = pygame.image.load("/home/noam/hacking_game/sign_up.png")
    login_size1 = (171, 62)
    login_image1 = pygame.transform.scale(login_image1, login_size1)
    login_rect1 = pygame.Rect(width / 2 - 50, height / 1.08, login_size1[0], login_size1[1])

    # Create the screen
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    # Create font object
    font1 = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 70)

    # Render the "hello" text onto a surface object
    text_surface = font2.render("don't have an account? ", True, red)
    text_rect = pygame.Rect(width / 1.8 - 40, height / 1.07, 0, 0)

    # Render the "hello" text onto a surface object
    text_surface1 = font1.render("login", True, red)
    text_rect1 = pygame.Rect(width / 1.43 - 40, height / 6, 0, 0)

    # Render the "user name was already taken" text onto a surface object
    username_was_taken_surface = font1.render("username was already taken!", True, red)
    username_was_taken_rect = pygame.Rect(width / 20 - 40, height / 20, 0, 0)

    # Render the "user name or password was incorrect" text onto a surface object
    username_incorrect_surface = font1.render("user name or password was incorrect!", True, red)
    username_incorrect_rect = pygame.Rect(width / 20 - 40, height / 20, 0, 0)

    # Render the "user name or password was incorrect" text onto a surface object
    error = font1.render("you have error", True, red)
    error = pygame.Rect(width / 20 - 40, height / 20, 0, 0)

    # Start the main loop
    running = True
    logged_in = False
    no_user = False
    already_in = False
    login = 2
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the button was clicked
                if login_rect.collidepoint(event.pos) or login_rect1.collidepoint(event.pos):
                    if login == 1:
                        login = 2
                        text_surface1 = font1.render("login", True, red)
                        text_surface = font2.render("don't have an account?", True, red)
                    else:
                        login = 1
                        text_surface1 = font1.render("sign up", True, red)
                        text_surface = font2.render("already have an account?", True, red)
                    print(login)

                elif button_rect.collidepoint(event.pos):
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect((host, port))
                    """
                    try:
                        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client.connect((host, port))
                    except socket.gaierror or OSError or ConnectionRefusedError:
                        screen.blit(username_incorrect_surface, username_incorrect_rect)"""


                    # Send a message
                    print(login)
                    message = f'{login}{text1},{text2}'
                    client.sendall(message.encode('utf-8'))

                    print('Username:', text1)
                    print('Password:', text2)
                    # Check if an input box was clicked
                    # Receive a response
                    data = client.recv(1024)
                    response = data.decode('utf-8')
                    print(f'Received response: {response}')
                    money = response.split(',')
                    balance = money[1]
                    # Close the connection
                    client.close()
                    if response == 'no user,1':
                        no_user = True
                        already_in = False
                    elif response == 'username was already taken,!':
                        already_in = True
                        no_user = False
                    elif money[0] == "logged" or 'successfully signed up':
                        logged_in = True
                elif input_box1.collidepoint(event.pos):
                    if text1 == "enter user name":
                        text1 = ''
                    active = 0
                    color1 = color_active
                    color2 = color_inactive
                elif input_box2.collidepoint(event.pos):
                    if text2 == "enter strong password":
                        text2 = ''
                    active = 1
                    color1 = color_inactive
                    color2 = color_active
                else:
                    active = -1
                    color1 = color_inactive
                    color2 = color_inactive
            if event.type == pygame.KEYDOWN:
                # Check if the active input box was changed
                if event.key == pygame.K_TAB:
                    active = (active + 1) % 2
                    color1 = color_inactive if active == 0 else color_active
                    color2 = color_inactive if active == 1 else color_active
                elif active == 0:
                    # Update the text in the first input box
                    if event.unicode == "\r":
                        active = 1
                    elif event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode
                elif active == 1:
                    # Update the text in the second input box
                    if event.unicode == "\r":
                        active = 0
                    elif event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += event.unicode
            if event.type == pygame.KEYDOWN:
                # Check if the active input box was changed
                if event.key == pygame.K_TAB:
                    active = (active + 1) % 2
                    color1 = color_inactive if active == 0 else color_active
                    color2 = color_inactive if active == 1 else color_active
    
        if text2 == 'enter strong password':
            txt_surface2 = font.render(text2, True, white)
        else:
            text2_display = '*' * len(text2)
            txt_surface2 = font.render(text2_display, True, white)
        # Draw the screen
        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)
        txt_surface1 = font.render(text1, True, white)
        screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        button_rect.x = width / 1.345 - button_size[0] / 2
        screen.blit(button_image, button_rect)


        # draw the binary buck balance
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)
        if login == 2:
            login_rect1.x = width / 1.13 - login_size1[0] / 2
            screen.blit(login_image1, login_rect1)
        else:
            login_rect.x = width / 1.13 - login_size[0] / 2
            screen.blit(login_image, login_rect)

        if logged_in:
            running = False
            main_screen()
        elif already_in:
            screen.blit(username_was_taken_surface, username_was_taken_rect)
        elif no_user:
            screen.blit(username_incorrect_surface, username_incorrect_rect)

        # Update the display
        pygame.display.flip()
login_page()

























