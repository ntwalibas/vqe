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

from quantum.hamiltonian import MaxCutHamiltonian
from classical.nelder import NelderMeadOptimizer
from classical.gradient import GradientOptimizer


def main():
    # The cost function that is to be evaluated on the quantum computer and which returns to us the expectation value of the Hamiltonian
    def cost(maxcut):
        ham = MaxCutHamiltonian(
            wires = 4,
            weights = {
                (0, 1): 1,
                (0, 3): 1,
                (1, 2): 1,
                (1, 3): 1,
                (2, 3): 1
            }
        )
        return ham.expectation()

    # Find the lowest eigenvalue through classical gradient descent minimization
    optimizer = GradientOptimizer(cost, 0.01)
    eigv = optimizer.optimize(params = [0.5], steps = 100)

    # Find the lowest eigenvalue through classical Nelder-Mead minimization
    # optimizer = NelderMeadOptimizer(cost)
    # eigv = optimizer.optimize(params = [0])
    print("The maximum cut of the given graph is: " + str(eigv))


if __name__ == "__main__":
    main()
