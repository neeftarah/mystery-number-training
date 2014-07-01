<?php

// Detect OS and define the good clean sreen function
if(substr(PHP_OS, 0, 3) == "WIN") define('CLS', 'cls');
else  define('CLS', 'clear');

mb_internal_encoding("utf-8");

define('SOLO', 1);
define('MULTI', 2);

$continue = true;
$time     = 0;
$langages = array();
$lang     = array();
$turn     = 0;
$score    = 0;


// 1. Show splash sreen for 3s
system(CLS);
echo "/******************************************************************************\\" . PHP_EOL;
echo "|                                  WELCOME TO                                  |" . PHP_EOL;
echo "|                                MYSTERY NUMBER                                |" . PHP_EOL;
echo "\******************************************************************************/" . PHP_EOL;

sleep(1);

// 2. Select a langage
do {
   system(CLS);

   $i = 0;
   foreach(glob('../locales/*.txt') as $file) {
      $i++;

      $langages[$i] = $file;

      $fp = fopen($file, 'r');
      echo $i . '. ' . fgets($fp);
      fclose($fp);
   }
   $input = fgets(STDIN);
} while((int) $input != $input || $input < 1 || $input > sizeof($langages));

$lang = file($langages[(int) $input]);

// 3. Select game mode
do {
   system(CLS);
   echo $lang[1];                                              // Please sélect the game mode
   echo '1. ' . $lang[2];                                      // Solo game
   echo '2. ' . $lang[3];                                      // Two players
   $input = fgets(STDIN);
} while(!in_array((int) $input, array(SOLO, MULTI)));

$mode = (int) $input;

// 4. Players name...
if(SOLO == $mode) {
   system(CLS);
   echo $lang[9];
   $player_name = trim(fgets(STDIN), PHP_EOL);
} else {
   system(CLS);
   echo sprintf($lang[10], 1);
   $player[1]['name'] = fgets(STDIN);

   echo PHP_EOL . sprintf($lang[10], 2);
   $player[2]['name'] = fgets(STDIN);
}

// 5. Select a difficulty...
do {
   system(CLS);
   echo $lang[4];                                           // Please sélect a difficulty
   echo '1. ' . sprintf($lang[5], 1, 100);                  // From %d to %d
   echo '2. ' . sprintf($lang[5], 1, 1000);                 // From %d to %d
   echo '3. ' . sprintf($lang[5], 1, 10000);                // From %d to %d
   echo '4. ' . $lang[6];                                   // Personalized difficulty
   $input = fgets(STDIN);
} while((int) $input != $input || $input < 1 || $input > 4);

$difficulty = (int) $input;

// Ask for the maximum number for the personalized difficulty
if(4 == $difficulty) {
   do {
      system(CLS);
      echo $lang[7];                                        // Please, enter the maximum number
      $input = fgets(STDIN);
   } while((int) $input != $input);

   $max = (int) $input;

// Set standard maximum number
} else {
   switch ($difficulty) {
      case 1:
         $max = 100;
         break;
      case 2:
         $max = 1000;
         break;
      case 3:
         $max = 10000;
         break;
   }
}

