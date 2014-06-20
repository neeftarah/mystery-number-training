#! /usr/local/bin/python3.4
# -*- coding:Utf-8 -*

import math
import random
import os
import time
import glob

SOLO          = 1
MULTI         = 2

continue_game = true
time          = 0
langages      = []
lang          = []
turn          = 0
score         = 0


# 1. Show splash screen for 1s
clearscreen()
print "/******************************************************************************\\"
print "|                                  WELCOME TO                                  |"
print "|                                MYSTERY NUMBER                                |"
print "\******************************************************************************/"

time.sleep(1)

# 2. Select a language
input_text = 0
while input_text < 1 || input_text > i :
    clearscreen()
    i = 0
    for lang_file in glob.iglob('../locales/*.txt') :
        i++
        fp = open(lang_file, 'r')
        print i . '. ' . fp.readline()
        fp.close()

    input_text = int(input())
lang = langages[input_text].readlines()

# 3. Select game mode
input_text = 0
while input_text != 1 && input_text != 2 :
    clearscreen()
    print lang[1]                                              # Please select the game mode
    print '1. ' . lang[2]                                      # Solo game
    print '2. ' . lang[3]                                      # Two players
    input_text = int(input())
mode = input_text

# 4. Players name...
if (SOLO == mode) :
    clearscreen()
    print lang[9]
    player_name = input()
else :
    clearscreen()
    print lang[10] % (1)
    player[1]['name'] = input()

    print lang[10] % (2)
    player[2]['name'] = input()


# 5. Select a difficulty...
while input_text not in [1, 2, 3, 4] :
    clearscreen()
    print lang[4]                                           # Please select a difficulty
    print '1. ' . lang[5] % (1, 100)                        # From %d to %d
    print '2. ' . lang[5] % (1, 1000)                       # From %d to %d
    print '3. ' . lang[5] % (1, 10000)                      # From %d to %d
    print '4. ' . lang[6]                                   # Personalized difficulty
    input_text = int(input())
difficulty = input_text

# Ask for the maximum number for the personalized difficulty
if 4 == difficulty :
    while input_text < 1 :
        clearscreen()
        print lang[7]                                        # Please, enter the maximum number
        input_text = int(input())

   maximum = (int) input_text

# Set standard maximum number
else :
    if difficulty == 1 :
        maximum = 100
    elif difficulty == 2 :
        maximum = 1000
    elif difficulty == 3 :
        maximum = 10000

# Start game loop
while continue_game :
   turn   = (1 == turn && MULTI == mode) ? 2 : 1

    # MULTI mode, enter the mystery number
    if (MULTI == mode) :
        while input_text < 1 || input_text > maximum :
            clearscreen()
            if 1 == turn :
                player_name   = player[1]['name'].capitalize()
                opposant_name = player[2]['name'].capitalize()
            else :
                player_name   = player[2]['name'].capitalize()
                opposant_name = player[1]['name'].capitalize()

            # Player 2 enter the mystery number please. Player 1, no cheating, don't look !
            print lang[8] % (opposant_name, player_name)

            input_text = int(input())

            # You must enter a smaller number ! This one is greater than the maximum difficulty
            if input_text > maximum :
                print lang[20]
                time.sleep(3)
        mystery_number = input_text
    else :
        mystery_number = random.randint(0, maximum)


    clearscreen()
    if (SOLO == mode) :
        print lang[15] % (player_name, maximum)                 # Player, you may find a number between 0 and maximum
    else :
        print lang[16] % (player_name, opposant_name)           # Player 1, you may find Player's 2 number


    # 6. Game
    start_time    = int(time.time())
    attempt_count = 0
    while input_text != mystery_number :
        attempt_count++
        print lang[17]                                          # Please, enter a number
        input_text = int(input())

        if input_text < mystery_number :
            print lang[11]
        elif input_text > mystery_number :
            print lang[12]

    spend_time    = int(time.time()) - start_time
    clearscreen()
    print lang[13] % (mystery_number, attempt_count, math.floor(spend_time / 60), spend_time % 60)

    # Score calculation
    score = 2 * maximum - attempt_count - spend_time

    if (MULTI == mode) :
        player[turn]['score']      = score
        player[turn]['attemps']    = attempt_count
        player[turn]['spend_time'] = spend_time


    # 7. Scores
    if (SOLO == mode || 2 == turn) :
        if (MULTI == mode) :
            # Player 1 : attemps = x spend time = m min s s  score = Score 1
            print lang[18] % (player[1]['name'].capitalize(), player[1]['attemps'], math.floor(player[1]['spend_time'] / 60), player[1]['spend_time'] % 60, player[1]['score'])
            # Player 2 : attemps = x spend time = m min s s  score = Score 2
            print lang[18] % (player[2]['name'].capitalize(), player[2]['attemps'], math.floor(player[2]['spend_time'] / 60), player[2]['spend_time'] % 60, player[2]['score'])

            if (player[1]['score'] > player[2]['score']) :
                print lang[19] % (player[1]['name'].capitalize())       # Player 1 win
            elif (player[2]['score'] > player[1]['score']) :
                print lang[19] % (player[2]['name'].capitalize())       # Player 2 win
            else :
                print lang[21]                                          # Match null

        # Get previous best scores
        if (is_file('scores.txt')) :
            fp = open('scores.txt', 'r')
            while(line = fgets(fp)) :
                best_scores[] = explode('|', trim(line, ))
            fp.close()
        else :
            best_scores = array()
