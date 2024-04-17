import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Constants and ranges
tau = np.linspace(0, 10, 100)
tau_prime = np.linspace(0, 10, 100)
Tau, Tau_prime = np.meshgrid(tau, tau_prime)
Tau_diff = Tau_prime - Tau

def eigenvalue_behavior(k1, k2, Tau, Tau_diff):
    # Model incorporating more realistic parameter impacts
    b = (np.cos(k1 * Tau) + np.cos(k2 * (Tau + Tau_diff)) - 
         np.sin(k1 * Tau) * np.sin(k2 * (Tau + Tau_diff)))
    return b

def stability_metric(b):
    # Differentiate between propagating modes and mixed modes
    condition = np.zeros_like(b)
    condition[np.abs(b) < 1] = 0  # Propagating modes
    condition[np.abs(b) > 1] = 1  # Mixed modes (one evanescent, one amplifying)
    return condition

params = [
    (1, 2), (1, 3), (2, 1), (3, 1)
]

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
colors = ['blue', 'red']  # Blue for propagating, Red for mixed modes
cmap = mcolors.ListedColormap(colors)
norm = mcolors.BoundaryNorm([0, 0.5, 1], cmap.N)

for ax, (k1, k2) in zip(axs.ravel(), params):
    b_values = eigenvalue_behavior(k1, k2, Tau, Tau_diff)
    stability = stability_metric(b_values)
    c = ax.contourf(Tau, Tau_diff, stability, levels=[-0.5, 0.5, 1.5], cmap=cmap, norm=norm, extend='both')
    ax.set_title(f'k1 = {k1}, k2 = {k2}')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r"$\tau' - \tau$")
    fig.colorbar(c, ax=ax, label='Mode Type')

plt.tight_layout()
plt.show()


