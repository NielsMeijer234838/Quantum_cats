from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram

# Build a simple one-qubit circuit for beginners.
# We create a single qubit and a matching classical bit to store the measurement.
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to qubit 0.
# This puts the qubit into a superposition of |0> and |1>.
qc.h(0)

# Measure the qubit into the classical register.
# After measurement, the state collapses to either 0 or 1.
qc.measure_all()

# Use the statevector sampler to run the circuit many times.
# shots=2200 lets us see the probabilities as measurement counts.
sampler = StatevectorSampler()
result = sampler.run([qc], shots=2200).result()

# Extract the counts from the result.
counts = result[0].data.meas.get_counts()
print("Measurement counts:", counts)

# Plot a histogram of the measured results.
# This helps beginners see the distribution visually.
hist = plot_histogram(counts)
hist.savefig("measurement_histogram.png")
print("Histogram saved to measurement_histogram.png")