// Start game loop
while($continue) {
   $turn   = (1 == $turn && MULTI == $mode) ? 2 : 1;

   // MULTI mode, enter the mystery number
   if(MULTI == $mode) {
      do {
         system(CLS);
         $player_name   = trim((1 == $turn) ? ucfirst($player[1]['name']) : ucfirst($player[2]['name']), PHP_EOL);
         $opposant_name = trim((1 == $turn) ? ucfirst($player[2]['name']) : ucfirst($player[1]['name']), PHP_EOL);

         // Player 2 enter the mystery number please. Player 1, no cheating, don't look !
         echo sprintf($lang[8], $opposant_name, $player_name);

         $input = fgets(STDIN);

         // You must enter a smaller number ! This one is greater than the maximum difficulty
         if((int) $input > $max) {
            echo trim($lang[20]) . '('.$max.')';
            sleep(3);
         }
      } while((int) $input != $input || $input < 1 || (int) $input > $max);

      $random = (int) $input;
   } else {
      $random      = mt_rand(0, $max);
   }

   $player_name   = trim($player_name);
   $opposant_name = trim($opposant_name);

   system(CLS);
   if(SOLO == $mode) {
      echo sprintf($lang[15], $player_name, $max);             // Player, you may find a number between 0 and max
   } else {
      echo sprintf($lang[16], $player_name, $opposant_name);   // Player 1, you may find Player's 2 number
   }

   // 6. Game
   $start_time    = time();
   $attempt_count = 0;
   do {
      $attempt_count++;
      echo trim($lang[17], PHP_EOL) . ' ';                      // Please, enter a number
      $input = fgets(STDIN);
      if((int) $input < $random) {
         echo $lang[11] . PHP_EOL;
      } elseif((int) $input > $random) {
         echo $lang[12] . PHP_EOL;
      }
   } while((int) $input != $random);

   $spend_time    = time() - $start_time;
   system(CLS);
   echo sprintf($lang[13], $random, $attempt_count, floor($spend_time / 60), $spend_time % 60) . PHP_EOL;
   sleep(3);

   // Score calculation
   $score = 2 * $max - $attempt_count - $spend_time;

   if(MULTI == $mode) {
      $player[$turn]['score']      = $score;
      $player[$turn]['attemps']    = $attempt_count;
      $player[$turn]['spend_time'] = $spend_time;
   }

   // 7. Scores
   if(SOLO == $mode || 2 == $turn) {
      // Prepare Score tab strings
      $title    = mb_str_pad(trim($lang[22], PHP_EOL), 76, ' ', STR_PAD_BOTH);
      $names    = mb_str_pad(trim($lang[23], PHP_EOL), 17, ' ', STR_PAD_BOTH);
      $attempts = mb_str_pad(trim($lang[24], PHP_EOL), 10, ' ', STR_PAD_BOTH);
      $time     = mb_str_pad(trim($lang[25], PHP_EOL), 12, ' ', STR_PAD_BOTH);
      $score    = mb_str_pad(trim($lang[26], PHP_EOL), 15, ' ', STR_PAD_BOTH);
      $date     = mb_str_pad(trim($lang[27], PHP_EOL), 10, ' ', STR_PAD_BOTH);

      if(MULTI == $mode) {

         echo PHP_EOL . PHP_EOL;
         echo "/******************************************************************************\\" . PHP_EOL;
         echo "| $title |" . PHP_EOL;
         echo "|------------------------------------------------------------------------------|" . PHP_EOL;
         echo "| $names | $attempts | $time | $score | $date |" . PHP_EOL;
         echo "|------------------------------------------------------------------------------|" . PHP_EOL;

         // Player 1
         echo '| ' . mb_str_pad(trim(ucfirst($player[1]['name'])), 17, ' ', STR_PAD_RIGHT)
              . ' | ' . mb_str_pad($player[1]['attemps'], 10, ' ', STR_PAD_BOTH)
              . ' | ' . mb_str_pad(floor($player[1]['spend_time'] / 60) . ' min '
                      . $player[1]['spend_time'] % 60 . ' s', 12, ' ', STR_PAD_BOTH)
              . ' | ' . mb_str_pad($player[1]['score'], 15, ' ', STR_PAD_BOTH)
              . ' | ' . mb_str_pad(date('Y-m-d'), 10, ' ', STR_PAD_BOTH) . ' |' . PHP_EOL;
         // Player 2
         echo '| ' . mb_str_pad(trim(ucfirst($player[2]['name'])), 17, ' ', STR_PAD_RIGHT)
              . ' | ' . mb_str_pad($player[2]['attemps'], 10, ' ', STR_PAD_BOTH)
              . ' | ' . mb_str_pad(floor($player[2]['spend_time'] / 60) . ' min '
                      . $player[2]['spend_time'] % 60 . ' s', 12, ' ', STR_PAD_BOTH)
              . ' | ' . mb_str_pad($player[2]['score'], 15, ' ', STR_PAD_BOTH)
              . ' | ' . mb_str_pad(date('Y-m-d'), 10, ' ', STR_PAD_BOTH) . ' |' . PHP_EOL;

         echo "|------------------------------------------------------------------------------|" . PHP_EOL;
         if($player[1]['score'] == $player[2]['score']) {
            echo '| ' . mb_str_pad(trim($lang[21]), 76, ' ', STR_PAD_BOTH) . ' |' . PHP_EOL;
         } else {
            $winner = ($player[1]['score'] > $player[2]['score']) ? $player[1]['name'] : $player[2]['name'];
            $winner = mb_strtoupper(trim(sprintf($lang[19], trim($winner, PHP_EOL), PHP_EOL)));
            echo '| ' . mb_str_pad($winner, 76, ' ', STR_PAD_BOTH) . ' |' . PHP_EOL;
         }
         echo "\******************************************************************************/" . PHP_EOL;
         echo PHP_EOL . PHP_EOL;

      } else {
         // Get previous best scores
         $best_scores = array();
         if(is_file('scores.txt')) {
            $fp = fopen('scores.txt', 'r');
            while($line = fgets($fp)) {
               $best_scores[] = explode('|', trim($line, PHP_EOL));
            }
            fclose($fp);
         } else {
            $best_scores = array();
         }

         // Add player score
         $best_scores[] = array(
            $player_name,
            $attempt_count,
            floor($spend_time / 60) .' min ' . $spend_time % 60 . ' s',
            $score,
            date('Y-m-d')
         );

         // Order Array
         for($i = 0; $i < sizeof($best_scores) - 1 ; $i++) {
            for($j = $i+1; $j < sizeof($best_scores) ; $j++) {
               if($best_scores[$j][3] > $best_scores[$i][3]) {
                  $tmp_tab = $best_scores[$i];
                  $best_scores[$i] = $best_scores[$j];
                  $best_scores[$j] = $tmp_tab;
               }
            }
         }

         // Delete the last line if more than 10 lines
         if(sizeof($best_scores) > 10) {
            array_pop($best_scores);
         }

         // Show best scores
         echo PHP_EOL . PHP_EOL;
         echo "/******************************************************************************\\" . PHP_EOL;
         echo "| $title |" . PHP_EOL;
         echo "|------------------------------------------------------------------------------|" . PHP_EOL;
         echo "| $names | $attempts | $time | $score | $date |" . PHP_EOL;
         echo "|------------------------------------------------------------------------------|" . PHP_EOL;
         foreach($best_scores as $player_datas) {
            $player_name     = mb_str_pad($player_datas[0], 17, ' ', STR_PAD_RIGHT);
            $player_attempts = mb_str_pad($player_datas[1], 10, ' ', STR_PAD_BOTH);
            $player_time     = mb_str_pad($player_datas[2], 12, ' ', STR_PAD_BOTH);
            $player_score    = mb_str_pad($player_datas[3], 15, ' ', STR_PAD_BOTH);
            $player_date     = mb_str_pad($player_datas[4], 10, ' ', STR_PAD_BOTH);
            echo "| $player_name | $player_attempts | $player_time | $player_score | $player_date |" . PHP_EOL;
         }

         echo "\******************************************************************************/" . PHP_EOL;
         echo PHP_EOL . PHP_EOL;

         // Save best scores
         $fp = fopen('scores.txt', 'w');
         foreach($best_scores as $player_datas) {
            fputs($fp, implode('|', $player_datas) . PHP_EOL);
         }
         fclose($fp);
      }

      // 8. New game ?
      echo $lang[14];                                             // Do you want to replay ?
      $input = fgets(STDIN);
      if(strtoupper(trim($input, PHP_EOL)) == 'N') {
         $continue = false;
      }
      system(CLS);
   }
}

function mb_str_pad($input, $pad_length, $pad_string, $pad_style, $encoding = "UTF-8") {
   return str_pad($input, strlen($input) - mb_strlen($input, $encoding) + $pad_length, $pad_string, $pad_style);
}
