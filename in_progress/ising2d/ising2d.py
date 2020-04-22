import cupy
import numpy
import matplotlib.pyplot as plt
from tqdm import tqdm

def interactions(a, np=numpy):
    return np.roll(a, 1, 0) + np.roll(a, 1, 1) + np.roll(a, -1, 0) + np.roll(a, -1, 1)

@profile
def half_iteration(a, mask, J = 1, beta = 1, np=numpy):
    deltaE = 2 * J * a * interactions(a, np=np)
    boltzmann = np.exp(-beta * deltaE) * mask
    flip_these = np.random.random(a.shape) < boltzmann
    a[flip_these] *= -1


@profile
def full_iteration(a, mask, J = 1, beta = 1, np=numpy):
    # this now becomes a VERY thin wrapper!
    half_iteration(a, mask, J, beta, np=np)
    half_iteration(a, 1-mask, J, beta, np=np)

def magnetization(a, np = numpy):
    mean_value = float(a.mean())
    std = float(a.std())
    return mean_value, std

def internal_energy(a, J = 1, np=numpy):
    current_energy = -J * a * interactions(a, np=np)
    mean_value = float(current_energy.mean())
    std = float(current_energy.std())
    return mean_value, std

Onsager_critical_temperature = 2 / numpy.log(1 + 2**0.5)

def plots(T_range, E, dE, M, dM, plotting=True):
    Cv = dE**2 / 1 / T_range**2
    if plotting:
        plt.plot(T_range, E)
        plt.xlabel(r"Temperature [in units where $k_B = 1$]")
        plt.ylabel("Average energy per spin")
        plt.xlim(T_range.min(), T_range.max());
        plt.vlines(Onsager_critical_temperature, E.min(), E.max())

        plt.figure()

        plt.plot(T_range, M)
        plt.xlabel(r"Temperature [in units where $k_B = 1$]")
        plt.ylabel("Average magnetization")
        plt.xlim(T_range.min(), T_range.max());
        plt.vlines(Onsager_critical_temperature, M.min(), M.max())


        plt.figure()
        plt.plot(T_range, Cv, "o-")
        plt.xlabel(r"Temperature [in units where $k_B = 1$]")
        plt.ylabel("Heat capacity per spin")
        plt.xlim(T_range.min(), T_range.max());
        plt.vlines(Onsager_critical_temperature, Cv.min(), Cv.max())

    return T_range[numpy.argmax(Cv)]

T_range = numpy.linspace(1.5, 3.5, 300)
k_b = 1

@profile
def simulation(iterations, size, T_range=T_range, k_b=k_b, plotting=True, np=numpy):
    energies = []
    energies_std = []
    magnetizations = []
    magnetizations_std = []
    a_mask = np.ones(size)
    a_mask[::2, ::2] = 0
    a_mask[1::2, 1::2] = 0
    # T_range = np.sort(np.concatenate((np.linspace(0.5, 5, 50), np.linspace(Tc-0.1, Tc+0.1, 20))))
    for T in tqdm(T_range):
        beta = 1 / (k_b * T)
        a = np.ones(size)
        E_mean = 0.0
        E_std = 0.0
        M_mean = 0.0
        M_std = 0.0
        for i in range(iterations):
            energy = internal_energy(a, np=np)
            E_mean += energy[0]
            E_std += energy[1]
            magnet = magnetization(a, np=np)
            M_mean += magnet[0]
            M_std += magnet[1]
            full_iteration(a, a_mask, beta=beta, np=np)
        energies.append(E_mean / iterations)
        magnetizations.append(M_mean / iterations)
        energies_std.append(E_std / iterations)
        magnetizations_std.append(M_std / iterations)      

    E = numpy.array(energies)
    dE = numpy.array(energies_std)
    M = numpy.array(magnetizations)
    dM = numpy.array(magnetizations_std)
    return plots(T_range, E, dE, M, dM, plotting)

if __name__ == "__main__":
    simulation(100, (64, 64), np=cupy)
