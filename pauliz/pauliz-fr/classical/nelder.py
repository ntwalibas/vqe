# -*- coding: utf-8 -*-

"""
Author          : Ntwali Bashige
Copyright       : Copyright 2019 - Ntwali Bashige
License         : MIT
Version         : 0.0.1
Author          : Ntwali Bashige
Email           : ntwali.bashige@gmail.com
"""

from scipy.optimize import minimize
import numpy as np


class NelderMeadOptimizer(object):
    def __init__(self, cost):
        self.cost = cost


    def optimize(self, **kwargs):
        params = kwargs.get("params", None)
        simplex = kwargs.get("simplex", None)
        xatol = kwargs.get("xatol", None)
        
        # Validate the cost function parameters
        if params is None:
            raise ValueError("Excepted 'params' passed as a keyword argument to be used by the cost function.")
        if isinstance(params, list) == False:
            raise ValueError("The 'params' keyword argument must be a list of parameters to be passed to the cost function.")

        # if the simplex is given, add it to the algoritm options
        options = {}
        if simplex is not None:
            options["initial_simplex"] = simplex
        if xatol is not None:
            options["xatol"] = xatol

        # Run the optmizer and return the minimized eigenvalue
        return minimize(self.cost, params, method = "Nelder-Mead", options = options).fun
