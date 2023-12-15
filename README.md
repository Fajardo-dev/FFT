This code analyzes the frequency content of a simple sine wave using the Fast Fourier Transform (FFT).

Functionality:
Imports necessary libraries: NumPy and Matplotlib.
Defines the sampling rate, time vector, and signal frequency.
Generates a sine wave signal with the specified frequency.
Calculates the FFT of the signal.
Extracts the frequency components from the FFT result.
Plots the original signal in the time domain and the frequency spectrum.
Code Breakdown:
Imports:
numpy: Used for mathematical operations and array manipulation.
matplotlib.pyplot: Used for data visualization.
Variables:
fs: Sampling rate (1000 Hz in this example).
t: Time vector based on the sampling rate.
f1: Signal frequency (5 Hz in this example).
signal: A NumPy array containing the sine wave data.
fft_result: The result of applying the FFT to the signal.
frequencies: An array containing the corresponding frequencies for each element in fft_result.
Calculations:
np.sin(2 * np.pi * f1 * t): Generates the sine wave signal with frequency f1.
np.fft.fft(signal): Calculates the FFT of the signal.
np.fft.fftfreq(len(fft_result), 1/fs): Extracts the corresponding frequencies for each element in fft_result.
Plots:
Subplot 1: Shows the original sine wave in the time domain.
Subplot 2: Shows the magnitude of the frequency components obtained from the FFT (frequency spectrum).
Usage:
Run the code in your Python environment.
The script will generate two subplots:
The first subplot displays the original sine wave in the time domain.
The second subplot displays the frequency spectrum, showing the amplitude of each frequency component present in the signal.
Notes:
This code is a basic example of frequency spectrum analysis using the FFT.
More complex signals and advanced analysis techniques can be implemented using similar principles.
