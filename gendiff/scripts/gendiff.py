#!/usr/bin/env python3

import argparse
from gendiff.diff import gen_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        metavar='first_file',
        type=str,
        help='path to the first file to compare'
    )
    parser.add_argument(
        'second_file',
        metavar='second_file',
        type=str,
        help='path to the second file to compare'
    )
    parser.add_argument(
        '-f',
        '--format',
        metavar='FORMAT',
        type=str,
        default='stylish',
        help='set format of output (default: "stylish")'
    )

    diff = gen_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    print(diff)


if __name__ == '__main__':
    main()
