from pyquil.quil import Program
from pyquil.api import get_qc
from pyquil.gates import CNOT, H

# Initializes a program as the following diagram.
# x0: |0> -H-.-
# x1: |0> ---+-
program = Program(H(0), CNOT(0, 1))

# Gets a QuantumComputer instance (2-qubit quantume virtual machine).
quantum_computer = get_qc('2q-qvm')

# Runs and measure with 20 times.
results = quantum_computer.run_and_measure(program, trials=20)
print(list(zip(results[0], results[1])))
