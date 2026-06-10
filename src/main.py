from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram

# Build a simple one-qubit circuit for beginners.
# We create a single qubit and a matching classical bit to store the measurement:
# QuantumCircuit(number of quantum bits, number of classical bits). 
# Each qubit starts in state |0⟩ and can be modified using quantum gates. 
# The number of classical bits is optional when using measure_all()
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to qubit 0.
# This puts the qubit into a superposition of |0> and |1>.
# This turns a definite state (|0>) into a 50/50 random state.
# After measurement, the result has an equal chance of being 0 or 1.
qc.h(0)

# Measure the qubit into the classical register.
# After measurement, the state collapses to either 0 or 1.
qc.measure_all()

# StatevectorSampler() is a Qiskit object that executes a quantum circuit and 
# returns simulated measurement results.
# Execute the quantum circuit 2200 times (shots).
# Each execution produces a measurement result (e.g., 0 or 1).
# Running the circuit many times allows us to estimate the probability
# distribution by counting how often each result occurs.
sampler = StatevectorSampler()
result = sampler.run([qc], shots=2200).result()

# Extract the counts from the result.
counts = result[0].data.meas.get_counts()
print()
print("Measurement counts:", counts)
print()

# Plot a histogram of the measured results.
# This helps beginners see the distribution visually.
hist = plot_histogram(counts)
hist.savefig("measurement_histogram.png")
print("Histogram saved to measurement_histogram.png")
print()