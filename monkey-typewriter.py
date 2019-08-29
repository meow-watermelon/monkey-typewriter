#!/usr/bin/env python3

import argparse
import math
import multiprocessing
import random
import string
import sys
import time

def rand_word(length):
    charset = list(string.ascii_lowercase)
    rand_list = []

    for i in range(length):
        rand_list.append(random.choice(charset))

    rand_str = ''.join(rand_list)

    return rand_str

def match_word(word):
    word_length = len(word)
    lower_word = word.lower()
    start_time = time.time()
    counter = 0

    while True:
        counter = counter + 1
        gen_rand_word = rand_word(word_length)
        if lower_word == gen_rand_word:
            end_time = time.time()
            print('%s:%f:%d' %(lower_word, end_time - start_time, counter))
            break

def get_words_list(filename):
    words_list = []

    try:
        with open(filename, 'r') as f:
            words_list = f.read().rstrip().split(' ')
    except:
        words_list = []

    return words_list

if __name__ == '__main__':
    '''initialize variables'''
    i = 0

    '''set up arguments'''
    parser = argparse.ArgumentParser(description='Small Monkey Typewriter', epilog='Please make sure there is no numbers or symbols in the input text file.\nOutput: <word>:<time_consumed>:<counters>')
    parser.add_argument('-f', '--file', type=str, required=True, help='input text filename')
    parser.add_argument('-w', '--worker', type=int, required=False, help='number of parallel workers (default: 5)')
    args = parser.parse_args()

    if args.worker:
        workers = args.worker
    else:
        workers = 5

    '''generate words list from the input text file'''
    words_list = get_words_list(args.file)
    if len(words_list) == 0:
        msg = 'ERROR: No valid words are extracted.'
        print(msg)
        sys.exit(1)

    '''run'''
    rounds = math.ceil(len(words_list) / workers)
    if rounds == 1:
        run_list = words_list
        msg = '>>> Running Batch [0]'
        print(msg)
        with multiprocessing.Pool(processes=len(words_list)) as pool:
            pool.map(match_word, run_list)
            pool.terminate()
            pool.join()
    else:
        for n in range(rounds):
            run_list = words_list[i:i+workers]
            i += workers
            msg = '>>> Running Batch [%d]' %(n)
            print(msg)
            with multiprocessing.Pool(processes=workers) as pool:
                pool.map(match_word, run_list)
                pool.terminate()
                pool.join()
