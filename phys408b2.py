import numpy as np
import matplotlib.pyplot as plt

# Define the parameter b and calculate eigenvalues for both lambda+ and lambda-
b_values = np.linspace(-3, 3, 400)
lambda_plus = np.array([b + 1j*np.sqrt(1 - b**2) if abs(b) < 1 else b + np.sqrt(b**2 - 1) for b in b_values])
lambda_minus = np.array([b - 1j*np.sqrt(1 - b**2) if abs(b) < 1 else b - np.sqrt(b**2 - 1) for b in b_values])

# Downsampling for the complex plane plot
downsampling_factor = 10  # Only plot every 10th point
sampled_indices = np.arange(0, len(b_values), downsampling_factor)

# Part (a): Plot the real part of the eigenvalues
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.plot(b_values, np.real(lambda_plus), label=r'Real Part of $\lambda_+$')
plt.plot(b_values, np.real(lambda_minus), label=r'Real Part of $\lambda_-$', linestyle='--')
plt.title('Evolution of the Real Parts of $\lambda_+$ and $\lambda_-$')
plt.xlabel('Parameter b')
plt.ylabel('Real Part')
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.xlim(-3, 3)  # Set x-axis limits
plt.ylim(-3, 3)  # Set y-axis limits

# Part (b): Plot on the complex plane
plt.subplot(1, 2, 2)
plt.scatter(np.real(lambda_plus[sampled_indices]), np.imag(lambda_plus[sampled_indices]), c=b_values[sampled_indices], cmap='coolwarm', marker='x', label=r'$\lambda_+$', edgecolors='black')
plt.scatter(np.real(lambda_minus[sampled_indices]), np.imag(lambda_minus[sampled_indices]), c=b_values[sampled_indices], cmap='coolwarm', marker='o', label=r'$\lambda_-$', edgecolors='black', alpha=0.6)
plt.colorbar(label='Value of b')
plt.title('Eigenvalues in the Complex Plane')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.grid(True)
plt.legend()
plt.axis('equal')  # Ensuring x and y axes have the same scale
plt.xlim(-3, 3)  # Set x-axis limits
plt.ylim(-3, 3)  # Set y-axis limits

plt.tight_layout()
plt.show()

