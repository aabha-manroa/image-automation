import os
from PIL import Image

# Paths for the greyscale images and output folder
input_folder = r'C:\\Users\\DELL\\OneDrive\\Documents\\image automation\\outputfolder2'  # Your folder with greyscale images
output_folder = r'C:\\Users\\DELL\\OneDrive\\Documents\\image automation\\outputfolder3'  # Your output folder for resized images


# Scale images to 10% of their original size and save them
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Assuming JPG and PNG files
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path)
        
        # Get the original size
        width, height = img.size
        
        # Scale the image to 10% of its original size
        new_size = (int(width * 0.1), int(height * 0.1))
        resized_img = img.resize(new_size)
        
        # Save the resized image to the output folder
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)
        print(f"Scaled {filename} to 10% and saved to {output_folder}")
