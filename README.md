# Quantum_cats

BIP, High performance shrodingers cat

link to the ultra-gambler repo: https://github.com/iamkredig/ultra-gambler
the quantum branch is: https://github.com/iamkredig/ultra-gambler/tree/py-test. the quantum branch require python installed on the pc. Please make sure to have python and quiskit installed, as well as adjusted the path to python in the cmake

### Annotated beginner version

The most important concepts are:

Let's start completely from the beginning.

# 1. What is a qubit?

In a normal computer, a bit can be:

```text
0
or
1
```

A **qubit** can be in a combination of both states at the same time.

We write:

```text
|0⟩
|1⟩
```

for the two possible states.

---

# 2. What is a Quantum Circuit?

A quantum circuit is just a sequence of operations applied to qubits.

This line creates a circuit with **2 qubits**:

```python
qc = QuantumCircuit(2)
```

Initial state:

```text
qubit 0 = |0⟩
qubit 1 = |0⟩
```

So:

```text
|00⟩
```

means:

```text
qubit0 = 0
qubit1 = 0
```

---

# 3. The Hadamard Gate (H)

```python
qc.h(0)
```

applies a Hadamard gate to qubit 0.

Before:

```text
|0⟩
```

After:

```text
(|0⟩ + |1⟩)/√2
```

Meaning:

```text
50% chance of measuring 0
50% chance of measuring 1
```

Visual idea:

```text
Before H:

100% 0

After H:

50% 0
50% 1
```

So after:

```python
qc.h(0)
```

the first qubit is random.

Current state:

```text
(|00⟩ + |10⟩)/√2
```

---

# 4. The CNOT Gate (CX)

```python
qc.cx(0, 1)
```

means:

```text
Control = qubit 0
Target  = qubit 1
```

Rule:

```text
If control = 1
    flip target
```

Examples:

```text
00 → 00
01 → 01
10 → 11
11 → 10
```

---

## Apply it to our state

Before CNOT:

```text
(|00⟩ + |10⟩)/√2
```

Apply CNOT:

```text
|00⟩ stays |00⟩
|10⟩ becomes |11⟩
```

Result:

```text
(|00⟩ + |11⟩)/√2
```

This is called an **entangled state**.

---

# 5. What is Entanglement?

The qubits are now connected.

If you measure:

```text
qubit0 = 0
```

you automatically know:

```text
qubit1 = 0
```

If you measure:

```text
qubit0 = 1
```

then:

```text
qubit1 = 1
```

Possible outcomes:

```text
00
11
```

Impossible outcomes:

```text
01
10
```

---

# 6. Measurement

```python
qc.measure_all()
```

Measurement converts quantum information into classical bits.

Before measurement:

```text
(|00⟩ + |11⟩)/√2
```

After measurement:

```text
50% → 00
50% → 11
```

---

# 7. The Sampler

```python
sampler = StatevectorSampler()
```

The sampler runs the circuit many times.

One run gives only:

```text
00
```

or

```text
11
```

So we run it thousands of times.

---

# 8. Running 2200 shots

```python
result = sampler.run([qc], shots=2200).result()
```

Here:

```python
shots=2200
```

means:

> Repeat the experiment 2200 times.

Example:

```text
Run 1: 00
Run 2: 11
Run 3: 00
Run 4: 11
...
```

---

# 9. Counting Results

```python
counts = result[0].data.meas.get_counts()
```

Possible output:

```python
{
    '00': 1098,
    '11': 1102
}
```

Meaning:

```text
00 appeared 1098 times
11 appeared 1102 times
```

which is approximately:

```text
50%
50%
```

---

# 10. Printing

```python
print(counts)
```

Output:

```python
{'00': 1098, '11': 1102}
```

---

# 11. Histogram

```python
plot_histogram(counts)
```

draws a graph.

Something like:

```text
1100 |
     |        ████
1000 |        ████
     |        ████
 500 |
     |
   0 +----------------
       00      11
```

Because only:

```text
00
11
```

can occur.

---

# Complete Code Example

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
