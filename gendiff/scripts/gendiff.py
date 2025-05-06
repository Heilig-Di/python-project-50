import argparse

from gendiff.gendiff_compare import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two '
                                 'configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish',
        help='set format of output: stylish (default), plain, json'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
