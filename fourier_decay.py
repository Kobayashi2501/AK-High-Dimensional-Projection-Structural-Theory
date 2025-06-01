
import numpy as np
import matplotlib.pyplot as plt

def compute_dyadic_shells(u_hat, max_shell=None):
    """
    Compute dyadic shell energies from the Fourier-transformed velocity field.
    
    Parameters:
        u_hat : np.ndarray
            Fourier-transformed velocity field, shape (Nx, Nx, Nx, 3)
        max_shell : int or None
            Maximum shell index to consider. If None, determined from input size.
    
    Returns:
        energy_shells : list
            List of energy values per dyadic shell.
    """
    Nx = u_hat.shape[0]
    kx = np.fft.fftfreq(Nx) * Nx
    ky = np.fft.fftfreq(Nx) * Nx
    kz = np.fft.fftfreq(Nx) * Nx
    KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing='ij')
    k_mag = np.sqrt(KX**2 + KY**2 + KZ**2)
    max_k = np.max(k_mag)
    if max_shell is None:
        max_shell = int(np.floor(np.log2(max_k))) + 1

    energy_shells = []
    for j in range(max_shell):
        mask = (k_mag >= 2**j) & (k_mag < 2**(j+1))
        shell_energy = np.sum(np.abs(u_hat[mask])**2)
        energy_shells.append(shell_energy)
    return energy_shells

def analyze_decay(energy_shells, show_plot=True):
    """
    Compute and plot log-log slope of dyadic shell energy decay.
    """
    j = np.arange(len(energy_shells))
    logE = np.log10(np.maximum(energy_shells, 1e-16))  # Avoid log(0)
    slope, intercept = np.polyfit(j, logE, 1)

    if show_plot:
        plt.figure(figsize=(6, 4))
        plt.plot(j, logE, 'o-', label='log10(E_j)')
        plt.plot(j, slope * j + intercept, 'r--', label=f'Fit: slope = {slope:.2f}')
        plt.title('Dyadic Shell Energy Decay')
        plt.xlabel('Shell Index j')
        plt.ylabel('log10 E_j')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    return slope
