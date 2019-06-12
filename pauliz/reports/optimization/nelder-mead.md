# Nelder-Mead simplex optimization

We proceed to use the Nelder-Mead optimization algorithm to minimize perform the minization.
Nelder-Mead is a derivative-free optimization procedure making it more or less insensitive to
statistical noise.

Compared to gradient descent, for our particular Hamiltonian, this algorithm came with a series
advantages:

1. Appears insensitive to the initial parameter.

2. No need to provide the number of steps until convergence.

3. No need to provide the step size for the algorithm.

Code (`main.py`):

```python
from quantum.ansatze import Rx
from quantum.hamiltonian import PZHamiltonian
from classical.nelder import NelderMeadOptimizer


def main():
    # The cost function that is to be evaluated on the quantum computer and which returns to us the expectation value of the Hamiltonian
    def cost(params):
        ham = PZHamiltonian(Rx)
        return ham.expectation(params)

    # Find the lowest eigenvalue through classical Nelder-Mead
    optimizer = NelderMeadOptimizer(cost)
    eigv = optimizer.optimize(params = [1.0])
    print("The ground state eigenvalue of the Pauli Z operator is: " + str(eigv))


if __name__ == "__main__":
    main()

```

However as noted in _No Free Lunch Theorems for Search by **Wolpert, D.H. and Macgready, W.G.**_, if algorithm A seems to outperform algorithm B,
then there will exist instances where algorithm B will clearly outperform algorithm A.
Therefore, we must not celebrate too early and always consider which nature our problem and the structure
of our solution in choosing the algorithm to apply.


## Conclusion

Nelder-Mead is an algoritm that's robust to small amount of noise. But there are exists much better
optimization techniques. The TOMLAB family of algorithms demonstrates superior performance for this
specific class of problems (where variational quantum eigensolver is used).
A comparison between Nelder-Mead and TOMLAB was done in _The theory of variational hybrid quantum-classical algorithms by **Jarrod R McClean et al.**_
and the reader is encouraged to consult the paper for details.

We close by noting that because there will be statistical noise in most of the cost functions we will use
for the variational quantum eigensolver algorithm, gradient based methods will in general be a poor choice
and derivative free methods will be a good choice most of the time.
The reader is referred to the book _Derivative-free optimization: a review of algorithms and comparison of software implementations by **Rios, L.M. and Sahinidis, N.V.**_
for a comprehensive comparison of derivative-free optmization methods.


## Author

Report prepared by Ntwali B.
