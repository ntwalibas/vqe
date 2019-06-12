#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author          : Ntwali Bashige
Copyright       : Copyright 2019 - Ntwali Bashige
License         : MIT
Version         : 0.0.1
Author          : Ntwali Bashige
Email           : ntwali.bashige@gmail.com
"""

from quantum.ansatze import Rx
from quantum.hamiltonian import PZHamiltonian
from classical.nelder import NelderMeadOptimizer


def main():
    # The cost function that is to be evaluated on the quantum computer and which returns to us the expectation value of the Hamiltonian
    def cost(params):
        ham = PZHamiltonian(Rx)
        return ham.expectation(params)

    # Find the lowest eigenvalue through classical Nelder-Mead minimization
    optimizer = NelderMeadOptimizer(cost)
    eigv = optimizer.optimize(params = [0.0])
    print("The ground state eigenvalue of the Pauli Z operator is: " + str(eigv))


if __name__ == "__main__":
    main()
