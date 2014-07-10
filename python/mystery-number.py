#! /usr/local/bin/python2.7
# -*- coding:Utf-8 -*

import math
import random
import os
import time
import datetime
import glob

SOLO          = 1
MULTI         = 2

continue_game = True
langages      = []
lang          = []
turn          = 0
score         = 0

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

# 1. Show splash screen for 1s
clearscreen()
print "/******************************************************************************\\"
print "|                                  WELCOME TO                                  |"
print "|                                MYSTERY NUMBER                                |"
print "\******************************************************************************/"

time.sleep(1)

# 2. Select a language
input_text = 0
while input_text < 1 or input_text > i :
    clearscreen()
    i = 0
    for lang_file in glob.iglob('../locales/*.txt') :
        i = i + 1
        langages.append(lang_file)
        fp = open(lang_file, 'r')
        print str(i) + '. ' + fp.readline().strip()
        fp.close()
    try:
        input_text = int(raw_input())
    except ValueError:
        print('\nPLease input a valid integer')
        time.sleep(1)

fp = open(langages[input_text - 1], 'r')
lang = fp.readlines()
fp.close()

# 3. Select game mode
input_text = 0
while input_text != 1 and input_text != 2 :
    clearscreen()
    print lang[1].strip()                                          # Please select the game mode
    print '1. ' + lang[2].strip()                                  # Solo game
    print '2. ' + lang[3].strip()                                  # Two players
    try:
        input_text = int(raw_input())
    except ValueError:
        print lang[28].strip()
        time.sleep(1)

mode = input_text

# 4. Players name...
if (SOLO == mode) :
    clearscreen()
    print lang[9].strip()

    try:
        player_name = raw_input()
    except ValueError:
        print lang[29].strip()
        time.sleep(1)

    print player_name
else :
    clearscreen()

    player = {}
    try:
        player[1] = {}
        player[1]['name'] = raw_input(lang[10].strip() % (1))
    except ValueError:
        print lang[29].strip()
        time.sleep(1)

    try:
        player[2] = {}
        player[2]['name'] = raw_input(lang[10].strip() % (2))
    except ValueError:
        print lang[29].strip()
        time.sleep(1)

# 5. Select a difficulty...
input_text = 0
while input_text not in [1, 2, 3, 4] :
    clearscreen()
    print lang[4]                                                   # Please select a difficulty
    print '1. ', lang[5].strip() % (1, 100)                        # From %d to %d
    print '2. ', lang[5].strip() % (1, 1000)                       # From %d to %d
    print '3. ', lang[5].strip() % (1, 10000)                      # From %d to %d
    print '4. ', lang[6].strip()                                   # Personalized difficulty
    try:
        input_text = int(raw_input())
    except ValueError:
        print lang[28].strip()
        time.sleep(1)
difficulty = input_text

