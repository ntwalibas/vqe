# -*- coding: utf-8 -*-

"""
Author          : Ntwali Bashige
Copyright       : Copyright 2019 - Ntwali Bashige
License         : MIT
Version         : 0.0.1
Author          : Ntwali Bashige
Email           : ntwali.bashige@gmail.com
"""

import pennylane as pl


def Rx(param, wire):
    pl.RX(param, wires = [wire])


def Ry(param, wire):
    pl.RY(param, wires = [wire])


def Rz(param, wire):
    pl.RZ(param, wires = [wire])


def Had(param, wire):
    pl.Hadamard(wires = [wire])


def Phase(param, wire):
    pl.Rot(0.0, 0.0, 2.0 * param, wires = [wire])
