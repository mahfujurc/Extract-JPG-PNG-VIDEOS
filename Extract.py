import os
import shutil

# Set the folder path (update this to your desired folder path)
folder_path = r"   "  # Replace with your folder path

# Define categories for images and videos
file_categories = {
    'JPG': '.jpg',
    'PNG': '.png',
    'Videos': ['.mp4', '.avi', '.mov'],  # Add more video extensions as needed
}

# Create subfolders for each category
for category, extensions in file_categories.items():
    category_folder = os.path.join(folder_path, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

# Loop through all files in the folder and move them to the appropriate subfolder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Check for .jpg files
        if file_extension == file_categories['JPG']:
            shutil.move(file_path, os.path.join(folder_path, 'JPG', filename))
            print(f"Moved: {filename} to JPG")
        
        # Check for .png files
        elif file_extension == file_categories['PNG']:
            shutil.move(file_path, os.path.join(folder_path, 'PNG', filename))
            print(f"Moved: {filename} to PNG")
        
        # Check for video files
        elif file_extension in file_categories['Videos']:
            shutil.move(file_path, os.path.join(folder_path, 'Videos', filename))
            print(f"Moved: {filename} to Videos")
