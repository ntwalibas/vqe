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

class PZHamiltonian(object):
    def __init__(self, ansatz):
        self.dev = pl.device("default.qubit", wires = 1)
        self.ansatz = ansatz


    def expectation(self, params):
        @pl.qnode(self.dev)
        def _expectation(_params):
            self.ansatz(_params[0], 0)
            return pl.expval.PauliZ(0)

        return _expectation(params)
