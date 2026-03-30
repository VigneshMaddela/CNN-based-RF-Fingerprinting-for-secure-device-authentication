import scipy.io
import numpy as np
import os

# Path to your dataset folder
dataset_path = "E:\\RF FINGERPRINTING\\dataset\\"
all_data = {}
device_files = [f"Device_{i}.mat" for i in range(1, 11)]

print("Loading data...")

for file_name in device_files:
    file_path = os.path.join(dataset_path, file_name)
    
    # Load the .mat file
    mat_data = scipy.io.loadmat(file_path)
    
    # --- This is the important part ---
    # A .mat file is a dictionary. We need to find the key for the data.
    # Let's print the keys to find the right one. 
    # It's probably not '__header__', '__version__', or '__globals__'.
    
    data_key = None
    for key in mat_data.keys():
        if not key.startswith('__'):
            data_key = key
            break
            
    if data_key:
        print(f"Loaded {file_name} (data key: '{data_key}')")
        # Store the data array in our dictionary
        all_data[file_name] = mat_data[data_key]
    else:
        print(f"Could not find data key in {file_name}")

# Now, 'all_data' is a dictionary like:
# {'Device_1.mat': array(...), 'Device_2.mat': array(...), ...}
print(f"\nSuccessfully loaded {len(all_data)} device files.")

# Example: Check the shape of the data for Device 1
# This should be (19920, 72) or (19920, 72, 2) or something similar
print(f"Raw shape for Device 1: {all_data['Device_1.mat'].shape}")