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


def Rx(param, wire):
    prog = Program()
    prog.inst(RX(param, wire))
    return prog


def Ry(param, wire):
    prog = Program()
    prog.inst(RY(param, wire))
    return prog


def Rz(param, wire):
    prog = Program()
    prog.inst(RZ(param, wire))
    return prog


def Had(param, wire):
    prog = Program()
    prog.inst(H(wire))
    return prog


def Phase(param, wire):
    prog = Program()
    prog.inst(PHASE(param, wire))
    return prog
