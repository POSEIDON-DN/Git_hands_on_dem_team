import os
import matplotlib.pyplot as plt
directory_path = r"C:\Users\MishraGK/myproject/Git_hands_on"
os.chdir(directory_path)
os.startfile(directory_path)
import h5py

# Open the data file
with h5py.File('sim_data_triaxial_compression.hdf5', 'r') as hdf_file:
    # Access metadata
    metadata = hdf_file['metadata']
    
    # Access a specific realization
    group = hdf_file['1']
    macro_stress = group['macro_stress'][:]
    macro_domain = group['macro_domain'][:]    
    particle_features = group['particle_features'][:]
    interaction_features_1 = group['interaction_features/1'][:]
    print(macro_stress.shape)
    stress = macro_stress.sum(axis=1)
    plt.plot(-stress) 
    plt.xlabel("Time step")
    plt.ylabel("Stress")
    plt.show()
    