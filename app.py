# Imports
import numpy as np
import matplotlib.pyplot as plt

# Example signal
fs = 1000  # Sampling Rate
t = np.arange(0, 1, 1/fs)  # Time vector
f1 = 5  # Signal frequency
signal = np.sin(2 * np.pi * f1 * t)

# Calculate the FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(fft_result), 1/fs)

# View the results
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Signal in the time domain')

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_result))
plt.title('Frequency spectrum (FFT)')
plt.xlabel('Frequency (Hz)')

plt.tight_layout()
plt.show()
