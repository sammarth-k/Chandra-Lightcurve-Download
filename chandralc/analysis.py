"""This module contains functions for lightcurve analysis."""

# chandralc modules
from chandralc import ml

# dependencies
import matplotlib.pyplot as plt
from scipy import signal


def psd(lightcurve):
    """Plots power spectral density for lightcurve.

    Parameters
    ----------
    lc: ChandraLightcurve
        ChandraLightcurve object
    Returns
    -------
    float
        Time period of frequency with maximum amplitude
    """

    frequency, power = signal.periodogram(lightcurve.raw_phot)
    plt.semilogx(frequency, power)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.show()

    return (1/frequency[list(power).index(max(power))])*3.241


def bin_lc(lightcurve, binsize):
    """Bins photon counts.

    Parameters
    ----------
    lc: ChandraLightcurve
        ChandraLightcurve object
    binsize : int
        Size of bin

    Returns
    -------
    list
        Array of bins
    """
    binned_photons = []

    # range: total number of df points over included bins --> temp3 of intervals
    for j in range(0, len(lightcurve)//binsize):
        temp2 = 0
        j *= binsize
        for k in range(binsize):
            # sum of all photons within one interval
            temp2 = temp2 + lightcurve[j+k]

        # appends that sum to a list
        binned_photons.append(temp2)

    return binned_photons

def bin_toarrays(lightcurve, binsize):
    """Bins photon counts.

    Parameters
    ----------
    lc: ChandraLightcurve
        ChandraLightcurve object
    binsize : int
        Size of bin

    Returns
    -------
    list
        Array of bins
    """
    binned_photons = []
    binned_time = []

    # range: total number of df points over included bins --> temp3 of intervals
    for j in range(0, len(lightcurve)//binsize):
        temp1 = []
        temp2 = 0
        j *= binsize
        for k in range(binsize):
            # sum of all photons within one interval
            temp2 = lightcurve[j+k]
            temp1.append(temp2)

        # appends that sum to a list
        binned_photons.append(temp1)

    return binned_photons

def flare_detect(lc, binsize=10):
    """Detects potential flares in lightcurves.

    Parameters
    ----------
    lc : ChandraLightcurve
        ChandraLightcurve object
    binsize : int
        Items per bin, by default 10

    Returns
    -------
    bool
        Whether flare(s) is/are detected or not
    """

    # binsize arrays of times and cumulative counts
    binned_time_arrays = analysis.bin_toarrays(lc.time_array, binsize)
    binned_count_arrays = analysis.bin_toarrays(lc.cumulative_counts, binsize)

    # Array of slopes of each bin from regression line
    slopes = [ml.regression_equation(x,y)[0] for x,y in zip(binned_time_arrays, binned_count_arrays)]

    # Replacing nan with 0
    for i in range(len(slopes)):
        if np.isnan(slopes(i)):
            slopes[i] = 0

    # array of potential flares
    potential_flares = [i * binsize * lc.chandra_bin for i in range(len(slopes)) if sigma_check(slopes,slopes[i])]

    if len(check_cluster(potential_flares,binsize)) > 0:
        return True

    return False