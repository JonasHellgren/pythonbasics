import numpy as np
import matplotlib.pyplot as plt

def generate_xy(w_start=0.0, wRef=1.0, alpha=0.1, steps=50):
    x = []
    y = []
    w = w_start  # initial weight from input

    for i in range(1, steps ):
        x.append(i)
        y.append(w)

        e = wRef - w
        w = w + alpha * e

        print(f"i = {i}, w = {w:.4f}, error = {e:.4f}")

    return x, y

w = 0
wRef=1
alpha=0.1
w_start=0.5
nSteps=50
x = []
y = []

alphas=np.array([0.1, 0.2,0.4,0.8 ])
for alpha in alphas:
    x, y = generate_xy(w_start, wRef, alpha, nSteps)
    plt.plot(x, y, label=f'alpha = {alpha:.1f}')

# Add horizontal reference line
plt.axhline(y=wRef, color='gray', linestyle='--', label='wRef')

# Final plot settings
plt.xlabel('Iteration')
plt.ylabel('w')
plt.title('Weight Convergence for Different Alphas')
plt.legend()
plt.grid(True)
plt.show()


