Chess Game has one main file (PRESSME.py) with two 
networking modules of (chess_server.py and chess_client.py)
and a game set-up module (pieces.py).

The other files are base files used for prototyping and images 
used for displaying pieces. Feel free to play around with 
(moves_ches.py and chess.py) by running 
(chess.py) which should import (moves_ches.py). 

REQUIREMENTS:
- Must have Python installed (version used 2.7.16)
- Must have Pygame installed (version used 1.9.5)

IMPORTS:
- threadding
- pygame
- os
- time
- socket
- _thread
- pieces (module written for game)
- chess_client (module for network)


You can run the main file, 
but will not be able to connect online. 

To run server, you must
use active server and connect it with (chess_server.py)
file by changing appropriate host address and port
(left as comment where to change host and port numbers).

To connect online enter server address
and port in (chess_client.py). (You don't need a 
server if you choose to play with offline.)


MAIN FILE:

To start game open and run PRESSME.py, which will import 
(pieces.py) and (chess_client.py). The file will start window 
and will run game. 

There are three main buttons. (NEXT, OFFLINE, and ONLINE)

ONLINE (will only appear in menu screen):

Will connect you to server.
Will send you to play with an online person if 
found (wait-time to retry is 20s).
Will immediately start game once player is found.

OFFLINE (will appear only in menu screen):

Will send you to an offline game. 
You can let someone else play for the second 
player, or you can use offline for strategizing.


MAIN SCREEN:

ONLINE and OFFLINE will appear.


For GAME:

PLAYER 1 (BLUE) will start game.

When is your turn:
  - you can press any piece that's yours
    and you will be shown possible moves allowed
  - you will be able to move piece to its assigned 
    spot available (circles)

To WIN:

The other player must run out of time.
Take the other's king. (won't show if mated, 
haven't planned to enable such feature).


AFTER GAME is WON/LOST:

NEXT button will appear.
Once pressed you will be returned to menu screen.


ADDITIONALS:


0 bugs known:

1 improvement need:
- lessen time-lag between players online

If you happen to find any bugs, please contact me at 
luismorales062012@gmail.com

DISCLAIMER: The board-image is not under my jurisdiction for sell nor gain profit.
I use that board image solely for showing board and not for profit. If you intend 
to copy the board-image, by any means, I'm not in charge nor its under my name for 
that image in its entirety. The pieces-images (ROOK, QUEEN, KING, BISHOP, KNIGHT, PAWN)
are mine. IF you intend to use these images for your own non-profit motives, by all means, you 
have my jurisdiction to use them. AS FOR CODE, if you plan to use it for non-profit motives
you also have my jurisdiction. HOWEVER, if you intend to use any for 'profit', please 
consult me before you do so.

TL;DR - The board image is not mine, the other images are. If you plan to use the code or/and
the images for 'profit', please consult with me first.
