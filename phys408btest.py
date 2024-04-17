import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Define the medium properties
epsilon1, mu1 = 1.5, 1.2
epsilon2, mu2 = 1.8, 1.1

# Define k relative to the properties of each medium
k_ratios = [(1, 2), (1, 3), (2, 1), (3, 1)]  # These are the ratios of k/√(εμ) as described

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
colors = ['blue', 'red']
cmap = mcolors.ListedColormap(colors)
norm = mcolors.BoundaryNorm([0, 0.5, 1], cmap.N)

# Generate plots for each set of ratios
for ax, (k_ratio1, k_ratio2) in zip(axs.ravel(), k_ratios):
    k1 = k_ratio1 * np.sqrt(epsilon1 * mu1)  # k1 adjusted for medium 1
    k2 = k_ratio2 * np.sqrt(epsilon2 * mu2)  # k2 adjusted for medium 2
    Tau, Tau_prime = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
    Tau_diff = Tau_prime - Tau

    # Calculate b using the specific wave numbers for each medium
    b_values = np.cos(k1 * Tau) * np.cos(k2 * Tau_diff) - \
               ((epsilon1 * mu1 + epsilon2 * mu2) / (2 * np.sqrt(epsilon1 * mu1 * epsilon2 * mu2))) * \
               np.sin(k1 * Tau) * np.sin(k2 * Tau_diff)

    stability = np.where(np.abs(b_values) < 1, 0, 1)  # Determine mode based on b value
    c = ax.contourf(Tau, Tau_diff, stability, levels=[-0.5, 0.5, 1.5], cmap=cmap, norm=norm, extend='both')
    ax.set_title(f'k/√(ε1μ1) = {k_ratio1}, k/√(ε2μ2) = {k_ratio2}')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r"$\tau' - τ$")
    fig.colorbar(c, ax=ax, label='Mode Type')

plt.tight_layout()
plt.show()