"""

      # Add pplayer score if  it's a solo game
      if (SOLO == mode) :
         best_scores[] = array(
            player_name,
            attempt_count,
            floor(spend_time / 60) .' min ' . spend_time % 60 . ' s',
            score,
            date('Y-m-d')
         )


      # Order Array
      for(i = 0 i < sizeof(best_scores) - 1  i++) :
         for(j = i+1 j < sizeof(best_scores)  j++) :
            if (best_scores[j][3] > best_scores[i][3]) :
               tmp_tab = best_scores[i]
               best_scores[i] = best_scores[j]
               best_scores[j] = tmp_tab




      # Delete the last line if  more than 10 lines
      if (sizeof(best_scores) > 10) :
         array_pop(best_scores)


      # Show best scores
      title    = str_pad(trim(lang[22], ), 76, ' ', STR_PAD_BOTH)
      names    = str_pad(trim(lang[23], ), 17, ' ', STR_PAD_BOTH)
      attempts = str_pad(trim(lang[24], ), 10, ' ', STR_PAD_BOTH)
      time     = str_pad(trim(lang[25], ), 10, ' ', STR_PAD_BOTH)
      score    = str_pad(trim(lang[26], ), 10, ' ', STR_PAD_BOTH)
      date     = str_pad(trim(lang[27], ), 17, ' ', STR_PAD_BOTH)

      print "/******************************************************************************\\"
      print "| title |"
      print "|------------------------------------------------------------------------------|"
      print "| names | attempts | time | score | date |"
      print "|------------------------------------------------------------------------------|"
      foreach(best_scores as player_datas) :
         player_name     = str_pad(player_datas[0], 17, ' ', STR_PAD_RIGHT)
         player_attempts = str_pad(player_datas[1], 10, ' ', STR_PAD_BOTH)
         player_time     = str_pad(player_datas[2], 10, ' ', STR_PAD_BOTH)
         player_score    = str_pad(player_datas[3], 10, ' ', STR_PAD_BOTH)
         player_date     = str_pad(player_datas[4], 17, ' ', STR_PAD_BOTH)
         print "| player_name | player_attempts | player_time | player_score | player_date |"


      print "\******************************************************************************/"

      # Save best scores if  it's a solo game
      if (SOLO == mode) :
         fp = fopen('scores.txt', 'w')
         foreach(best_scores as player_datas) :
            fputs(fp, implode('|', player_datas) . )

         fclose(fp)


      # 8. New game ?
      print lang[14]                                             # Do you want to replay ?
      input_text = fgets(STDIN)
      if (strtoupper(trim(input_text, )) == 'N') :
         continue_game = false

      clearscreen()

"""

# function to clear screen for each OS
def clearscreen(numlines=80):
   if  os.name == "posix":
      # Unix/Linux/MacOS/BSD/etc
      os.system('clear')
   elif  os.name in ("nt", "dos", "ce"):
      # DOS/Windows
      os.system('cls')
   else:
      # Fallback for other operating systems.
      print '\n' * numlines