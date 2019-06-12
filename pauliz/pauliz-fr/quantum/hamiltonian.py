# -*- coding: utf-8 -*-

"""
Author          : Ntwali Bashige
Copyright       : Copyright 2019 - Ntwali Bashige
License         : MIT
Version         : 0.0.1
Author          : Ntwali Bashige
Email           : ntwali.bashige@gmail.com
"""

from pyquil.paulis import PauliSum, PauliTerm
from grove.pyvqe.vqe import VQE
import pyquil.api as api


class PZHamiltonian(object):
    def __init__(self, ansatz):
        self.ansatz = ansatz
        self.qvm = api.QVMConnection()


    def expectation(self, params):
        def _expectation(_params):
            exp = PauliSum([PauliTerm.from_list([('Z', 0)])])
            return VQE.expectation(self.ansatz(_params[0], 0), exp, None, self.qvm)

        return _expectation(params)
