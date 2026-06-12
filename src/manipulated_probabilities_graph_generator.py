from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
import matplotlib.pyplot as plt
import numpy as np

qc = QuantumCircuit(2)
qc.ry(0.7754, 1)
qc.cry(1.4706, control_qubit=1, target_qubit=0)
qc.x(1)
qc.cry(1.0472, control_qubit=1, target_qubit=0)
qc.x(1)
qc.measure_all()

sampler = StatevectorSampler()
result = sampler.run([qc], shots=100_000).result()
counts = result[0].data.meas.get_counts()

total = sum(counts.values())
labels = ['00\n(symbol 1)', '01\n(symbol 2)', '10\n(symbol 3)', '11\n(symbol 4)']
targets = [50, 30, 15, 5]
measured = [counts.get(s, 0) / total * 100 for s in ['00', '01', '10', '11']]

fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor('#0f0f1a')
ax.set_facecolor('#0f0f1a')

x = np.arange(4)
width = 0.35

bars_target = ax.bar(x - width/2, targets, width, color='#3a3a6e', linewidth=0,
                     zorder=2, label='Target %')
bars_measured = ax.bar(x + width/2, measured, width, color='#00b4d8', linewidth=0,
                       zorder=2, label='Measured % (100k shots)')

for bar, val in zip(bars_target, targets):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.6,
            f'{val}%', ha='center', va='bottom', color='#8888bb', fontsize=10)

for bar, val in zip(bars_measured, measured):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.6,
            f'{val:.1f}%', ha='center', va='bottom', color='#00d4f8', fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(labels, color='#aaaacc', fontsize=11)
ax.set_ylabel('Probability (%)', color='#aaaacc', fontsize=11)
ax.set_ylim(0, 62)
ax.set_title('Quantum Slot — Symbol Probability Distribution', color='#ffffff',
             fontsize=13, pad=14)

ax.tick_params(colors='#aaaacc')
for spine in ax.spines.values():
    spine.set_edgecolor('#2a2a4a')
ax.yaxis.grid(True, color='#2a2a4a', linewidth=0.6, zorder=0)
ax.set_axisbelow(True)

ax.legend(facecolor='#1a1a2e', edgecolor='#2a2a4a', labelcolor='#aaaacc', fontsize=10)

plt.tight_layout()
plt.savefig('quantum_slot_distribution.png', dpi=150,
            bbox_inches='tight', facecolor='#0f0f1a')
plt.show()
