import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Bass Diffusion Model function
def bass_model(t, p, q, M):
    return (M * (p + q)**2 * np.exp(-(p + q) * t)) / (p + q * np.exp(-(p + q) * t))**2

def fit_bass_model(t, revenue): # this is a function to fit Bass model to data and return estimated parameters
    params, _ = curve_fit(bass_model, t, revenue, p0=[0.01, 0.3, 2000])
    return params  # Returns p, q, M

def predict_bass_model(years_future, p, q, M): # this is a function to generate predictions using the Bass model
    t_future = years_future - years_future[0]  # Normalize time
    return bass_model(t_future, p, q, M)

def compute_cumulative_adoption(predicted_adoption, M): # this is a function to compute cumulative adoption fraction
    return predicted_adoption / M

def compute_instantaneous_adoption(p, q, cumulative_adoption): # a function to compute instantaneous adoption rate f(t)
    return p + q * cumulative_adoption

# finnaly, I have created a function to plot all the necessary data
def plot_data(x, y, title, xlabel, ylabel, linestyle='-', marker='o', color='blue', label="Data"):
    plt.figure(figsize=(10,6))
    plt.plot(x, y, linestyle=linestyle, marker=marker, color=color, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()