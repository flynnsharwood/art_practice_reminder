import os
import random
import datetime
import time
from PIL import Image
from tkinter import Tk, Label, Button

# Set the directory containing the images
image_directory = r"C:\path\to\directory"

# Get a list of the images in the directory and its subfolders
images = []
for root, dirs, files in os.walk(image_directory):
    for file in files:
        images.append(os.path.join(root, file))

# Set the time interval for the reminder (in seconds)
time_interval = 3600

# Open the log file for writing
log_file = open("random_reference_image_log.txt", "w")

while True:
    # Wait for the time interval
    time.sleep(time_interval)

    # Choose a random image from the list
    image = random.choice(images)

    # Open the image file with PIL
    img = Image.open(image)

    # Display the image on the screen
    img.show()

    # Create a window with a close button
    window = Tk()
    window.title("Random Reference Image Reminder")
    window.geometry("900x400")
    window.resizable(False, False)
    Label(window, text=f"Time to draw a random reference image! Your image is {image}").pack()

    # Get the current time
    current_time = datetime.datetime.now()

    # Write a log message to the log file
    log_file.write(f"Displayed image {image} at {current_time}\n")

    # Calculate the time 5 minutes in the future
    future_time = current_time + datetime.timedelta(seconds=300)

    # Keep the window open until the current time is equal to or greater than the future time
    while datetime.datetime.now() < future_time:
        window.update()
    
    # Destroy the window
    window.destroy()

    # Close the image
    img.close()


# Close the log file
log_file.close()
