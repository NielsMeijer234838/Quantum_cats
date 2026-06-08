# Quantum_cats
BIP, High performance shrodingers cat

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

# Complete Story

Initial state:

```text
|00⟩
```

After H:

```text
(|00⟩ + |10⟩)/√2
```

After CNOT:

```text
(|00⟩ + |11⟩)/√2
```

After Measurement:

```text
50% → 00
50% → 11
```

This is actually one of the most famous quantum circuits because it creates a **Bell State**, specifically:

\frac{|00\rangle+|11\rangle}{\sqrt{2}}

and is often the first example used to demonstrate **superposition**, **entanglement**, and **quantum randomness**.
