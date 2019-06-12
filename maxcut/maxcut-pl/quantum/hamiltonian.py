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


class MaxCutHamiltonian(object):
    def __init__(self, **kwargs):
        self.dev = pl.device("default.qubit", wires = kwargs.pop("wires"))
        self.weights_map = kwargs.get("weights", None)

        if self.weights_map is None:
            raise ValueError("Expected the graph's edges 'weights' as part of the constructor keyword arguments.")

        # Validate the weights maps
        self.weights_map = _validate_weigths(self.weights_map)


    def expectation(self):
        @pl.qnode(self.dev)
        def _expectation_01(_params):
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            return pl.expval.PauliZ(0), pl.expval.PauliZ(1)

        @pl.qnode(self.dev)
        def _expectation_02(_params):
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            return pl.expval.PauliZ(0), pl.expval.PauliZ(2)

        @pl.qnode(self.dev)
        def _expectation_03(_params):
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            return pl.expval.PauliZ(0), pl.expval.PauliZ(3)

        @pl.qnode(self.dev)
        def _expectation_12(_params):
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            return pl.expval.PauliZ(1), pl.expval.PauliZ(2)

        @pl.qnode(self.dev)
        def _expectation_13(_params):
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            return pl.expval.PauliZ(1), pl.expval.PauliZ(3)

        @pl.qnode(self.dev)
        def _expectation_23(_params):
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            ###############################################
            pl.CNOT(wires = [0, 1])
            pl.CNOT(wires = [1, 2])
            pl.CNOT(wires = [2, 3])
            ###############################################
            pl.RY(_params[0], wires = [0])
            pl.RY(_params[1], wires = [1])
            pl.RY(_params[2], wires = [2])
            pl.RY(_params[3], wires = [3])
            return pl.expval.PauliZ(2), pl.expval.PauliZ(3)

        # Calculate the individuation weights that will be added to form the total
        total_weight = 0
        params = [0.1, 0.2, 0.3, 0.4]
        for edges, weight in self.weights_map.items():
            if edges == (0, 1):
                total_weight = total_weight + weight * (sum(_expectation_01(params)) / 2)

            elif edges == (0, 2):
                total_weight = total_weight + weight * (sum(_expectation_02(params)) / 2)

            elif edges == (0, 3):
                total_weight = total_weight + weight * (sum(_expectation_03(params)) / 2)

            elif edges == (1, 2):
                total_weight = total_weight + weight * (sum(_expectation_12(params)) / 2)

            elif edges == (1, 3):
                total_weight = total_weight + weight * (sum(_expectation_13(params)) / 2)

            elif edges == (2, 3):
                total_weight = total_weight + weight * (sum(_expectation_23(params)) / 2)

            else:
                raise ValueError("The given edge '" + str(edge) + "' in the weights map is out of bounds. the minimum is '(0, 1)' and the maximum is '(2, 3)'.")

        # We are done, return the user the maximum cut which corresponds to the sum of all cut edges' weights
        return total_weight


def _validate_weigths(weights_map):
    for edges, weight in weights_map.items():
        # We make sure we were given a pair as edges
        if type(edges) is not tuple:
            raise ValueError("All keys in the weights map must be tuples of two integers.")

        # Make sure that each tuple is a pair
        if len(edges) != 2:
            raise ValueError("All keys in the weights map must have two integers as keys.")

        # We make sure we were given integers as elements of the weights map key pair
        if type(edges[0]) is not int:
            raise ValueError("The first item in the weights map keys must be an integer.")
        if type(edges[1]) is not int:
            raise ValueError("The second item in the weights map keys must be an integer.")

        # We make sure that edges.first < edges.second as required for the algorithm to work
        if edges[0] >= edges[1]:
            raise ValueError("The first item of a0 weights map key must less than the second item.")

        # We make sure that the weight is a number
        if type(weight) is not int:
            raise ValueError("The weight must be an integer.")

    return weights_map