# Ask for the maximum number for the personalized difficulty
if 4 == difficulty :
    input_text = 0
    while input_text < 1 :
        clearscreen()
        print lang[7].strip()                                       # Please, enter the maximum number
        try:
            input_text = int(raw_input())
        except ValueError:
            print lang[28].strip()
            time.sleep(1)

    maximum = input_text

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
    if 1 == turn and MULTI == mode :
        turn = 2
    else :
        turn = 1

    # MULTI mode, enter the mystery number
    if (MULTI == mode) :
        input_text = 0
        while input_text < 1 or input_text > maximum :
            clearscreen()
            if 1 == turn :
                player_name   = player[1]['name'].capitalize()
                opposant_name = player[2]['name'].capitalize()
            else :
                player_name   = player[2]['name'].capitalize()
                opposant_name = player[1]['name'].capitalize()

            # Player 2 enter the mystery number please. Player 1, no cheating, don't look !
            print lang[8] % (opposant_name, player_name)

            try:
                input_text = int(raw_input())
            except ValueError:
                print lang[28].strip()
                time.sleep(1)

            # You must enter a smaller number ! This one is greater than the maximum difficulty
            if input_text > maximum :
                print lang[20].strip(),  ' (',  maximum,  ')'
                time.sleep(3)
        mystery_number = input_text
    else :
        mystery_number = random.randint(0, maximum)

    clearscreen()
    if (SOLO == mode) :
        print lang[15].strip() % (player_name, maximum)                 # Player, you may find a number between 0 and maximum
    else :
        print lang[16].strip() % (player_name, opposant_name)           # Player 1, you may find Player's 2 number


    # 6. Game
    start_time    = int(time.time())
    attempt_count = 0
    input_text    = 0
    while input_text != mystery_number :
        attempt_count = attempt_count + 1
        print lang[17].strip()                                          # Please, enter a number
        try:
            input_text = int(raw_input())
        except ValueError:
            print lang[28].strip()
            time.sleep(1)

        if input_text < mystery_number :
            print lang[11].strip()
        elif input_text > mystery_number :
            print lang[12].strip()

    spend_time    = int(time.time()) - start_time
    clearscreen()
    print lang[13].strip() % (mystery_number, attempt_count, math.floor(spend_time / 60), spend_time % 60)
    time.sleep(3)

    # Score calculation
    score = 2 * maximum - attempt_count - spend_time

    if (MULTI == mode) :
        player[turn]['score']      = score
        player[turn]['attemps']    = attempt_count
        player[turn]['spend_time'] = spend_time


    # 7. Scores
    if (SOLO == mode or 2 == turn) :
        if (MULTI == mode) :
            # Player 1 : attemps = x spend time = m min s s  score = Score 1
            print lang[18] % (player[1]['name'].capitalize(), player[1]['attemps'], math.floor(player[1]['spend_time'] / 60), player[1]['spend_time'] % 60, player[1]['score'])
            # Player 2 : attemps = x spend time = m min s s  score = Score 2
            print lang[18] % (player[2]['name'].capitalize(), player[2]['attemps'], math.floor(player[2]['spend_time'] / 60), player[2]['spend_time'] % 60, player[2]['score'])

            if (player[1]['score'] > player[2]['score']) :
                print lang[19].strip() % (player[1]['name'].capitalize())       # Player 1 win
            elif (player[2]['score'] > player[1]['score']) :
                print lang[19].strip() % (player[2]['name'].capitalize())       # Player 2 win
            else :
                print lang[21].strip()                                          # Match null

        # Get previous best scores
        best_scores = []
        if os.path.isfile('scores.txt') :
            fp = open('scores.txt', 'r')
            lines = fp.readlines()
            for line in lines  :
                best_scores.append( line.strip().split('|'))
            fp.close()

        # Add pplayer score if  it's a solo game
        today = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
        if (SOLO == mode) :
            best_scores.append([player_name, attempt_count, str(int(math.floor(spend_time / 60))) + 'min ' + str(spend_time % 60) + 's', score, today])


        # Order Array
        for i in range(0, len(best_scores) - 1):
            for j in range(i + 1, len(best_scores)) :
                if (best_scores[j][3] > best_scores[i][3]) :
                    tmp_tab        = best_scores[i]
                    best_scores[i] = best_scores[j]
                    best_scores[j] = tmp_tab

        # Delete the last line if  more than 10 lines
        if len(best_scores) > 10 :
            best_scores.pop()


        # Show best scores
        title    = lang[22].strip().center(76)
        names    = lang[23].strip().center(17)
        attempts = lang[24].strip().center(10)
        time_str = lang[25].strip().center(10)
        score    = lang[26].strip().center(10)
        date     = lang[27].strip().center(17)

        print "/******************************************************************************\\"
        print "|", title, "|"
        print "|------------------------------------------------------------------------------|"
        print "|", names, "|", attempts, "|", time_str, "|", score, "|", date, "|"
        print "|------------------------------------------------------------------------------|"
        for player_datas in best_scores :
            name_of_player     = player_datas[0]
            name_of_player     = name_of_player.decode('UTF-8').ljust(17)
            attempts_of_player = str(player_datas[1]).center(10)
            time_of_player     = str(player_datas[2]).center(10)
            score_of_player    = str(player_datas[3]).center(10)
            date_of_player     = str(player_datas[4]).center(17)
            print "|", name_of_player, "|", attempts_of_player, "|", time_of_player, "|", score_of_player, "|", date_of_player, "|"


        print "\******************************************************************************/"

        # Save best scores if  it's a solo game
        if SOLO == mode :
            fp = open('scores.txt', 'w')

            for player_datas in best_scores :
                string = '|'.join(str(data) for data in player_datas)
                fp.write(string + os.linesep)

        fp.close()


        # 8. New game ?
        valid_input = False
        while not valid_input :
            try:
                print lang[14].strip()
                input_text  = raw_input()                       # Do you want to replay ?
                valid_input = True
            except ValueError:
                print lang[31].strip()
                valid_input = False
                time.sleep(1)


        if input_text.strip().upper() == 'N' :
            continue_game = False

        clearscreen()
