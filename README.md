
# Optimizing Agent Performance on a virtual track using unitary transformations.

## Description

This repository contains Python code for agent optimization. Agents navigate on a "track" characterized by a set of features generated using Fourier components. The performance of each agent in a specific portion of the track is given by the similarity between the agent's features and the track features of that location. The optimization involves rotating agents' features to improve their speed based on the dot product with the track features.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- tqdm
- IPython (optional for live plotting)

## Mathematical Foundation

### Fourier Track Generation

The track on which the agents navigate is generated using a truncated Fourier series:

\[
\text{Track}(x) = \sum_{n=1}^{N} \left( A_n \cos(2 \pi n x) + B_n \sin(2 \pi n x) \right)
\]

Where \( A_n \) and \( B_n \) are random coefficients, and \( N \) is the highest frequency.

These features represent arbitrary track features, such as the curvature of the track, the presence of straight lines, surface grip etc. 
The only constraint is that the track features are periodic, so that the track is a closed loop.

### Speed Calculation

The speed of each agent on the track is determined by:

\[
\text{speed} = \alpha + \beta \frac{\langle \text{agent}, \text{track features} \rangle}{\lVert \text{agent} \rVert \lVert \text{track features} \rVert}
\]

Where \( \alpha \) and \( \beta \) are constants, and \( \langle \cdot, \cdot \rangle \) denotes the dot product.

### Feature Rotation
The agent's features are represented by a vector in the plane. Different agents have different features, and the features of a single agent are constant during a lap/race. After each lap, the agent's features can be rotated to optimize performance.
An agent's features are rotated to optimize performance using:

\[
\text{Agent}_{\text{new}} = R(\theta, \textbf{u}, \textbf{v}) \text{Agent}_{\text{old}}
\]

Where \( R \) is the rotation matrix in the plane defined by vectors \( \textbf{u} \) and \( \textbf{v} \), and \( \theta \) is the rotation angle.

## Usage

Run the main function with your preferred settings:

```python
lap_times_history, budget_history, trained_agents, track = main(num_agents=10, num_laps=2000, initial_budget=200.0, live_plotting=False, dt=0.1)
```

## Functions

- `generate_fourier_vectorized`: Generates the track based on Fourier series.
- `speed_vectorized`: Computes the speed of agents based on dot product with track features.
- `rotate_features`: Rotates an agent's feature vector.
- `optimize_agent`: Optimizes an agent's performance based on the lap time.
- `main`: Main function to tie all elements together.

## Plots

The program will generate plots showing:

1. Track features
2. Agent positions
3. Lap Times Progression
4. Budget Progression

## Author

Guglielmo Ferranti, PhD Student in Complex Systems, University of Catania, Italy.
