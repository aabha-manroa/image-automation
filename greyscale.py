import os
from PIL import Image

# Paths for the downloaded images and output folder
input_folder = r'C:\\Users\\DELL\\OneDrive\\Documents\\image automation\\outputfolder1'  # Your folder with downloaded images
output_folder = r'C:\\Users\\DELL\\OneDrive\\Documents\\image automation\\outputfolder2'     # Your output folder for greyscale images

# Convert images to greyscale and save them
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Assuming JPG and PNG files
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path).convert("L")  # Convert to greyscale (L mode)
        
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)
        print(f"Converted {filename} to greyscale and saved to {output_folder}")
