import os
import shutil

def save_files(output_dir):
    """
    Copies files from the package's data directory to the specified output directory.
    
    Args:
        output_dir (str): Path to the local directory where files will be saved.
    """
    # Get the path to the package's data directory
    package_dir = os.path.dirname(__file__)
    data_dir = os.path.join(package_dir, "data")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Copy each file from the package's data directory to the output directory
    for file_name in os.listdir(data_dir):
        src_file = os.path.join(data_dir, file_name)
        dest_file = os.path.join(output_dir, file_name)
        shutil.copy(src_file, dest_file)
        print(f"Copied {file_name} to {output_dir}")