import numpy as np


lambda_exp = 2  # Exponential distribution parameter
na = 320  # Number of samples required from part (a)
m = 1000  # Number of trials

true_mean_exp = 1 / lambda_exp
true_std_exp = 1 / lambda_exp

count_exp = 0

for i in range(m):
    samples = np.random.exponential(scale=1/lambda_exp, size=na)
    
    # Calculate sample mean
    sample_mean = np.mean(samples)
    
    # Check if the sample mean differs from the true mean by no more than
    # 25% of the true standard deviation
    if np.abs(sample_mean - true_mean_exp) <= 0.25 * true_std_exp:
        count_exp += 1

# Display results
print("For the exponential distribution:")
print(f"Number of trials meeting the criteria: {count_exp} out of {m}")

# Part (b): Standard Normal distribution
nb = 62  # Number of samples required from part (b)

# True mean and standard deviation of standard normal distribution
true_mean_normal = 0
true_std_normal = 1

# Initialize counter for trials meeting the criteria
count_normal = 0

for i in range(m):
    # Generate random samples from standard normal distribution
    samples_normal = np.random.standard_normal(size=nb)
    
    # Calculate sample mean
    sample_mean_normal = np.mean(samples_normal)
    
    # Check if the sample mean differs from the true mean by no more than
    # 25% of the true standard deviation
    if np.abs(sample_mean_normal - true_mean_normal) <= 0.25 * true_std_normal:
        count_normal += 1

# Display results
print("\nFor the standard normal distribution:")
print(f"Number of trials meeting the criteria: {count_normal} out of {m}")
