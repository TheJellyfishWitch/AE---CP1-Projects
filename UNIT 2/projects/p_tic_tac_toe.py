# AE | P1 | Pesudocode Tic Tac Toe

#GET player_one name from user
#GET player_two name from user

# WHILE TRUE
    #SET board to empty_board
    #DISPLAY board

    #WHILE game_over is FALSE
        #GET player_one (x’s) space from user
        #UPDATE board
        #DISPLAY board
        #IF x in three rows / columns / diagonal
            #DISPLAY “Player One Wins!”
            #DISPLAY board
            #SET game-over to TRUE
        #ELSE IF board filled
            #DISPLAY “Tie, no one wins :(”
            #DISPLAY board
            #SET game_over to TRUE
        #END IF
        #IF game_over is FALSE
            #GET player_two (o’s) space from user
            #UPDATE board
            #DISPLAY board
            #IF o in three rows / columns / diagonal
                #DISPLAY “Player Two Wins!”
                #DISPLAY board
                #SET game_over to TRUE
            #ELSE IF board filled
                #DISPLAY “Tie, no one wins :(”
                #DISPLAY board
                #SET game_over to TRUE
            #END IF
        #END IF
    #END WHILE

    #DISPLAY “Would you like to play again?”
    #GET answer
    #IF answer is no
        #BREAK
    #END IF
#END WHILE
