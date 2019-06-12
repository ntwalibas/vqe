# Gradient descent optimization

Gradient descent is a derivate based optimization technique and one of the simplest.
There it makes sense that as a first step one would use to perform the classical optimization.

In this report, we examine cases where gradient descent would not work at all by giving the wrong results;
i.e. it returns an eigenvalue that is not the ground state (it gets stuck in a local minimum).


## Observation 1: gradient descent sensitivity to the initial ansatz parameter

For an initial parameter equal to zero, gradient descent will not converge at all to the known
global minimum and will get stuck to the next available eigenvalue, in our case 1.

Code (`main.py`):

```python
from quantum.ansatze import Rx
from quantum.hamiltonian import PZHamiltonian
from classical.gradient import GradientOptimizer


def main():
    # The cost function that is to be evaluated on the quantum computer and which returns to us the expectation value of the Hamiltonian
    def cost(params):
        ham = PZHamiltonian(Rx)
        return ham.expectation(params)

    # Find the lowest eigenvalue through classical gradient descent optimization
    optimizer = GradientOptimizer(cost, 0.1)
    eigv = optimizer.optimize(params = [0.0], steps = 100)
    print("The ground state eigenvalue of the Pauli Z operator is: " + str(eigv))


if __name__ == "__main__":
    main()
```


## Obervation 2: Gradient descent is sensitive to the number of steps and initial parameter

As the number of steps decrease and the initial parameter increases further from zero, we can
maintain a given accuracy of the eigenvalue of interest.

What this tells us is that the initial parameter matters a lot. Due to resources constraints, we may
not be able to increase the number of steps for better accuracy but changing the initial parameter
can be changed at no computational cost. Therefore when seeks better accuracy, he or she can look at the initial parameter.
This is not necessarily easy because for some problems, the number of initial parameters may form a space too big
to explore but it is still worth it experimenting.

Code (`main.py`):

```python
from quantum.ansatze import Rx
from quantum.hamiltonian import PZHamiltonian
from classical.gradient import GradientOptimizer


def main():
    # The cost function that is to be evaluated on the quantum computer and which returns to us the expectation value of the Hamiltonian
    def cost(params):
        ham = PZHamiltonian(Rx)
        return ham.expectation(params)

    # Find the lowest eigenvalue through classical gradient descent optimization
    optimizer = GradientOptimizer(cost, 0.1)
    eigv = optimizer.optimize(params = [2.0], steps = 10) # eigv = -0.9015038162478396
    # eigv = optimizer.optimize(params = [1.0], steps = 20) # eigv = -0.8907435965533671
    print("The ground state eigenvalue of the Pauli Z operator is: " + str(eigv))


if __name__ == "__main__":
    main()
```


## Conclusion

The paper _The theory of variational hybrid quantum-classical algorithms by **Jarrod R McClean et al.**_
recommends the use of nonlinear optmization schemes such TOMLAB class of algorithms.
We must remember that though the initial application of the variational quantum eigensolver was in quantum
chemistry where the values are statistical in nature and subject to noise and gradient descent is not suitable
for such tasks.

Therefore, the choice of optimization algorithm is dependent of the problem at hand and computational
resources at ones disposal. In this case, as we are working with pure states, gradient descent is good enough.


## Author

Report prepared by Ntwali B.

