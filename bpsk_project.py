import numpy as np
import matplotlib.pyplot as plt

# Generate binary data
data = np.random.randint(0, 2, 10)
print("Binary Data:", data)

# Time axis
bit_duration = 1
samples_per_bit = 100
t = np.linspace(0, bit_duration, samples_per_bit)

# Carrier signal
fc = 5
carrier = np.cos(2 * np.pi * fc * t)

# BPSK Modulation
bpsk_signal = []

for bit in data:
    if bit == 1:
        signal = np.cos(2 * np.pi * fc * t)
    else:
        signal = -np.cos(2 * np.pi * fc * t)

    bpsk_signal.extend(signal)

# Convert to numpy array
bpsk_signal = np.array(bpsk_signal)

# Add noise
noise = np.random.normal(0, 0.5, len(bpsk_signal))
noisy_signal = bpsk_signal + noise

# Demodulation
received_data = []

for i in range(0, len(noisy_signal), samples_per_bit):
    segment = noisy_signal[i:i+samples_per_bit]
    product = segment * carrier

    if np.sum(product) > 0:
        received_data.append(1)
    else:
        received_data.append(0)

print("Recovered Data:", received_data)

# Plot signals
plt.figure(figsize=(10, 4))
plt.plot(bpsk_signal)
plt.title("BPSK Signal")
plt.grid()

plt.figure(figsize=(10, 4))
plt.plot(noisy_signal)
plt.title("Noisy Signal")
plt.grid()

plt.show()