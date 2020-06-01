import pygame, sys, random, pickle, time

lines = [line.rstrip() for line in open('First Game High Scores.txt')]  # Reads the text file line by line
high_scores_names = []  # Creates a list for the names of people with high scores
high_scores = []  # Creates a list for the high scores

for i in range(0, 9, 2):  # Puts the names of the people with high scores in a list
    high_scores_names.append(lines[i])

for i in range(1, 10, 2):  # Puts the high scores in a list
    high_scores.append(int(lines[i]))

pygame.init()
pygame.mixer.init()
#pygame.mixer.music.load('ALI-A INTRO EARRAPE [FULL SONG].mp3')
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(0.5)  # Sets the volume of the music (0-1.0)

font = pygame.font.SysFont("monospace", 35)
font2 = pygame.font.SysFont("times new roman", 40, True)
HEIGHT = 600
WIDTH = 800

draw_line = False
horizontal_line = HEIGHT / 2 + 50

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size] #If you want player exactly in middle: WIDTH/2 - player_size/2 #initial position

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 100]
enemy_list = [enemy_pos]

SPEED = 7
score = 0 #should be 0
num_enemies = 5
level = 1 #should be 1
screen = pygame.display.set_mode((WIDTH, HEIGHT))

counter = 0
counter2 = 0
right_side = True  # Used to put player on the right side of the screen at the start of level 4
game_over = False
clock = pygame.time.Clock()


