import os
import shutil

# Path for the folder to be zipped
folder_to_zip = r'C:\\Users\\DELL\\OneDrive\\Documents\\image automation\\outputfolder3'  # Your folder with resized images
output_zip_path = r'C:\\Users\\DELL\\OneDrive\\Documents\\image automation\\outputfolder3.zip'  # Path for the zip file

# Zip the contents of outputfolder3
shutil.make_archive(output_zip_path.replace('.zip', ''), 'zip', folder_to_zip)

print(f"All files in {folder_to_zip} have been zipped into {output_zip_path}")
