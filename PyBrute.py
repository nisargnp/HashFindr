from __future__ import print_function

import os
import sys

import itertools
import hashlib
import time

import click

@click.command()
@click.option('-h', '--hash_needed', help='The hash to find.', prompt=True)
@click.option('-l', '--hash_location', type=click.Choice(['start', 'end', 'contain']), \
    help='The location of the hash.', prompt=True)
@click.option('-t', '--hash_type', type=click.Choice(['md5', 'sha1', 'sha256']), \
    help='Type of hash to generate.', prompt=True)
@click.option('-c', '--charset', help='Input charset.')
@click.option('-n', '--num', type=int, help='Number of passwords to find before program stops.')
def main(hash_needed, hash_location, hash_type, charset, num):

    print('')

    if hash_location is None:
        hash_location = 'start'

    if charset is None:
        charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"$%&/()=?`\''

    if num is None:
        num = 1

    if os.path.isfile(hash_needed):
        with open(hash_needed) as file:
            hash_needed = file.read()

    if os.path.isfile(hash_location):
        with open(hash_location) as file:
            hash_location = file.read()

    if os.path.isfile(charset):
        with open(charset) as file:
            charset = file.read()

    find_hash(hash_needed, hash_location, hash_type, charset, num)


def find_hash(hash_needed, hash_location, hash_type, charset, num_needed):

    # set needed hash
    hash_needed = hash_needed.lower()

    # getting the start time
    start_time = time.time()

    # set loop variables
    temp_hash = ''
    temp_pass = ''
    length = 0
    num_found = 0

    # loop until a valid password is found
    while True:

        length += 1

        # iterate through all permutations of the charset
        for temp_pass in itertools.product(charset, repeat=length):

            line = ''.join(temp_pass).encode('utf-8')

            # calculate the hash
            temp_hash = ''
            if hash_type == 'md5':
                temp_hash = hashlib.md5(line).hexdigest()
            elif hash_type == 'sha1':
                temp_hash = hashlib.sha1(line).hexdigest()
            elif temp_hash == 'sha256':
                temp_hash = hashlib.sha256(line).hexdigest()

            # determine is hash is correct
            correct = False
            if hash_location == 'start':
                correct = temp_hash.startswith(hash_needed)
            elif hash_location == 'end':
                correct = temp_hash.endswith(hash_needed)
            elif hash_location == 'contain':
                correct = hash_needed in temp_hash

            if correct:
                num_found += 1

                print('time:', str(time.time() - start_time))
                print('pass:', ''.join(temp_pass))
                print('hash:', temp_hash)
                print('')

            # exit once desired num of passwords are found
            if num_found >= num_needed:
                sys.exit(0)

if __name__ == '__main__':
    main()
