import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Gaussian Process to generate a smooth random field
def generate_gp(L, n):
    x = np.atleast_2d(np.linspace(0, L, L)).T
    kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
    y_train = np.random.randn(L, n)
    gp.fit(x, y_train)
    y_pred, _ = gp.predict(x, return_std=True)
    return y_pred

# Initialize track features
def initialize_track(L, n):
    return generate_gp(L, n)

# Initialize agent features
def initialize_agent(n):
    return np.random.randn(n)

# Compute speed based on similarity (cosine similarity used here)
def speed(agent, track_features, alpha=1.0, beta=1.0):
    norm_agent = np.linalg.norm(agent)
    norm_track = np.linalg.norm(track_features)
    return alpha + beta * np.dot(agent, track_features) / (norm_agent * norm_track)

# Main function for simulation
def main(num_agents=1):
    L = 1000  # Track length
    n = 5  # Number of features
    alpha = 1.0
    beta = 1.0
    dt = 0.1  # Time step
    t = 0  # Time

    track = initialize_track(L, n)
    agents = [initialize_agent(n) for _ in range(num_agents)]
    positions = np.zeros(num_agents)

    fig, ax = plt.subplots()
    circles = [ax.plot([], [], 'o', lw=3)[0] for _ in range(num_agents)]
    ax.set_xlim(0, L)
    ax.set_ylim(-2, 2)
    track_plot, = ax.plot(np.linspace(0, L, L), track[:, 0], 'g-', label='Track Feature 1')
    ax.legend()

    while t < 100:
        for i in range(num_agents):
            agent = agents[i]
            s = positions[i]
            track_features = track[int(s) % L]
            v = speed(agent, track_features, alpha, beta)
            positions[i] += v * dt
            circles[i].set_data(positions[i] % L, 0)
        
        t += dt
        plt.draw()
        plt.pause(0.01)

    plt.show()

if __name__ == "__main__":
    main(num_agents=3)
