#!/usr/bin/env python3

from sys import stdin

from utilities import dual, parse


def main():
    for name, faces in parse(stdin.read()):
        assert faces == dual(dual(faces))

        name += '_dual'
        faces = dual(faces)

        print(name, faces, sep='=', end='\n\n')


if __name__ == '__main__':
    main()
