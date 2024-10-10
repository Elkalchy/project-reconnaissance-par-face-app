import numpy as np
import json
import cv2
import os
from tkinter import filedialog, Tk

def create_directory(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_face_id(directory: str) -> int:
    user_ids = []
    for filename in os.listdir(directory):
        number = int(os.path.split(filename)[-1].split("-")[1])
        user_ids.append(number)
    user_ids = sorted(list(set(user_ids)))
    max_user_ids = 1 if len(user_ids) == 0 else max(user_ids) + 1
    for i in sorted(range(0, max_user_ids)):
        try:
            if user_ids.index(i):
                face_id = i
        except ValueError:
            return i
    return max_user_ids

def save_name(face_id: int, face_name: str, filename: str) -> None:
    names_json = {}
    if os.path.exists(filename):
        with open(filename, 'r') as fs:
            names_json = json.load(fs)
    names_json[face_id] = face_name
    with open(filename, 'w') as fs:
        json.dump(names_json, fs, ensure_ascii=False, indent=4)

def import_images(face_name: str):
    directory = 'images'
    create_directory(directory)
    names_json_filename = 'names.json'
    
    face_id = get_face_id(directory)
    save_name(face_id, face_name, names_json_filename)

    # Open a file dialog to select images
    Tk().withdraw()  # Prevents the root window from appearing
    image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    for count, img_path in enumerate(image_paths, start=1):
        # Read the image and save it
        img = cv2.imread(img_path)
        if img is not None:
            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'./images/Users-{face_id}-{count}.jpg', gray)
            print(f'Saved: Users-{face_id}-{count}.jpg')

    print('Success! All images imported.')

# Example usage
if __name__ == "__main__":
    name = input('Enter user name and press <return> --> ')
    import_images(name)
