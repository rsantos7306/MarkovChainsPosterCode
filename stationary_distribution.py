# SIMULATION VERSION
# Libraries
import numpy as np
import random

# 0 is sunny, 1 is cloudy, 2 is snowy
initial_state = 0
state_counter = np.zeros(3, dtype=float)

# Transition Matrix
matA = np.array([[0.2, 0.6, 0.2],  
                 [0.3, 0,  0.7],
                  [0.5, 0, 0.5]])


# defining function to approximate standard distribution
def converge_prob(initial_state, matA, n):
    state = initial_state
    state_counter[state] += 1
    for i in range(n):
        random_state = random.choices([0, 1, 2], weights = [matA[state, 0], matA[state, 1], matA[state, 2]])
        state = random_state
        state_counter[state] +=1.0
    
    # Approximataes the probability
    for j in range(3):
        (state_counter[j]) = state_counter[j] / (n+1)
        
    return state_counter
  
# Simulations  
print(f"Now we will look at some various simulations.")
print(f"Initial state sunny, n = 5: {converge_prob(initial_state, matA, 5)}")
print(f"Initial state sunny, n = 10: {converge_prob(initial_state, matA, 10)}")
print(f"Initial state sunny, n = 20: {converge_prob(initial_state, matA, 20)}")
print(f"Initial state sunny, n = 100: {converge_prob(initial_state, matA, 100)}")
print(f"Initial state sunny, n = 100000: {converge_prob(initial_state, matA, 100000)}")
print(f"Initial state cloudy, n = 100000: {converge_prob(1, matA, 100000)}")
print(f"Initial state snowy, n = 100000: {converge_prob(2, matA, 100000)}")



# USING LINEAR ALGEBRA
# Libraries
import numpy as np

# Calculating the probabilities using eigenvalue calculations
# Matrix defining the different probabilities from state to state of form 
# (rows = outgoing state, columns = incoming state) and order burger, pizza, hotdog
matA = np.array([[0.2, 0.6, 0.2],  
                 [0.3, 0,  0.7],
                  [0.5, 0, 0.5]])

w, v = np.linalg.eig(matA.T)

# find index for when there is eigenvalue 1
index = np.argmin(np.abs(w - 1))

# extract corresponding eigenvector
pi = np.real(v[:, index])

# normalize to sum to 1 (cuz they are probs)
pi = pi / pi.sum()

print("Convergent probabilities:", pi)
