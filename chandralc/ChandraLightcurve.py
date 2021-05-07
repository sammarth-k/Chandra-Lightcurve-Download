# dependencies

# External Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# User made modules
from chandralc import convert, analysis, plot

class ChandraLightcurve(object):
    """Class for lightcurve plotting and analysis.

    Attributes
    ----------
    path: str
        Filepath
    df: pandas.core.frame.DataFrame
        DataFrame of lightcurve
    time: float
        Total observation time
    count: float
        Net photon counts of observation
    rate_ks: float
        Net count rate in kiloseconds
    rate_s: float
        Net count rate in seconds
    obsid: str
        Observation ID
    coords: str
        Source coordinates in J2000 format

    """

    def __init__(self, file):
        """Inits ChandraLightcurve class.

        Parameters
        ----------
        file : str
            Filename or filepath of raw lightcurve
        """
        self.path = file

        if "txt" in file:
            self.df = convert.txt_to_df(file, convert.header_check(file))
        elif "fits" in file:
            self.df = convert.fits_to_df(file, convert.header_check(file))

        chandra_bin = 3.241039999999654

        self.cumulative_count_arr = []

        count = 0

        # Creating counts array
        for index, row in self.df.iterrows():
            if self.df['EXPOSURE'][index] > 0:
                count += self.df.COUNTS[index]
            elif self.df['EXPOSURE'][index] == 0:
                count += 0

            self.cumulative_count_arr.append(count)

        # array for timestamps
        self.time_array = [chandra_bin / 1000 *
                           i for i in range(1, len(self.cumulative_count_arr) + 1)]

        # Lightcurve stats
        self.time = round(self.time_array[-1], 3)
        self.count = count
        self.rate_ks = round(self.count / self.time, 3)
        self.rate_s = round(self.count / (self.time * 1000), 5)

        # Source information
        file = file.split("_lc.fits")[0].split("_")
        file = file.split("/")[-1] if "/" in file else file
        self.obsid = file[1]
        self.coords = convert.extract_coords(self.path)

        # raw data
        self.raw_phot = [self.df.COUNTS[i] if self.df.EXPOSURE[i]
                         > 0 else 0 for i in range(len(self.df))]

    def lightcurve(self, binning=500.0, figsize=(15, 9), rate=True, color="blue", fontsize=25, family="sans serif", save=False):
        """Plots cumulative photon counts over time.

        Parameters
        ----------
        figsize : tuple, optional
            Size of figure in inches (length, breadth), by default (15, 9)
        color : str, optional
            Color of plotted data, by default "blue"
        fontsize : int, optional
            Fontsize of tick labels, by default 25
        family : str, optional
            Font family for text, by default 'sans serif'
        save : bool, optional
            Save figure or not, by default False
        """

        plot.lightcurve(self, binning=binning, figsize=figsize, rate=rate, color=color, fontsize=fontsize, family=family, save=save)
    
    def cumulative(self, figsize=(15, 9), color="blue", fontsize=25, family='sans serif', save=False):
        """Plot binned lightcurves over time.

        Parameters
        ----------
        binning : float, optional
            Binning in seconds, by default 500.0
        figsize : tuple, optional
            Size of figure in inches (length, breadth), by default (15, 9)
        rate : bool, optional
            Choose whether to plot count rate or net counts per bin on y-axis, by default True
        color : str, optional
            Color of plotted data, by default "blue"
        fontsize : int, optional
            Fontsize of tick labels, by default 25
        family : str, optional
            Font family for text, by default 'sans serif'
        save : bool, optional
            Save figure or not, by default False
        """

        plot.cumulative(self, figsize=figsize, color=color, fontsize=fontsize, family=family, save=save)


    def psd(self):
        """Plots power spectral density for lightcurve.

        Returns
        -------
        float
            Time period of frequency with maximum amplitude
        """

        return analysis.psd(self)

    def bin(self, binsize):
        """Bins photon counts.

        Parameters
        ----------
        binsize : int
            Size of bin

        Returns
        -------
        list
            Array of bins
        """

        return analysis.bin(self,binsize)