# Report

In this experiment on variational quantum eigensolver, we investigated how the choice of ansatz
and minimization algoritm influences the find result we get.

In the choice of ansatz, we noted that one must make sure the chosen ansatz influces the states
in a manner that as the given ansatz parameter changes, the state (qubit) should move through
Hilbert space in a manner that expectation measurement yields all possible measurement when
the domain of the parameter is thoroughly explored.

In the choice of the optimization algorithm, we noted that derivative-free optimization
methods are superior to gradient based optimization methods. We used the Nelder-Mead
algorithm but also noted the TOMLAB algorithm is superior to it.

We left a few questions unanswer for future ampirical and theoretical investigations.


## Report structure

In this folder, reports are organized as shown below. Attached are the main points to look for when reading each report.

```
project
│   README.md
│
└───ansatz
│   │   ansatz.md: Consideration regarding the choice of ansatz.
│   
└───optimization
│   │   gradient-descent.md: Caveats pertaining to the use of gradient descent.
│   |   nelder-mead.md: Justification over gradient descent and note on the superior TOMLAB.
│   
└───images
    │   Ansatz_1.png: Successful evolution of the Hamiltonian expectation with respect of a correct ansatz.
    │   Ansatz_2.png: Failure of the evolution of the Hamiltonian expectation with respect to the Rz ansatz which doesn't explore the Z axis.
    │   Ansatz_3.png: Failure of the evolution of the Hamiltonian expectation with respect to the Hadamard ansatz which accepts not parameter.

```


## Author

Reports prepared by Ntwali B.
