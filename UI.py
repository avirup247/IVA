import tkinter as tk
import pyttsx3
import numpy as np
import matplotlib.pyplot as plt
import threading

# Initialize speech engine
engine = pyttsx3.init()

# Define function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define function to handle "Speak" button click
def speak_command():
    command = entry.get()
    speak(command)
    # Start spectrum thread
    spectrum_thread = threading.Thread(target=show_spectrum)
    spectrum_thread.start()

# Define function to show spectrum
def show_spectrum():
    # Create random spectrum data
    data = np.random.rand(100) * 100
    # Create spectrum plot
    plt.plot(data)
    plt.title("Voice Response Spectrum")
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.show()

# Create UI
root = tk.Tk()
root.title("Sci-fi AI Voice UI")
root.geometry("600x400")
root.configure(background="black")

# Create text entry box
entry = tk.Entry(root, width=50, font=("Arial", 20))
entry.pack(pady=20)

# Create "Speak" button
button = tk.Button(root, text="Speak", command=speak_command, font=("Arial", 20))
button.pack(pady=20)

# Create label for spectrum plot
label = tk.Label(root, text="Voice Response Spectrum", font=("Arial", 20), bg="black", fg="white")
label.pack()

root.mainloop()