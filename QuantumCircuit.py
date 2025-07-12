from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Apply Hadamard gate to qubit 0 (creates superposition)
qc.h(0)

# Apply CNOT gate (creates entanglement)
qc.cx(0, 1)

# Visualize the circuit
qc.draw('mpl')

# Simulate statevector
state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)

# Add measurement
qc.measure_all()

# Simulate with QASM
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()
plot_histogram(counts)
plt.show()
