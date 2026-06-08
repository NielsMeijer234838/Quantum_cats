# Quantum_cats
BIP, High performance shrodingers cat

Here is the same program with much more detailed comments that explain the basic principles (Prinzipien) and the Fachbegriffe used in quantum computing.

### Annotated beginner version

The most important concepts in this example are:

### Qubit

Definition: Quantum bit.

Explanation: Can exist in state |0⟩, |1⟩, or a superposition of both.

Example: After the Hadamard gate, the qubit is in (|0⟩ + |1⟩)/√2.

### Superposition

Definition: A quantum state that combines multiple basis states.

Explanation: The system is not simply 0 or 1 before measurement.

Example: (|0⟩ + |1⟩)/√2.

### Hadamard Gate (H)

Definition: A quantum gate that creates superposition.

Explanation: Transforms a definite state into an equal superposition.

Example: |0⟩ → (|0⟩ + |1⟩)/√2.

### Measurement

Definition: Reading a qubit's value.

Explanation: Converts the quantum state into a classical bit and causes collapse.

Example: Measuring the superposition gives 0 or 1.

### Collapse (Kollaps)

Definition: Reduction of a superposition to a definite outcome.

Explanation: After measurement, the qubit is no longer in the original superposition.

Example: The measured state becomes either |0⟩ or |1⟩.

### Shots

Definition: Number of repeated executions.

Explanation: Quantum probabilities are estimated statistically.

Example: 2200 shots produce counts close to 50/50.

### Histogram

Definition: Bar chart of measurement frequencies.

Explanation: Helps visualize the probability distribution.

Example: Two bars of roughly equal height for 0 and 1.

### The absolute principle behind this program

Quantum computing works with probability amplitudes instead of fixed classical values. The Hadamard gate creates a superposition. Measurement converts that quantum state into a classical result. By repeating the experiment many times (shots), we estimate the probabilities of the outcomes.

In this specific circuit, the theory predicts approximately:

| Outcome | Probability |
| ------- | ----------- |
| 0       | 50%         |
| 1       | 50%         |

So the histogram should show two bars of roughly equal height.

### Mental model

![Qubits Explained: The Building Blocks of Quantum Computing | by Priya N | Medium](https://images.openai.com/static-rsc-4/8sVzA2vff2_r0xpIo52_Sz8BrSuy1tg05TzZFnq2Qokn9tZWF86IBSqNFujgRVn2lqSQv9oxO6Paq4A1fPuYWQ3xbALohB8IXnya7oGEpYLEyiee9Zvl9one8V7HxFm2vgm90l-j0WNmjvhzZaOam2Kd7MVw6Pz3Yh7f-9B5RELfGTyOgT0iQo9z7NAqCJjT?purpose=fullsize)

1. Start with a qubit in |0⟩.

2. Apply H → create superposition.

3. Measure → collapse to 0 or 1.

4. Repeat many times → observe the statistical distribution.

This is the foundation of almost all quantum information experiments. Entanglement, teleportation, quantum cryptography, and quantum algorithms all build on these same ideas.
