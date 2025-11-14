import numpy as np
import matplotlib.pyplot as plt

def plot_transformation(A, v1, v2, vector_name="v"):
    # Apply transformation
    Av1 = A @ v1
    Av2 = A @ v2

    plt.figure(figsize=(6,6))

    # Original vectors
    plt.quiver(0,0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label=f'{vector_name}1')
    plt.quiver(0,0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='green', label=f'{vector_name}2')

    # Transformed vectors
    plt.quiver(0,0, Av1[0], Av1[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'A{vector_name}1')
    plt.quiver(0,0, Av2[0], Av2[1], angles='xy', scale_units='xy', scale=1, color='purple', label=f'A{vector_name}2')

    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    plt.grid()
    plt.gca().set_aspect("equal")
    plt.legend()
    plt.show()
