
import numpy as np

def divergence_free_projection(u_hat, kx, ky, kz):
    """
    Project velocity field in Fourier space onto divergence-free subspace.
    """
    k_squared = kx**2 + ky**2 + kz**2
    k_squared[k_squared == 0] = 1  # avoid divide-by-zero
    k_dot_u = kx * u_hat[..., 0] + ky * u_hat[..., 1] + kz * u_hat[..., 2]
    for i, k in enumerate([kx, ky, kz]):
        u_hat[..., i] -= (k * k_dot_u) / k_squared
    return u_hat

def compute_nonlinear_term(u, kx, ky, kz):
    """
    Compute non-linear term (u · ∇)u in spectral space.
    """
    u_hat = np.fft.fftn(u, axes=(0,1,2))
    grad_u = np.stack([np.fft.ifftn(1j * k * u_hat, axes=(0,1,2)).real for k in [kx, ky, kz]], axis=-1)
    nonlinear = np.sum(u[..., None] * grad_u, axis=3)
    return np.fft.fftn(nonlinear, axes=(0,1,2))

def simulate_nse(u0, f, nu, dt, T, Nx):
    """
    Full pseudo-spectral 3D incompressible NSE solver (Fourier-based).

    Parameters:
        u0 : np.ndarray
            Initial velocity field of shape (Nx, Nx, Nx, 3)
        f : np.ndarray
            Forcing term (constant), shape (Nx, Nx, Nx, 3)
        nu : float
            Viscosity
        dt : float
            Time step
        T : float
            Final time
        Nx : int
            Grid size (assumes cubic domain)

    Returns:
        snapshots : np.ndarray
            Array of velocity field snapshots, shape (steps, Nx, Nx, Nx, 3)
    """
    u = u0.copy()
    steps = int(T / dt)
    snapshots = []

    # Define wave numbers
    k1d = np.fft.fftfreq(Nx) * Nx
    KX, KY, KZ = np.meshgrid(k1d, k1d, k1d, indexing='ij')
    kx, ky, kz = [2j * np.pi * K for K in (KX, KY, KZ)]
    k_squared = kx**2 + ky**2 + kz**2
    k_squared[k_squared == 0] = 1  # avoid divide-by-zero

    # FFT of forcing
    f_hat = np.fft.fftn(f, axes=(0,1,2))

    for step in range(steps):
        u_hat = np.fft.fftn(u, axes=(0,1,2))
        u_hat = divergence_free_projection(u_hat, kx, ky, kz)

        nonlinear_hat = compute_nonlinear_term(u, kx, ky, kz)

        # Semi-implicit update: u_hat ← (u_hat - dt * nonlinear + dt * f_hat) / (1 + dt * nu * k²)
        for i in range(3):
            u_hat[..., i] = (u_hat[..., i] - dt * nonlinear_hat[..., i] + dt * f_hat[..., i]) / (1 + dt * nu * k_squared)

        u_hat = divergence_free_projection(u_hat, kx, ky, kz)
        u = np.fft.ifftn(u_hat, axes=(0,1,2)).real

        snapshots.append(u.copy())

    return np.array(snapshots)
