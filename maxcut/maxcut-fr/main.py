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

from pennylane import numpy as np
from quantum.ansatze import RxCnot, RyCnot
from quantum.hamiltonian import MaxCutHamiltonian
from classical.nelder import NelderMeadOptimizer


def main():
    # The cost function that is to be evaluated on the quantum computer and which returns to us the expectation value of the Hamiltonian
    def cost(maxcut):
        ham = MaxCutHamiltonian(
            ansatz = RyCnot,
            wires = [0, 1, 2, 3],
            depth = 2,
            weights = {
                (0, 1): 1,
                (1, 2): 1,
                (1, 3): 1,
                (2, 3): 1
            }
        )
        return ham.expectation()

    # Find the lowest eigenvalue through classical gradient descent minimization
    # optimizer = GradientOptimizer(cost, 0.01)
    # eigv = optimizer.optimize(params = [0.5], steps = 100)

    # Find the lowest eigenvalue through classical Nelder-Mead minimization
    optimizer = NelderMeadOptimizer(cost)
    eigv = optimizer.optimize(params = [0])
    print("The maximum cut of the given graph is: " + str(eigv))


if __name__ == "__main__":
    main()
