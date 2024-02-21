import streamlit as st
import numpy as np
import  matplotlib.pyplot as plt

x = st.slider('Pilih Rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Pilih Rentang', 0.0, 10.0, 5.0)
st.write('nilai y:', y)
def f(x):
  return 18 * x ** 2 + x - 10
# Define the trapezoidal rule for numerical integration
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


# Create a slider for selecting the integral interval
integral_interval = st.slider('Pilih Rentang Integral', -10.0, 10.0, (-5.0, 5.0))

# Generate x values for the function
x = np.linspace(-10, 10, 100)

# Calculate corresponding y values for the function
y = f(x)

# Plot the function
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, label='$f(x) = 18x^2 + x - 10$', color='b')

# Calculate the definite integral using trapezoidal rule
integral_value = trapezoidal_rule(f, integral_interval[0], integral_interval[1], 1000)  # Using 1000 intervals
st.write(f"The definite integral over the interval [{integral_interval[0]}, {integral_interval[1]}] is: {integral_value}")

# Show the selected interval on the plot
ax.fill_between(x, y, where=((x >= integral_interval[0]) & (x <= integral_interval[1])), color='skyblue', alpha=0.5)

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Graph of $f(x) = 18x^2 + x - 10$ with Selected Integral Interval')
ax.grid(True)
ax.legend()

st.pyplot(fig)

