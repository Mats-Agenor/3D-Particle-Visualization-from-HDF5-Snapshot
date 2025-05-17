#3D Particle Visualization from HDF5 Snapshot
-------------------------------------------------
This Python script visualizes particle data from GADGET-style HDF5 simulation snapshots in 3D space. The tool is particularly useful for analyzing cosmological simulations or astrophysical systems.

**Features**

Loads particle positions from HDF5 files (GADGET-4 format)

Supports different particle types (gas, dark matter, stars)

Converts coordinates from centimeters to kiloparsecs (kpc) for better visualization

Creates interactive 3D scatter plots with:

Optional mass-dependent point sizing

Subsampling for large datasets

Customizable viewing angles

Clean, publication-quality styling

**Usage**

Specify your HDF5 snapshot file path

Select particle type (0=gas, 1=dark matter, 4=stars)

Adjust subsampling rate if needed for large datasets

Run the script to generate an interactive 3D visualization

**Current Capabilities**

You can read positions of Dark Matter particles (ParType1) and Stars (ParType4). Note that visualization becomes more computationally intensive with larger particle counts.

**Future Improvements**

Planned enhancements include:

Implementation of Gaussian kernels for gas particles

SPH-like density visualization capabilities

