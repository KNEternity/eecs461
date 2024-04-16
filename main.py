import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Set random seed for reproducibility
np.random.seed(42)

# Generate 20,000 uniform random samples
uniform_samples = np.random.uniform(0, 1, 20000)

# Apply transformation to convert to exponential distribution with mean of 3
transformed_samples = -3 * np.log(1 - uniform_samples)

# Calculate the average of transformed sample values
average_transformed = np.mean(transformed_samples)
print(f"Average of transformed sample values: {average_transformed}")

# Create histogram for transformed sample values

# Calculate theoretical probabilities for exponential distribution with mean of 3
x = np.arange(0, 15.1, 0.1)
y = expon.pdf(x, scale=3)

# Plot theoretical probabilities as discrete bars
plt.bar(x, y, width=0.1, alpha=0.5, label='Theoretical', color='r', edgecolor='black', linewidth=1.5)

# Set plot labels and title
plt.title('Exponential Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Relative Frequency / Probability')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
