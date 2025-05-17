#!/usr/bin/env python3
"""
3D Particle Visualization from HDF5 Snapshot
Plots particle positions from a GADGET-style HDF5 snapshot.

"""

import h5py
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams["axes.labelsize"] = 25
plt.rcParams["xtick.labelsize"] = 14
plt.rcParams["ytick.labelsize"] = 14
plt.rcParams['font.size'] = 25
plt.rc('font', **{'family':'serif', 'serif':['Times']})
mpl.rcParams['figure.dpi'] = 100
mpl.rcParams['text.usetex'] = True
mpl.rcParams['legend.frameon'] = False
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['ytick.right'] = True
mpl.rcParams['xtick.major.size'] = 5
mpl.rcParams['xtick.minor.size'] = 3
mpl.rcParams['ytick.major.size'] = 5
mpl.rcParams['ytick.minor.size'] = 3
mpl.rcParams['xtick.major.width'] = 0.79
mpl.rcParams['xtick.minor.width'] = 0.79
mpl.rcParams['ytick.major.width'] = 0.79
mpl.rcParams['ytick.minor.width'] = 0.79



def load_particle_data(filename, part_type=0):
    """
    Load particle coordinates from HDF5 snapshot.
    
    Parameters:
        filename (str): Path to HDF5 file
        part_type (int): Particle type (0=gas, 1=DM, 4=stars, etc.)
    
    Returns:
        tuple: (x, y, z) coordinate arrays
    """
    with h5py.File(filename, 'r') as f:
        # Access particle group (e.g., PartType0 for gas)
        group = f[f'PartType{part_type}']
        
        # Load coordinates (convert from cm to kpc for better visualization)
        coords = group['Coordinates'][:] / 3.0857e21  # 1 kpc = 3.0857e21 cm
        
        # Separate into x, y, z components
        x = coords[:,0]
        y = coords[:,1]
        z = coords[:,2]
        
        # Load masses if we want size scaling
        masses = group['Masses'][:] if 'Masses' in group else None
        
    return x, y, z, masses

def plot_3d_particles(x, y, z, masses=None, subsample=1):
    """
    Create 3D scatter plot of particles.
    
    Parameters:
        x, y, z (arrays): Coordinate arrays
        masses (array): Optional mass array for size scaling
        subsample (int): Plot every nth particle for large datasets
    """
    # Create figure with 3D axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Apply subsampling if needed
    if subsample > 1:
        x = x[::subsample]
        y = y[::subsample]
        z = z[::subsample]
        if masses is not None:
            masses = masses[::subsample]
    
    # Calculate point sizes (normalized to 0.1-5.0 range)
    sizes = 0.1
    if masses is not None:
        sizes = 0.1 + 4.9 * (masses / np.max(masses))
    
    # Create scatter plot
    sc = ax.scatter(
        x, y, z,
        c='royalblue',          # Particle color
        s=sizes,                # Particle sizes
        alpha=0.3,              # Slight transparency
        edgecolors='none',      # No border on points
        depthshade=True         # Depth shading for 3D effect
    )
    
    # Axis labels with units
    ax.set_xlabel('X [kpc]', fontsize=12)
    ax.set_ylabel('Y [kpc]', fontsize=12)
    ax.set_zlabel('Z [kpc]', fontsize=12)
    
    # Title with particle count
    ax.set_title(f'3D Particle Distribution (N={len(x):,})', fontsize=14)
    
    # Remove grid lines and set background color
    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Equal aspect ratio
    ax.set_box_aspect([1,1,1])
    
    # Adjust viewing angle (elevation, azimuth)
    ax.view_init(elev=30, azim=45)
    plt.savefig(f'single_nebula_1.png')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Configuration
    SNAPSHOT_FILE = "single_nebula_1.hdf5"
    PARTICLE_TYPE = 0       # 0=gas, 1=dark matter, 4=stars
    SUBSAMPLE = 1           # Plot every nth particle (use >1 for large datasets)
    
    # Load data
    print(f"Loading particles from {SNAPSHOT_FILE}...")
    x, y, z, masses = load_particle_data(SNAPSHOT_FILE, PARTICLE_TYPE)
    
    # Plot
    print(f"Plotting {len(x):,} particles...")
    plot_3d_particles(x, y, z, masses, subsample=SUBSAMPLE)
