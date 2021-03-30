# import pygame, time
# from pygame import draw

# board = [
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0]]
# pygame.init()
# win = pygame.display.set_mode((500,500))
# pygame.display.set_caption('CHESS PYGAME')
# font = pygame.font.SysFont("Somic Sans MS", 30)


# def main():
#     run = True
#     clock = pygame.time.Clock()
    
#     while run:
#         update_game()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.quit()


# def update_game():
#     draw.rect(win, "red", (10,10,100,100))
#     text = font.render(("hello"), True, "blue")
#     win.blit(text, (50,50))
#     pygame.display.update()


# main()
############
# import pygame,time, sys
# from pygame import draw
# from pygame.locals import*
# pygame.init()
# screen_size = (400,400)
# screen = pygame.display.set_mode(screen_size)
# pygame.display.set_caption("timer")
# time_left = 90 #duration of the timer in seconds
# crashed  = False
# font = pygame.font.SysFont("Somic Sans MS", 30)
# color = (255, 255, 255)

# while not crashed:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             crashed = True
#     total_mins = time_left//60 # minutes left
#     total_sec = time_left-(60*(total_mins)) #seconds left
#     time_left -= 1
#     if time_left > -1:
#         draw.rect(screen, "blue", pygame.Rect(180, 180, 200, 60), 0, 15)
#         text = font.render(("Time left: "+str(total_mins)+":"+str(total_sec)), True, color)
#         screen.blit(text, (200, 200))
#         pygame.display.flip()
#         screen.fill((20,20,20))
#         time.sleep(1)#making the time interval of the loop 1sec
#     else:
#         text = font.render("Time Over!!", True, color)
#         screen.blit(text, (200, 200))
#         pygame.display.flip()
#         screen.fill((20,20,20))

# pygame.quit()
# sys.exit()


####
# import pygame, time
# from pygame import draw


# class Turns():
#     def __init__(self, window, font):
#         self._window = window
#         self._font = font
#         self.player1 = self.timer((705, 30), 90)
#         self.player2 = self.timer((705, 600), 90)

#     def set_player(self, player):
#         if "b" == player:
#             self.timer((705, 30),self.player1)
#         else:
#             self.timer((705, 600),self.player1)


#     def timer(self, position, time_rem):
#         player_time = time_rem
#         x,y = position
#         draw.rect(self._window, "white", (x,y,90,70), 0, 13)
#         timer_text = self._font.render(("Timer:"), True, "black")
#         player_time = self.constant_display(position, player_time)
#         self._window.blit(timer_text, (x+12,y+10))
#         pygame.display.update()
#         return player_time
    
#     def constant_display(self, position, time_left):
#         x,y = position
#         _time = time_left - time.time()
#         print(_time)
#         time_display = self._font.render(("00:00"), True, "black")
#         self._window.blit(time_display, (x+12,y+40))
#         return _time
    

# pygame.init()
# win = pygame.display.set_mode((900, 900))
# font = pygame.font.SysFont("Somic Sans MS", 30)
# pygame.display.set_caption('CHESS PYGAME')

# main = Turns(win, font)
# main.set_player("b")

# def update():
#     main.set_player("b")
#     pygame.display.update()


# while True:
#     update()
#     time.sleep(10)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             pygame.quit()
#######


# import time

# def start():
#     start = time.time()

# def player1():




# current_t = 1.90909

# time_rem = 90-current_t
# min = str(int(time_rem//60))
# sec = str(int(time_rem-(float(min)*60)))
# stringe = f"{min:0>2}:{sec:0>2}".format(min, sec)
# print(stringe)

# player_turn = "b"

# player_turn = "r" if player_turn == "b" else "b"
# print(player_turn)
# player_turn = "r" if player_turn == "b" else "b"
# print(player_turn)

###
#infinite loop
# t = [1,2]
# for i in t:
#     t.append(i)
#     print(t)
#     if t == 10:
#         t-= 1
###


import time

# class timer:
#     def __init__(self) -> None:
#         pass
#     def update_timer(self):
#         timed = time()
#         timed.time()
#         return timed

#     def get_time(self):
#         return self.update_timer()

# my_time = timer()
# i = 0
# while i <10:
#     i =+ 1
#     print(my_time.get_time())
# start = time.time()
# ex = 0
# while ex < 10:
#     ex =+ time.time() - start
#     print(int(ex))

# Submitter: lemoral1(Morales, Luis)

# print('My first program: a hybrid')
# print('Answer (from Inteprxter) =', '1,267,650,600,228,229,401,496,703,205,376')