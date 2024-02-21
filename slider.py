import streamlit as st
import numpy as np
import  matplotlib.pyplot as plt

x = st.slider('Pilih Rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Pilih Rentang', 0.0, 10.0, 5.0)
st.write('nilai y:', y)
def f(x):
  return 18 * x ** 2 + x - 10
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

t = np.linspace(x[0]*np.pi, x[1]*np.pi, 100)
u = np.sin(y*t)
st.write('nilai t:', t)

fig, ax = plt.subplots(figsize=(16,8))
ax.plot(t, u, label='sin(t)', color='b') #plotting sin(t) curve
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis ='y', labelsize = 20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth= .5)
st.pyplot(fig)

# Create a slider for x values
x_values = st.slider('Pilih Rentang X', -10.0, 10.0, (0.0, 1.0))
y_values = st.slider('Pilih Rentang Y', -100.0, 100.0, (0.2, 0.5))
# Generate x values for the function
x = np.linspace(x_values[0], x_values[1], 100)
def animate_slider():
    slider_placeholder = st.empty()
    for x_val in np.linspace(-10, 10, 100):
        slider_placeholder.slider('Pilih Rentang X', -10.0, 10.0, x_val)
animate_slider()

# Calculate corresponding y values
y = f(x)
st.write('nilai y:', y)
# Plot the function
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, label='$f(x) = 18x^2 + x - 10$', color='b')
ax.fill_between(x, y, where=((x >= x_values[0]) & (x <= x_values[1])), color='black', alpha=0.5)  # Shading the integral area
ax.set_xlabel('x')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Graph of $f(x) = 18x^2 + x - 10$')
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Calculate the definite integral
integral_value = trapezoidal_rule(f, x_values[0], x_values[1], 1000)  # Using 1000 intervals
st.write(f"The definite integral over the interval [{x_values[0]}, {x_values[1]}] is: {integral_value}")

