#!/usr/bin/env python

import sys
import random
import string
import argparse

#
#         _ _     _               _     _     
#    __ _(_) |__ | |__   ___ _ __(_)___| |__  
#   / _` | | '_ \| '_ \ / _ \ '__| / __| '_ \ 
#  | (_| | | |_) | |_) |  __/ |  | \__ \ | | |
#  \__, |_|_.__/|_.__/ \___|_|  |_|___/_| |_|
#  |___/
#
# Author: Jared Marshall Hall
# License: MIT License
# Contact: hall.jared.m@gmail.com
# Created: March 27, 2016
# Purpose: Generate gibberish text as a text wall or cut into
#   paragraphs with an optional specified line length.
# Why: I wanted a text generator for when I'm building a website
#   or doing anything else where I may need text placeholders.
#   I realise that most people would make it so it uses an English
#   dictionary instead of using randomly generated text. The reason I
#   didn't do that is because I wanted to have roughly the format of
#   English without the words.. why? because it's distracting for me.
#   When I'm working against a deadline I want to work as efficiently
#   as possible with as little distraction as possible.
# Installation: Can be added to usr/local/bin
#     like so (for calling straight from the command line regardless of current folder):
#         cd /usr/local/bin (command below must be called from within this folder)
#         sudo ln -s <path_to_gibberish/gibberish>  
#
#     Donate Bitcoin:
#     1AYk yF8P 1k19 NpAA xxEm WBa6 rp7g wgHz dr
#
#     Donate Dogecoin:
#     DBGX4dwhD7SHhfcgzKjSZ2yJDhruAPgPUP
#
#     Donate via Paypal:
#     http://bit.ly/1klxN1M
#

argc = len(sys.argv)

# set up parser + args
parser = argparse.ArgumentParser()
parser.add_argument('wordcount', help='number of words in gibberish', type=int)
parser.add_argument('-p', '--paragraphs', help='usage: gibberish <wordcount> -p 49 \nBreak gibberish into paragraphs, default is between 4-7 sentences per paragraph. Numbers should be entered with no comma (4-7 or 4,7 should be entered as 47)', nargs='?', const=47, type=int, required=False)
parser.add_argument('-w', '--width', help='specify number of words per line', nargs='?', type=int, required=False)
args = vars(parser.parse_args())

# grab the gibberish word count
word_count = sys.argv[1]

# check and see if 'paragraphs' flag is activiated
if (args['paragraphs']):
    paragraph_choices = list(str(args['paragraphs']))
    paragraph_length = random.choice(range(int(paragraph_choices[0]), (int(paragraph_choices[1]) + 1)))
    # first indent
    sys.stdout.write("\t")
else:
    paragraph_length = None

# check and see if the 'width' flag is activated
if (args['width']):
    line_width = args['width']
else:
    line_width = None
    
# create a function to generate a gibberish word
# more word types could be added
# ** made with the English language in mind, definitely not comprehensive
def generateWord():
    # pick the word type via a random number 
    word_type = random.choice(range(1,10))
    # if the number 1 is drawn (smaller chance) let the word be from 1-3 characters (I, am, the, etc.)
    if (word_type == 1):
        word_length = random.choice(range(1,4))
        generated_word = ''.join(random.choice(string.lowercase) for x in range(word_length))
    # else let the word be a standard word between 5-13 characters
    else:
        word_length = random.choice(range(5, 14))
        generated_word = ''.join(random.choice(string.lowercase) for x in range(word_length))
    return generated_word

# grab a starting sentence length via a number number between 15 and 20
sentence_length = random.choice(range(15,21))
# initiate the sentence and word_in_sentence counters 0
sentence_counter = 0
word_in_sentence_counter = 0
word_counter = 0

# loop through the number of words specified when starting the program
#   use enumerate to get a loopcounter (i prefer old fashion counters
#   to this method) for me using enumerate can get confusing, especially when
#   you need to reset the counter
for word, loopcounter in enumerate(range(int(word_count))):
    if (word_counter % line_width == 0) and (word_counter != 0):
        sys.stdout.write('\n')
    # check to see if paragraph_length is null 
    if (paragraph_length != None):
        # if the sentence counter has reached the limit for paragraph length
        #   and it's not at the beginning of the paragraph
        if (sentence_counter % paragraph_length == 0) and (sentence_counter != 0) and (word_counter != 0):
            # add a new line
            sys.stdout.write("\n")
            # indent
            sys.stdout.write('\t')
            # grab another random paragraph_length (so they aren't all the
            #   same)
            paragraph_length = random.choice(range(int(paragraph_choices[0]), (int(paragraph_choices[1]) + 1)))
            # add one to the sentence_counter 
            sentence_counter = 0
        # if it isn't the end of the paragraph
        else:
            # generate a new word
            gibberish_word = generateWord()
            # if the last word in the sentence has been reached
            if ((word_in_sentence_counter + 1) % sentence_length == 0):
                # print the last line of the sentence with a period and 2 spaces
                sys.stdout.write(gibberish_word + ".  ")
                word_counter += 1
                word_in_sentence_counter = 0
                sentence_length = random.choice(range(15,21))
                # if its the end of a sentence
                sentence_counter+=1
            # if it's the end of the gibberish generation
            elif ((int(word_counter)) == int(word_count)):
                sys.stdout.write(gibberish_word + ".")
                word_in_sentence_counter += 1
                word_counter += 1
            # just print the gibberish word with a space
            else:
                sys.stdout.write(gibberish_word + " ")
                word_in_sentence_counter += 1
                word_counter += 1
    else:
        gibberish_word = generateWord()
        # print the last word of the sentence with a period and 2 spaces
        if ((word_in_sentence_counter + 1) % sentence_length == 0):
            sys.stdout.write(gibberish_word + ".  ")
            word_in_sentence_counter = 0
            word_counter += 1
            sentence_length = random.choice(range(15,21))
        # if it's the end of gibberish generation
        elif ((int(word_counter + 1)) == int(word_count)):
            sys.stdout.write(gibberish_word + ".")
            word_in_sentence_counter += 1
            word_counter += 1
        else:
            sys.stdout.write(gibberish_word + " ")
            word_in_sentence_counter += 1
            word_counter += 1
