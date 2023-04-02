#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file', type=str, help='')
    parser.add_argument('second_file', metavar='second_file', type=str, help='')
    parser.add_argument('-f', '--format', metavar='FORMAT', type=str, default='stylish', help='Set format of output')
    args = parser.parse_args()

    # Do something with first_file, second_file and format...

if __name__ == '__main__':
    main()
