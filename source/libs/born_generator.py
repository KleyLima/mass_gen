# -*- coding: utf-8 -*-

from random import randrange as rd


class BornGen:
    @classmethod
    def __init__(cls):
        cls.dt_nasc = '{}-{}-{}'.format(rd(1950, 2010), rd(1, 12), rd(1, 28))


if __name__ == '__main__':
    print(BornGen().dt_nasc)
