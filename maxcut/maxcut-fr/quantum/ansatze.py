# -*- coding: utf-8 -*-

"""
Author          : Ntwali Bashige
Copyright       : Copyright 2019 - Ntwali Bashige
License         : MIT
Version         : 0.0.1
Author          : Ntwali Bashige
Email           : ntwali.bashige@gmail.com
"""

from pyquil.quil import Program
from pyquil.gates import *


def RxCnot(params, wires, depth):
    prog = Program()
    length = len(params) - 1

    while depth > 0:
        index = 0
        while index <= length:
            prog.inst(RY(params[index], index))
            index = index + 1

        index = 0
        while index < length:
            prog.inst(CNOT(index, index + 1))
            index = index + 1

        depth = depth - 1

    for j in range(len(wires)):
        prog.inst(RY(params[0], 0))

    return prog


def RyCnot(params, wires, depth):
    prog = Program()
    length = len(params) - 1

    while depth > 0:
        index = 0
        while index <= length:
            prog.inst(RY(params[index], index))
            index = index + 1

        index = 0
        while index < length:
            prog.inst(CNOT(index, index + 1))
            index = index + 1

        depth = depth - 1

    for j in range(len(wires)):
        prog.inst(RY(params[0], 0))

    return prog
