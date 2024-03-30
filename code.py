import os
import random
import time
from PIL import Image

# Function to display image
def display_image(image_path):
    image = Image.open(image_path)
    image.show()

# Function to load images
def load_images(image_dir):
    images = {'angry': [], 'happy': [], 'neutral': []}
    for folder_name in os.listdir(image_dir):
        folder_path = os.path.join(image_dir, folder_name)
        if os.path.isdir(folder_path):
            emotion = folder_name.lower()
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    images[emotion].append(file_path)
    return images

# Load images
image_dir = 'images'  # Modify this to your image directory path
images = load_images(image_dir)

# Instructions
print('Press Enter when you see an angry face.')
input('Press Enter to start...')

# Main loop
while True:
    # Present a sequence of images
    for _ in range(5):
        image_path = random.choice(images['angry'])
        display_image(image_path)
        input('Press Enter to continue...')
    for _ in range(5):
        image_path = random.choice(images['neutral'])
        display_image(image_path)
        input('Press Enter to continue...')
    
    # Inter-trial interval
    time.sleep(1.0)
    
    # Check for input to exit
    if input('Press q to quit, or Enter to continue: ').lower() == 'q':
        break
