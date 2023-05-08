import urllib.request
from PIL import ImageTk, Image
import tkinter as tk
import io

# Create the Tkinter window
def main():
    window = tk.Tk()

    # Set the window title
    window.title("ESP32-CAM Image Viewer")

    # Set the window size
    window.geometry("500x500")
    # Create a label to display the image
    image_label = tk.Label(window)
    image_label.pack()

# URL for capturing the image from ESP32-CAM
image_url = "http://192.168.43.115/capture"
#function to load the image
def load_image()->Image.Image|None:
    try:
        with urllib.request.urlopen(image_url) as url:
            # Read the image data
            image_data = url.read()

        # Create a PIL Image object from the image data
        image = Image.open(io.BytesIO(image_data))
        return image
    except Exception as e:
        # Display an error message if image capture fails
        print("Error:", e)
        return None

# Function to update the image
def update_image():
    try:
        # Open the image URL
        with urllib.request.urlopen(image_url) as url:
            # Read the image data
            image_data = url.read()

        # Create a PIL Image object from the image data
        image = Image.open(io.BytesIO(image_data))

        # Resize the image to fit the window
        image = image.resize((400, 400))

        # Create a Tkinter-compatible image
        tk_image = ImageTk.PhotoImage(image)

        # Update the image in the Tkinter window
        #image_label.configure(image=tk_image)
        #image_label.image = tk_image

    except Exception as e:
        # Display an error message if image capture fails
        print("Error:", e)

    # Schedule the next image update
    window.after(1000, update_image)

def main():

    # Start updating the image
    update_image()

    # Start the Tkinter event loop
    window.mainloop()
