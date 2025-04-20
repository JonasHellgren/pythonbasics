import numpy as np
import matplotlib.pyplot as plt

# Function that generates x and y data for weight adaptation
def generate_xy(w_start=0.0, wRef=1.0, alpha=0.1, steps=50):
    x = []
    y = []
    w = w_start  # Initial value of weight
    for i in range(1, steps):
        x.append(i)     # Store current iteration number
        y.append(w)     # Store current weight value
        e = wRef - w    # Calculate error between target and current weight
        w = w + alpha * e  # Update weight using learning rate (alpha)
    return x, y  # Return iteration steps and corresponding weight values

# Setup initial parameters
wRef = 1              # Desired target value of the weight
alpha = 0.1           # Default alpha (not used here directly)
w_start = 0.5         # Initial value of w
nSteps = 50           # Number of iterations

# Try different learning rates
alphas = np.array([0.1, 0.2, 0.4, 0.8])

# Loop through each learning rate and plot the results
for alpha in alphas:
    x, y = generate_xy(w_start, wRef, alpha, nSteps)
    plt.plot(x, y, label=f'alpha = {alpha:.1f}')  # Plot each alpha on the same graph

# Add horizontal line showing the reference value
plt.axhline(y=wRef, color='gray', linestyle='--', label='wRef')

# Add labels, title, legend, and grid to the plot
plt.xlabel('Iteration')
plt.ylabel('w')
plt.title('Weight Convergence for Different Alphas')
plt.legend()
plt.grid(True)
plt.show()


