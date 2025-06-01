
import numpy as np
from sklearn.manifold import Isomap
from ripser import ripser
from persim import plot_diagrams
import matplotlib.pyplot as plt

def embed_and_analyze(snapshots, n_neighbors=10, n_components=2, show_plot=True):
    """
    Apply Isomap dimensionality reduction to the orbit snapshots and compute persistent homology (PH₁).

    Parameters:
        snapshots : np.ndarray
            Array of shape (n_samples, ...) representing time-series snapshots of the velocity field.
        n_neighbors : int
            Number of neighbors to use for Isomap.
        n_components : int
            Target dimension for Isomap embedding.
        show_plot : bool
            Whether to display the persistence diagram.

    Returns:
        diagrams : list of np.ndarray
            Persistent homology diagrams up to dimension 1.
    """
    if not isinstance(snapshots, np.ndarray):
        raise TypeError("snapshots must be a NumPy array.")

    # Flatten each snapshot if multidimensional
    if snapshots.ndim > 2:
        snapshots = snapshots.reshape((snapshots.shape[0], -1))

    if snapshots.shape[0] <= n_neighbors:
        raise ValueError("Number of snapshots must be greater than number of Isomap neighbors.")

    # Apply Isomap for dimensionality reduction
    isomap = Isomap(n_neighbors=n_neighbors, n_components=n_components)
    orbit_embedded = isomap.fit_transform(snapshots)

    # Compute persistent homology (PH₁)
    result = ripser(orbit_embedded, maxdim=1)
    diagrams = result['dgms']

    # Plot diagrams
    if show_plot:
        plot_diagrams(diagrams, show=True)

    return diagrams
