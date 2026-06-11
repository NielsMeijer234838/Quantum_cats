from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Create a circuit with 2 qubits => 4 equally likely outcomes (00, 01, 10, 11)
qc = QuantumCircuit(2)

# Put both qubits into a 50/50 superposition
qc.ry(0.9273, 1)
qc.cry(1.3181, control_qubit=1, target_qubit=0)
qc.x(1)
qc.cry(1.3181, control_qubit=1, target_qubit=0)
qc.x(1)

# Measure both qubits
qc.measure_all()

# StatevectorSampler() executes the circuit 1 time and
# returns simulated measurement results.
sampler = StatevectorSampler()
result = sampler.run([qc], shots=1).result()

# Extract the counts from the result.
counts = result[0].data.meas.get_counts()

# Get measured bitstring
bitstring = list(counts.keys())[0]

# Convert to integer 1-4
# 00 -> 1
# 01 -> 2
# 10 -> 3
# 11 -> 4
casino_symbol = int(bitstring, 2) + 1

# Output only the number for C++
print(casino_symbol)