def countdown():
    for i in range(3, 0):
        text5 = str(i)
        label5 = font2.render(text5, 10, WHITE)
        text_rect = label5.get_rect(center=(WIDTH // 2, 100))
        screen.blit(label5, text_rect)
        time.sleep(1)
        screen.fill(BLACK)


def draw_grid():
    for c in range(0, WIDTH, player_size):
        pygame.draw.line(screen, WHITE, (c, 0), (c, HEIGHT), 2)  # Vertical lines, can comment out


def set_level(score, SPEED, player_pos):
    global num_enemies, level, WIDTH, enemy_size, screen, draw_line, HEIGHT, player_size, counter, right_side
    if score < 20:
        #different_speeds = [2, 10, 14, 16, 30]
        #s = random.randint(0, 4)
        #SPEED = different_speeds[s]
        SPEED = 7
        num_enemies = 8
        level = 1
    elif score < 40:
        SPEED = 10
        num_enemies = 11
        level = 2
    elif score < 60:
        SPEED = 14
        num_enemies = 14
        level = 3
    elif score < 100:
        SPEED = 16
        num_enemies = 16
        WIDTH = 600
        if player_pos[0] >= 600 and right_side:
            player_pos[0] = 600-player_size
            right_side = False
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        level = 4
    else: #if score >= 100
        draw_line = True
        if player_pos[1] <= horizontal_line:
            draw_line = False
            HEIGHT = 600 // 2 + 50 + (3 * player_size)  # Changes height of screen
        enemy_size = 50 #should be 60 OR 50
        player_size = 40
        SPEED = 19
        num_enemies = 19
        WIDTH = 600
        if counter == 0:
            #time.sleep(3)
            #text4 = "Ready for level 5?"
            #label4 = font2.render(text4, 1, WHITE)
            #text_rect = label4.get_rect(center = (WIDTH // 2, 100))
            #screen.blit(label4, text_rect)
            #countdown()
            counter = 1
        if player_pos[1] > horizontal_line:
            player_pos[1] -= 1
        #if player_pos[0] >= 600: #if the player is near the right side of the screen, don't cut them off the screen
            #player_pos[0] = WIDTH-player_size # not needed I think
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        level = 5
    return SPEED


def scores():
    if score < high_scores[4]:  # IF user is not in the top 5
        same_scores = True
    else:
        same_scores = False
    if score >= high_scores[4]:  # If the user is now in the top 5
        name = str(input("Enter your name: "))  # Prompts user to enter their name
        if score > high_scores[0]:  # If the user is now in first place
            for i in range(4, 0, -1):  # Drops everyone in the standings down by 1
                high_scores[i] = high_scores[i - 1]
            high_scores[0] = score

            for i in range(4, 0, -1):  # Drops everyone in the standings down by 1
                high_scores_names[i] = high_scores_names[i - 1]
            high_scores_names[0] = name

        elif high_scores[1] <= score < high_scores[0]:  # If the user is now in second place
            # high_scores[0] remains the same
            for i in range(4, 1, -1):  # Drops everyone in the standings down by 1
                high_scores[i] = high_scores[i - 1]
            for i in range(4, 1, -1):  # Drops everyone in the standings down by 1
                high_scores_names[i] = high_scores_names[i - 1]
            high_scores[1] = score
            high_scores_names[1] = name

        elif high_scores[2] <= score < high_scores[1]:  # If the user is now in third place
            for i in range(4, 2, -1):  # Drops everyone in the standings down by 1
                high_scores[i] = high_scores[i - 1]
            for i in range(4, 2, -1):  # Drops everyone in the standings down by 1
                high_scores_names[i] = high_scores_names[i - 1]
            high_scores[2] = score
            high_scores_names[2] = name

        elif high_scores[3] <= score < high_scores[2]:  # If the user is now in fourth place
            for i in range(4, 3, -1):  # Drops everyone in the standings down by 1
                high_scores[i] = high_scores[i - 1]
            for i in range(4, 3, -1):  # Drops everyone in the standings down by 1
                high_scores_names[i] = high_scores_names[i - 1]
            high_scores[3] = score
            high_scores_names[3] = name
        elif high_scores[4] <= score < high_scores[3]:  # If the user is now in fifth place
            high_scores[4] = score
            high_scores_names[4] = name

    open("First Game High Scores.txt", "w").close()  # Delete everything in the text file
    updated_lines = ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5]  # Creates array with 10 elements
    updated_lines[0] = high_scores_names[0]  # Update the high scores information
    updated_lines[1] = str(high_scores[0])
    updated_lines[2] = high_scores_names[1]
    updated_lines[3] = str(high_scores[1])
    updated_lines[4] = high_scores_names[2]
    updated_lines[5] = str(high_scores[2])
    updated_lines[6] = high_scores_names[3]
    updated_lines[7] = str(high_scores[3])
    updated_lines[8] = high_scores_names[4]
    updated_lines[9] = str(high_scores[4])

    longest_name = len(max(high_scores_names, key=len))  # Gets the length of the longest name

    counter = 0  # See for loop below
    with open('First Game High Scores.txt', 'w') as file:  # Writes information to the text file
        for i in updated_lines:
            counter += 1
            file.write(i)
            if counter <= 9:  # This prevents making an extra line at the end of the file
                file.write('\n')

    file.close()  # Closes the text file
    print ('')
    print ('Your score: ', score)
    if same_scores:  # If the high scores remained the same
        print ('')
        print ('The high scores did not change.')
        print ('')
        print (' HIGH SCORES')
    else:
        print ('')
        print('NEW HIGH SCORES')

    for i in range(0, 5, 1):
        # print (high_scores_names[i], high_scores[i])  # Prints the new high scores
        print(high_scores_names[i].ljust(longest_name + 1, ' '),
              str(high_scores[i]).ljust(20, ' '))  # Prints the high scores


def ready():
    global label3
    counter3 = 1
    screen.fill(BLACK)
    text3 = "Press any key to start the game."
    label3 = font.render(text3, 1, WHITE)
    screen.blit(label3, (60, 40))
    pygame.display.update()
    while counter3 == 1:
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                counter3 = 0
                pygame.mixer.music.play(-1, 0)  # Plays the background music
                break


def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < num_enemies and delay < 0.1:
        x_pos = random.randint(0, WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    if level <= 4:
        for enemy_pos in enemy_list:
            pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    else:
        for enemy_pos in enemy_list:
            pygame.draw.rect(screen, WHITE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def update_enemy_positions(enemy_list, enemy_pos):
    # Updates position of enemy
    global score
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] <= HEIGHT:  # If enemy block is still in game
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    if level == 4:
        diagonal = random.random()
        if diagonal <= 0.6: # 60% of the enemies will go diagonally
            enemy_pos[0] += 3
    #elif level == 5:
     #   diagonal = random.random()
      #  if diagonal <= 0.85: # 85% of the enemies will go diagonally
       #     enemy_pos[0] += 3
    return score


def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False


def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x > p_x and e_x < (p_x + player_size)) or (p_x > e_x and p_x < (e_x + enemy_size)):
        if (e_y > p_y and e_y < (p_y + player_size)) or (p_y > e_y and p_y < (e_y + enemy_size)):
            return True
    return False


ready()

while not game_over:
    for event in pygame.event.get():
        #print(event) #can comment out
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT or event.key == pygame.K_a and x >= player_size:
                x -= player_size
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and x < WIDTH - player_size:
                x += player_size
            #elif event.key == pygame.K_UP and y > player_size: #Vertical movement
            #    y -= player_size
            #elif event.key == pygame.K_DOWN and y < HEIGHT - player_size: #Vertical movement
            #   y += player_size

            player_pos = [x, y]

    screen.fill(BLACK)
    #draw_grid()
    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, enemy_pos)
    SPEED = set_level(score, SPEED, player_pos)

    text = "Score: " + str(score)
    label = font.render(text, 1, YELLOW)
    text2 = "Level: " + str(level)
    label2 = font.render(text2, 1, RED)
    screen.blit(label2, (10, HEIGHT - 40))
    screen.blit(label, (WIDTH - 210, HEIGHT - 40))

    if collision_check(enemy_list, player_pos):
        draw_enemies(enemy_list)
        game_over = True
        scores()  # Updates the new high scores

    draw_enemies(enemy_list)  # Draws enemies
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    if draw_line:
        pygame.draw.line(screen, WHITE, (0, horizontal_line), (WIDTH, horizontal_line), 2)  # Horizontal line
    clock.tick(30)  # 30 frames per second
    #print (enemy_list)

    pygame.display.update()
