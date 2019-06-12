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


class MaxCutHamiltonian(object):
    def __init__(self, **kwargs):
        self.ansatz = kwargs.pop("ansatz")
        self.wires = kwargs.pop("wires")
        self.depth = kwargs.pop("depth")
        self.weights_map = kwargs.get("weights", None)
        self.qvm = api.QVMConnection()

        if self.weights_map is None:
            raise ValueError("Expected the graph's edges 'weights' as part of the constructor keyword arguments.")

        # Validate the weights maps
        self.weights_map = _validate_weigths(self.weights_map, len(self.wires))


    def expectation(self):
        def _expectation(_qubits, _params):
            exp = PauliSum([PauliTerm.from_list([('Z', _qubits[0]), ('Z', _qubits[1])])])
            return VQE.expectation(self.ansatz(_params, self.wires, self.depth), exp, None, self.qvm)

        # Calculate the individuation weights that will be added to form the total
        total_weight = 0
        params = [0.1, 0.2, 0.3, 0.4]
        for edges, weight in self.weights_map.items():
            total_weight = total_weight + weight * _expectation(edges, params)

        # We are done, return the user the maximum cut which corresponds to the sum of all cut edges' weights
        return total_weight


def _validate_weigths(weights_map, qubits):
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

        # We make sure the edges are within qubits boundaries
        if edges[0] < 0 or edges[1] > qubits:
            raise ValueError("Edges outside of qubits count are not allowed.")

        # We make sure that the weight is a number
        if type(weight) is not int:
            raise ValueError("The weight must be an integer.")

    return weights_map
