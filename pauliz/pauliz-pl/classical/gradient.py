# -*- coding: utf-8 -*-

"""
Author          : Ntwali Bashige
Copyright       : Copyright 2019 - Ntwali Bashige
License         : MIT
Version         : 0.0.1
Author          : Ntwali Bashige
Email           : ntwali.bashige@gmail.com
"""

from pennylane.optimize import GradientDescentOptimizer
from pennylane import numpy as np


class GradientOptimizer(object):
    def __init__(self, cost, step_size):
        self.cost = cost
        self.optimizer = GradientDescentOptimizer(step_size)


    def optimize(self, **kwargs):
        params = kwargs.get("params", None)
        steps = kwargs.get("steps", None)
        
        # Validate the cost function parameters
        if params is None:
            raise ValueError("Excepted 'params' passed as a keyword argument to be used by the cost function.")
        if isinstance(params, list) == False:
            raise ValueError("The 'params' keyword argument must be a list of parameters to be passed to the cost function.")

        # Make sure we were given the number of steps unti convergence
        if steps is None:
            raise ValueError("Excepted 'steps' to be passed a keyword argument for the number of steps the optimizer is to take towards convergence.")

        # Run the optmizer for the given number of steps
        for i in range(steps):
            params = self.optimizer.step(self.cost, params)

        return self.cost(params)
