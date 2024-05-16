### Game 2048 ###
import pygame
import random
from time import sleep

def draw_color():
    # This function will draw the color of the squares
    if in_animation:
        if direction == "right" or direction == "left":
            for i in range(4):
                for j in range(4):
                    if copy[i][j] == 2:
                        pygame.draw.rect(screen, "sandy brown", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 4:
                        pygame.draw.rect(screen, "tan", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 8:
                        pygame.draw.rect(screen, "darkkhaki", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 16:
                        pygame.draw.rect(screen, "olivedrab", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 32:
                        pygame.draw.rect(screen, "darkgreen", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 64:
                        pygame.draw.rect(screen, "cyan", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 128:
                        pygame.draw.rect(screen, "skyblue", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 256:
                        pygame.draw.rect(screen, "gold", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 512:
                        pygame.draw.rect(screen, "violet", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 1024:
                        pygame.draw.rect(screen, "fuchsia", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
                    elif copy[i][j] == 2048:
                        pygame.draw.rect(screen, "crimson", (j*120+400+distanced_moved[i][j], i*120+120, 90, 90))
        elif direction == "up" or direction == "down":
            for i in range(4):
                for j in range(4):
                    if copy[i][j] == 2:
                        pygame.draw.rect(screen, "sandy brown", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 4:
                        pygame.draw.rect(screen, "tan", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 8:
                        pygame.draw.rect(screen, "darkkhaki", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 16:
                        pygame.draw.rect(screen, "olivedrab", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 32:
                        pygame.draw.rect(screen, "darkgreen", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 64:
                        pygame.draw.rect(screen, "cyan", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 128:
                        pygame.draw.rect(screen, "skyblue", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 256:
                        pygame.draw.rect(screen, "gold", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 512:
                        pygame.draw.rect(screen, "violet", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 1024:
                        pygame.draw.rect(screen, "fuchsia", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
                    elif copy[i][j] == 2048:
                        pygame.draw.rect(screen, "crimson", (j*120+400, i*120+120+distanced_moved[i][j], 90, 90))
    else:
        for i in range(4):
            for j in range(4):
                if r[i][j] == 0:
                    pygame.draw.rect(screen, "white", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 2:
                    pygame.draw.rect(screen, "sandy brown", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 4:
                    pygame.draw.rect(screen, "tan", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 8:
                    pygame.draw.rect(screen, "darkkhaki", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 16:
                    pygame.draw.rect(screen, "olivedrab", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 32:
                    pygame.draw.rect(screen, "darkgreen", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 64:
                    pygame.draw.rect(screen, "cyan", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 128:
                    pygame.draw.rect(screen, "skyblue", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 256:
                    pygame.draw.rect(screen, "gold", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 512:
                    pygame.draw.rect(screen, "violet", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 1024:
                    pygame.draw.rect(screen, "fuchsia", (j*120+400, i*120+120, 90, 90))
                elif r[i][j] == 2048:
                    pygame.draw.rect(screen, "crimson", (j*120+400, i*120+120, 90, 90))

def draw_white():
    # This function will draw the white squares when in animation.
    for i in range(4):
        for j in range(4):
            if copy[i][j] == 0:
                pygame.draw.rect(screen, "white", (j*120+400, i*120+120, 90, 90))

def write_number():
    # This function will write the numbers on the squares and other text.
    font = pygame.font.Font(None, 54)
    text = font.render("Points: " + str(p), True, "black")
    screen.blit(text, (100, 100))
    font = pygame.font.Font(None, 54)
    text = font.render("Press Backspace to Undo", True, "black")
    screen.blit(text, (560, 600))
    if in_animation:
        if direction == "right" or direction == "left":
            for i in range(4):
                for j in range(4):
                    if copy[i][j] > 0 and copy[i][j] < 10:
                        font = pygame.font.Font(None, 54)
                        text = font.render(str(copy[i][j]), True, "black")
                        screen.blit(text, (j*120+435+distanced_moved[i][j], i*120+150))
                    elif copy[i][j] > 10 and copy[i][j] < 100:
                        font = pygame.font.Font(None, 54)
                        text = font.render(str(copy[i][j]), True, "black")
                        screen.blit(text, (j*120+425+distanced_moved[i][j], i*120+150))
                    elif copy[i][j] > 100 and copy[i][j] < 1000:
                        font = pygame.font.Font(None, 54)
                        text = font.render(str(copy[i][j]), True, "black")
                        screen.blit(text, (j*120+412+distanced_moved[i][j], i*120+150))
                    if copy[i][j] > 1000:
                        font = pygame.font.Font(None, 54)
                        text = font.render(str(copy[i][j]), True, "black")
                        screen.blit(text, (j*120+400+distanced_moved[i][j], i*120+150))
        elif direction == "up" or direction == "down":
            for i in range(4):
                for j in range(4):
                    if copy[i][j] > 0 and copy[i][j] < 10:
                        font = pygame.font.Font(None, 54)
                        text = font.render(str(copy[i][j]), True, "black")
                        screen.blit(text, (j*120+435, i*120+150+distanced_moved[i][j]))
                    elif copy[i][j] > 10 and copy[i][j] < 100:
                        font = pygame.font.Font(None, 54)
                        text = font.render(str(copy[i][j]), True, "black")
                        screen.blit(text, (j*120+425, i*120+150+distanced_moved[i][j]))
                    elif copy[i][j] > 100 and copy[i][j] < 1000:
                        font = pygame.font.Font(None, 54)
                        text = font.render(str(copy[i][j]), True, "black")
                        screen.blit(text, (j*120+412, i*120+150+distanced_moved[i][j]))
                    if copy[i][j] > 1000:
                        font = pygame.font.Font(None, 54)
                        text = font.render(str(copy[i][j]), True, "black")
                        screen.blit(text, (j*120+400, i*120+150+distanced_moved[i][j]))
    else:
        for i in range(4):
            for j in range(4):
                if r[i][j] > 0 and r[i][j] < 10:
                    font = pygame.font.Font(None, 54)
                    text = font.render(str(r[i][j]), True, "black")
                    screen.blit(text, (j*120+435, i*120+150))
                elif r[i][j] > 10 and r[i][j] < 100:
                    font = pygame.font.Font(None, 54)
                    text = font.render(str(r[i][j]), True, "black")
                    screen.blit(text, (j*120+425, i*120+150))
                elif r[i][j] > 100 and r[i][j] < 1000:
                    font = pygame.font.Font(None, 54)
                    text = font.render(str(r[i][j]), True, "black")
                    screen.blit(text, (j*120+412, i*120+150))
                if r[i][j] > 1000:
                    font = pygame.font.Font(None, 54)
                    text = font.render(str(r[i][j]), True, "black")
                    screen.blit(text, (j*120+400, i*120+150))
    font = pygame.font.Font(None, 54)
    text = font.render("Press Enter to Restart", True, "black")
    screen.blit(text, (100, 600))
    font = pygame.font.Font(None, 54)
    text = font.render("Press W, A, S, D or Arrow Keys to Move", True, "black")
    screen.blit(text, (100, 650))

def distance_to_move(dir):
    # This function will return the distance of the numbers will move.
    distance = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    if dir == "right":
        for i in range(4):
            for j in range(4):
                if r[i][j] > 0:
                    for k in range(j+1, 4):
                        if r[i][k] == 0:
                            distance[i][j] += 1
                        elif r[i][j] == r[i][k]:
                            distance[i][j] += 1
                            break
                        else:
                            break
        for i in range(4):
            for j in range(2, -1, -1):
                distance[i][j] += distance[i][j+1]
            if r[i][0] == r[i][1] == r[i][2] == r[i][3]:
                distance[i][0] -= 1
                distance[i][1] -= 1
            elif r[i][0] == r[i][1] == r[i][2]:
                distance[i][0] -= 1
            elif r[i][1] == r[i][2] == r[i][3] and r[i][1] != 0:
                distance[i][1] -= 1
                if r[i][0] > 0:
                    distance[i][0] -= 1
            elif r[i][0] == r[i][1] == r[i][3] and r[i][2] == 0:
                distance[i][0] -= 1
            elif r[i][0] == r[i][2] == r[i][3] and r[i][1] == 0:
                distance[i][0] -= 1
            
    elif dir == "down":
        for i in range(4):
            for j in range(4):
                if r[j][i] > 0:
                    for k in range(j+1, 4):
                        if r[k][i] == 0:
                            distance[j][i] += 1
                        elif r[j][i] == r[k][i]:
                            distance[j][i] += 1
                            break
                        else:
                            break
        for i in range(4):
            for j in range(2, -1, -1):
                distance[j][i] += distance[j+1][i]
            if r[0][i] == r[1][i] == r[2][i] == r[3][i]:
                distance[0][i] -= 1
            elif r[0][i] == r[1][i] == r[2][i]:
                distance[0][i] -= 1
            if r[1][i] == r[2][i] == r[3][i] and r[1][i] != 0:
                distance[1][i] -= 1
                if r[0][i] > 0:
                    distance[0][i] -= 1
            if r[0][i] == r[1][i] == r[3][i] and r[2][i] == 0:
                distance[0][i] -= 1
            if r[0][i] == r[2][i] == r[3][i] and r[1][i] == 0:
                distance[0][i] -= 1

    elif dir == "left":
        for i in range(4):
            for j in range(4):
                if r[i][j] > 0:
                    for k in range(j-1, -1, -1):
                        if r[i][k] == 0:
                            distance[i][j] += 1
                        elif r[i][j] == r[i][k]:
                            distance[i][j] += 1
                            break
                        else:
                            break
        for i in range(4):
            for j in range(1, 4):
                distance[i][j] += distance[i][j-1]
            if r[i][3] == r[i][2] == r[i][1]== r[i][0]:
                distance[i][3] -= 1
                distance[i][2] -= 1
            elif r[i][3] == r[i][2] == r[i][1]:
                distance[i][3] -= 1
            elif r[i][2] == r[i][1] == r[i][0] and r[i][2] != 0:
                distance[i][2] -= 1
                if r[i][3] > 0:
                    distance[i][3] -= 1
            elif r[i][3] == r[i][2] == r[i][0] and r[i][1] == 0:
                distance[i][3] -= 1
            elif r[i][3] == r[i][1] == r[i][0] and r[i][2] == 0:
                distance[i][3] -= 1    
        for i in range(4):
            for j in range(4):
                distance[i][j] = -distance[i][j]
    
    elif dir == "up":
        for i in range(4):
            for j in range(4):
                if r[j][i] > 0:
                    for k in range(j-1, -1, -1):
                        if r[k][i] == 0:
                            distance[j][i] += 1
                        elif r[j][i] == r[k][i]:
                            distance[j][i] += 1
                            break
                        else:
                            break
        for i in range(4):
            for j in range(1, 4):
                distance[j][i] += distance[j-1][i]
            if r[3][i] == r[2][i] == r[1][i] == r[0][i]:
                distance[3][i] -= 1
            elif r[3][i] == r[2][i] == r[1][i]:
                distance[3][i] -= 1
            if r[2][i] == r[1][i] == r[0][i] and r[2][i] != 0:
                distance[2][i] -= 1
                if r[3][i] > 0:
                    distance[3][i] -= 1
            if r[3][i] == r[2][i] == r[0][i] and r[1][i] == 0:
                distance[3][i] -= 1
            if r[3][i] == r[1][i] == r[0][i] and r[2][i] == 0:
                distance[3][i] -= 1    
        for i in range(4):
            for j in range(4):
                distance[i][j] = -distance[i][j]

    for i in range(4):
        for j in range(4):
            if r[i][j] == 0:
                distance[i][j] = 0
            distance[i][j] = distance[i][j] * 6
    return distance

def column_value():
    # This function returns the number of non-zero numbers in each column into a list.
    count = 0
    value=[0,0,0,0]
    for x in range(4):
        for y in range(4):
            if r[y][x] > 0:
                count +=1
        value[x] = count
        count = 0
    return(value)

def down():
    # This function moves the numbers down.
    column_list = column_value()
    global p
    # x is the row number and y is the column number
    for x in range(4):
        # If there is only one number in the column then it will move down to the last row.
        if column_list[x] == 1:
            value = 0
            for y in range(4):
                if r[y][x] > 0:
                    value = r[y][x]
                r[y][x] = 0
            r[3][x] = value
        elif column_list[x] == 2:
            value = [0,0]
            it = 0
            for y in range(4):
                if r[y][x] > 0:
                    value[it] = r[y][x]
                    it += 1
                r[y][x] = 0
            if value[0] == value[1]:
                r[3][x] = value[0] * 2
                p += value[0] * 2
            else:
                r[2][x] = value[0]
                r[3][x] = value[1]
        elif column_list[x] == 3:
            value = [0,0,0]
            it = 0
            for y in range(4):
                if r[y][x] == 0:
                    pos = it
                it += 1
            
            pop_pos = [0,1,2,3]
            pop_pos.remove(pos)
            value[0] = r[pop_pos[0]][x]
            value[1] = r[pop_pos[1]][x]
            value[2] = r[pop_pos[2]][x]

            if value[2] == value[1]:
                value = [0,0,value[0], value[1] * 2]
                p += value[1] * 2
            elif value[1] == value[0]:
                value = [0,0,value[0] * 2, value[2]]
                p += value[0] * 2
            else:
                value = [0, value[0], value[1], value[2]]
            r[0][x] = value[0]
            r[1][x] = value[1]
            r[2][x] = value[2]
            r[3][x] = value[3]
        elif column_list[x] == 4:
            value = [r[0][x], r[1][x], r[2][x], r[3][x]]
            if value[3] == value[2]:
                if value[1] == value[0]:
                    value = [0, 0, value[1]*2, value[3]*2]
                    p += value[1] * 2 + value[3] * 2
                else:
                    value = [0, value[0], value[1], value[3]*2]
                    p += value[3] * 2
            elif value[2] == value[1]:
                value = [0, value[0], value[2]*2, value[3]]
                p += value[2] * 2
            elif value[1] == value[0]:
                value = [0, value[1]*2, value[2], value[3]]
                p += value[1] * 2
            r[0][x] = value[0]
            r[1][x] = value[1]
            r[2][x] = value[2]
            r[3][x] = value[3]

def left():
    # This function moves the numbers to the left.
    n = 0
    global p
    for i in r:
        row_value = i.count(0)
        if row_value == 0:
            value = [0,0,0,0]
            for k in range(4):
                value[k] = i[k]

            if value[0] == value[1]:
                if value[2] == value[3]:
                    r[n] = [value[0]*2, value[2]*2, 0, 0]
                    p += value[0] * 2 + value[2] * 2
                else:
                    r[n] = [value[0]*2, value[2], value[3], 0]
                    p += value[0] * 2
            elif value[1] == value[2]:
                r[n] = [value[0], value[1]*2, value[3], 0]
                p += value[1] * 2
            elif value[2] == value[3]:
                r[n] = [value[0], value[1], value[2]*2, 0]
                p += value[2] * 2
            else:
                r[n] = [value[0], value[1], value[2], value[3]]
        elif row_value == 1:
            pos_ind = i.index(0)
            pos = [0,1,2,3]
            pos.remove(pos_ind)
            
            value = [i[pos[0]], i[pos[1]], i[pos[2]]]
            if value[1] == value[0]:
                r[n] = [value[1]*2, value[2], 0, 0]
                p += value[1] * 2
            elif value[2] == value[1]:
                r[n] = [value[0], value[2]*2, 0, 0]
                p += value[2] * 2
            else:
                r[n] = [value[0], value[1], value[2], 0]
        elif row_value == 2:
            pos = [0,1,2,3]
            copy = [i[0], i[1], i[2], i[3]]
            for k in range(2):
                pos_ind = copy.index(0)
                pos.pop(pos_ind)
                copy.pop(pos_ind)
            value = [i[pos[0]], i[pos[1]]]
            if value[0] == value[1]:
                r[n] = [value[0]*2, 0, 0, 0]
            else:
                r[n] = [value[0], value[1], 0, 0]
        elif row_value == 3:
            for k in i:
                if k > 0:
                    value = k
            r[n] = [value, 0, 0, 0]
        n += 1

def up():
    global p
    # This function moves the numbers up.
    column_list = column_value()
    
    for x in range(4):
        if column_list[x] == 1:
            value = 0
            for y in range(4):
                if r[y][x] > 0:
                    value = r[y][x]
                r[y][x] = 0
            r[0][x] = value
        elif column_list[x] == 2:
            value = [0,0]
            it = 0
            for y in range(4):
                if r[y][x] > 0:
                    value[it] = r[y][x]
                    it += 1
                r[y][x] = 0
            if value[0] == value[1]:
                r[0][x] = value[0] * 2
            else:
                r[0][x] = value[0]
                r[1][x] = value[1]
        elif column_list[x] == 3:
            value = [0,0,0]
            it = 0
            for y in range(4):
                if r[y][x] == 0:
                    pos = it
                it += 1
            
            pop_pos = [0,1,2,3]
            pop_pos.remove(pos)
            value[0] = r[pop_pos[0]][x]
            value[1] = r[pop_pos[1]][x]
            value[2] = r[pop_pos[2]][x]

            if value[0] == value[1]:
                value = [value[0] * 2, value[2],0,0]
                p += value[0] * 2
            elif value[1] == value[2]:
                value = [value[0], value[1] * 2,0,0]
                p += value[1] * 2
            else:
                value = [value[0], value[1], value[2], 0]
            r[0][x] = value[0]
            r[1][x] = value[1]
            r[2][x] = value[2]
            r[3][x] = value[3]
        elif column_list[x] == 4:
            value = [r[0][x], r[1][x], r[2][x], r[3][x]]
            if value[0] == value[1]:
                if value[2] == value[3]:
                    value = [value[0]*2, value[2]*2, 0, 0]
                    p += value[0] * 2 + value[2] * 2
                else:
                    value = [value[0]*2, value[2], value[3], 0]
                    p += value[0] * 2
            elif value[1] == value[2]:
                value = [value[0], value[1]*2, value[3], 0]
                p += value[1] * 2
            elif value[2] == value[3]:
                value = [value[0], value[1], value[2]*2, 0]
                p += value[2] * 2
            r[0][x] = value[0]
            r[1][x] = value[1]
            r[2][x] = value[2]
            r[3][x] = value[3]

def right():
    global p
    # This function moves the numbers to the right.
    n = 0
    for i in r:
        row_value = i.count(0)
        if row_value == 0:
            value = [0,0,0,0]
            for k in range(4):
                value[k] = i[k]

            if value[3] == value[2]:
                if value[1] == value[0]:
                    r[n] = [0,0,value[1] * 2, value[3] * 2]
                    p += value[1] * 2 + value[3] * 2
                else:
                    r[n] = [0, value[0], value[1], value[3] * 2]
                    p += value[3] * 2
            elif value[2] == value[1]:
                r[n] = [0,value[0], value[2] * 2, value[3]]
                p += value[2] * 2
            elif value[1] == value[0]:
                r[n] = [0, value[1]*2, value[2], value[3]]
                p += value[1] * 2
            else:
                r[n] = [value[0], value[1], value[2], value[3]]
        elif row_value == 1:
            pos_ind = i.index(0)
            pos = [0,1,2,3]
            pos.remove(pos_ind)
            
            value = [i[pos[0]], i[pos[1]], i[pos[2]]]
            if value[2] == value[1]:
                r[n] = [0,0, value[0], value[2]*2]
                p += value[2] * 2
            elif value[1] == value[0]:
                r[n] = [0, 0, value[1]*2, value[2]]
                p += value[1] * 2
            else:
                r[n] = [0, value[0], value[1], value[2]]
        elif row_value == 2:
            pos = [0,1,2,3]
            copy = [i[0], i[1], i[2], i[3]]
            for k in range(2):
                pos_ind = copy.index(0)
                pos.pop(pos_ind)
                copy.pop(pos_ind)
            value = [i[pos[0]], i[pos[1]]]
            if value[0] == value[1]:
                r[n] = [0,0,0, value[1]*2]
                p += value[1] * 2
            else:
                r[n] = [0,0,value[0], value[1]]
        elif row_value == 3:
            for k in i:
                if k > 0:
                    value = k
            r[n] = [0,0,0,value]
        n += 1

def add_new():
    # This function adds a new number to a random spot in the game.
    n = random.randint(1,10)
    if n == 1:
        n = 4
    else:
        n = 2
    count = -1
    for i in r:
        count += i.count(0)
    try:
        pos = random.randint(0, count)
    except ValueError:
        if game_over():
            display_game_over()
        return
    base = 0

    while pos > r[base].count(0) - 1:
        pos -= r[base].count(0)
        base += 1
    while pos > -1:
        if r[base][pos] == 0:
            r[base][pos] = n
            pos = -2
        pos += 1

def display_high_score():
    # This function will display the high score.
    font = pygame.font.Font(None, 54)
    text = font.render("High Score: " + str(high), True, "black")
    screen.blit(text, (75, 180))
    
def game_over():
    # This function will check if the game is over.
    for i in r:
        if 0 in i:
            return False
    for i in range(4):
        for j in range(3):
            if r[i][j] == r[i][j+1]:
                return False
            if r[j][i] == r[j+1][i]:
                return False
    return True

def game_won():
    # This function will check if the game is won.
    for i in r:
        for j in i:
            if j > 2048:
                return True
    return False

def display_game_over():
    # This function will display the game over screen.
    font = pygame.font.Font(None, 54)
    text = font.render("Game Over", True, "black")
    screen.blit(text, (1280 / 2 - text.get_width() / 2, 720 / 2 - text.get_height() / 2))

def display_game_won():
    # This function will display the game won screen.
    font = pygame.font.Font(None, 54)
    text = font.render("You Win", True, "black")
    screen.blit(text, (1280 / 2 - text.get_width() / 2, 60))

def set_game():
    s1 = random.randint(0, 15)
    s2 = random.randint(0, 14)

    if s1 == s2:
        s2 += 1

    #r stands for rubix
    rubix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #p stands for points

    if random.randint(1,10) == 1:
        n1 = 4
    else:
        n1 = 2
    if random.randint(1,10) == 1:
        n2 = 4
    else:
        n2 = 2

    rubix[s1//4][int((s1/4-s1//4)*4)] = n1
    rubix[s2//4][int((s2/4-s2//4)*4)] = n2

    return rubix


### Main Code ###
def main():
    global r, p, high, in_animation, distance, distanced_moved, copy, important_value, direction, screen, clock, running, dt
    r = set_game()
    p = 0
    last_p = 0
    high = 0
    in_animation = False
    distance = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    distanced_moved = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    last_pos = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    important_value = 1
    direction = "none"

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    while running:
        # Loop that ends when X button clicked.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("pink")


        # pygame.draw.lines(screen, "black", True, ((100, 100), (1180,100)), 3)
        if in_animation:
            draw_white()
        draw_color()
        write_number()
        display_high_score()

        keys = pygame.key.get_pressed()

        if not in_animation:
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                copy_p = p
                distance = distance_to_move("up")
                direction = "up"
                for i in range(4):
                    for j in range(4):
                        copy[i][j] = r[i][j]
                up()
                if copy != r:
                    add_new()
                    in_animation = True
                    last_pos = copy
                    last_p = copy_p

            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                distance = distance_to_move("down")
                direction = "down"
                copy_p = p
                for i in range(4):
                    for j in range(4):
                        copy[i][j] = r[i][j]
                down()
                if copy != r:
                    add_new()
                    in_animation = True
                    last_pos = copy
                    last_p = copy_p

            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                distance = distance_to_move("left")
                direction = "left"
                copy_p = p
                for i in range(4):
                    for j in range(4):
                        copy[i][j] = r[i][j]
                left()
                if copy != r:
                    add_new()
                    in_animation = True
                    last_pos = copy
                    last_p = copy_p

            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                distance = distance_to_move("right")
                direction = "right"
                copy_p = p
                for i in range(4):
                    for j in range(4):
                        copy[i][j] = r[i][j]
                right()
                if copy != r:
                    add_new()
                    in_animation = True
                    last_pos = copy
                    last_p = copy_p

            elif keys[pygame.K_BACKSPACE]:
                r = last_pos
                p = last_p
        else:
            for i in range(4):
                for j in range(4):
                    distanced_moved[i][j] += distance[i][j]
            important_value += 6
            if important_value > 120:
                in_animation = False
                important_value = 0
                distanced_moved = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        if game_over():
            display_game_over()
        
        if game_won():
            display_game_won()
        
        if p > high:
            high = p
        
        #Restart the game
        if keys[pygame.K_RETURN]:
            r = set_game()
            p = 0
            draw_color()
            write_number()
            sleep(0.2)

        pygame.display.flip()
        # limits FPS to 60
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
