# Choice of ansatz

In the literature, one often reads that the choice of ansatz is arbitrary.
It is not meant that any ansatz will do for any problem. What is meant is that there exists
a class of ansatz from which we can choose the one that fits the algorithm at hand.

In this report, we explore different ansatz that will not work on the Hamiltonian of choice.
We wish to find the lowest eigenvalue of the Pauli Z operator. With Pauli Z as our Hamiltonian,
which ansatz will not work at all? Which ones will work?

Our ansatz set contains the rotation gates `Rx` (rotation about X), `Ry` (rotation about Y), `Rz` (rotation about Z), `Had` (Hadamard) and `Phase` (Phase shift).
The `Rx` and `Ry` gates are able to affect the expectation value because they change the location of the qubit on the Z axis through rotations.

A successful evolution of the expectation of the Hamiltonian with respect to the ansatz parameter is shown in the figure below.

Figure (successful evolution of the expectation of the ansatz parameter):

![Successful evolution of the Hamiltonian expectation with respect to the ansatz parameter](images/Ansatz_1.png "Pauli Z expectation with the Ry ansatz parameter.")


## Observation 1: Importance of ansatz independence from the Hamiltonian

We notice that Rz will not vary for different values of the gate parameter because Rz just rotates
the qubit around the Z and a projection of qubit on the Z axis will always result in the same expectation
for the Z operator.

Figure (the expectation doesn't vary with the ansatz parameter):

![Note that the Hamiltonian parameter doesn't vary with the change in the ansatz parameter](images/Ansatz_2.png "Pauli Z expectation with the Rz ansatz parameter.")

Code (`main.py`):

```python
from pennylane import numpy as np
from matplotlib import pyplot as pp

from quantum.ansatze import Rz
from quantum.hamiltonian import PZHamiltonian


def main():
    # We create the Hamiltonian passing it the state creation ansatz
    ham = PZHamiltonian(Rz)

    # We find expectations between 0 and 2*pi
    params = np.linspace(0.0, 2 * np.pi, 100)
    expecs = [ham.expectation([param]) for param in params]

    # We plot the expectation curve: params vs expectation
    pp.xlabel("Ansatz parameter")
    pp.ylabel("Expectation")
    pp.plot(params, expecs)
    pp.show()

if __name__ == "__main__":
    main()

```


## Observation 2: Not all parametrized ansatz can do

When the ansatz does not depend on a parameter, the qubit can't evolve.
We use the Hadamard gate as our ansatz. Since the ansatz doesn't depend on any paramater,
any phase it induces on the qubit will be global and the Pauli Z expectation with respect
to the qubit will not be affected.

Note that even though one could use the Phase gate which depends on a parameter, the effect is the same
as using the Hadamard gate: the phase gate induces a phase on the qubit but being our only qubit, the phase
is global and doesn't result in a change of the qubit in the Bloch sphere and hence no change in
the qubit measurement result (from which we can deduce the expectation).

Figure (the expectation doesn't vary with the ansatz parameter):

![Note that the Hamiltonian parameter doesn't vary with the change in the ansatz parameter](images/Ansatz_3.png "Pauli Z expectation with the Hadamard ansatz parameter.")

Code (`main.py`):

```python
from pennylane import numpy as np
from matplotlib import pyplot as pp

from quantum.ansatze import Had
from quantum.hamiltonian import PZHamiltonian


def main():
    # We create the Hamiltonian passing it the state creation ansatz
    ham = PZHamiltonian(Had)

    # We find expectations between 0 and 2*pi
    params = np.linspace(0.0, 2 * np.pi, 100)
    expecs = [ham.expectation([param]) for param in params]

    # We plot the expectation curve: params vs expectation
    pp.xlabel("Ansatz parameter")
    pp.ylabel("Expectation")
    pp.plot(params, expecs)
    pp.show()

if __name__ == "__main__":
    main()

```

## Conclusion

As is evident in our observation, our freedom of choice of the ansatz is reduced because not all gates
are valid ansatz. Therefore one must choose carefully the ansatz before proceeding with classical optimization
else one risks working with the wrong ansatz.


## Future considerations

1. Do difference ansatz lead to difference convergence speed? If so, how do we determine the faster one?

2. Are there ansatz that will converge but will not reach the minimum? If yes, which ones?


## Author

Report prepared by Ntwali B.
