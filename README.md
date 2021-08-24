![chandralc](https://raw.githubusercontent.com/sammarth-k/chandralc/main/images/chandralc.png)

# chandralc: A Python Package for CXO Lightcurve Analysis

<p align="left">
 <a href="LICENSE.txt"><img src = "https://img.shields.io/github/license/sammarth-k/chandralc?logo=MIT"></a> <a herfF="https://python.org" target="_blank"><img src="https://img.shields.io/badge/Made%20with-Python-306998.svg"></a> <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

The `chandralc` Python package was developed to analyze Chandra X-ray Observatory lightcurves in a matter of seconds. With algorithms and programs to automatically extract, download, plot, and analyze data, it is the perfect tool to study CXO lightcurves efficiently and accurately.

To see ``chandralc`` in action, check out `<a href="https://github.com/sammarth-k/chandralc/blob/main/demo.ipynb">`the demo`</a>`.

### Features:

#### Lightcurve Extraction

Extract lightcurves from one or more ObsIDs automatically. This feautre is not yet available publicly.

#### Downloads:

- Large database of over 150,000 lightcurves from 10,000+ X-ray Sources
- Downloading extracted lightcurves from 19+ galaxies.
- Search for lightcurves with J2000 coordinates
- Retrieve galaxy from lightcurve file names

#### Convert:

- Convert FITS lightcurves to ASCII txt files

#### Analysis:

##### Observation Details

- Total counts
- Observation time (in kiloseconds)
- Count rate (kiloseconds (`rate_ks`), seconds (`rate_s`))
- Source coordinates (J2000 format)
- ObsID (Observation ID of the lightcurve)
- Galaxy (Messier or NGC)

#### Plots

- Cumulative Count plots over time to view net counts over time
- Lightcurves with custom binning to view data in the form of count rate per bin or net counts per bin over time.
- Power Spectral Density (PSD) to identify periodicity and their time periods/frequencies.
- Running Average Plot

#### State Detection

- Flares
- Eclipses

#### Astrophysics Database Connection

- NASA ADS
  - Search for listings which include the source
  - Simple usage: only one method require (`.search_ads()`)

##### Upcoming features:

- Integration with `<a href="https://github.com/sammarth-k/galaXy.lc">` galaXy.lc `</a>`
- VizeR connection

### Installation

1. Install dependencies via the `requirements.txt` file: `pip install requirements.txt`
2. Install the `chandralc` package via PIP: `pip install chandralc`

[more details coming soon]

##### Cite chandralc

If you use ``chandralc`` in your research, please cite it as follows:

```tex
@MISC{chandralc,
	author = {{Kumar}, Sammarth},
	title = "{chandralc: Python Package for CXO Lightcurve Analysis}",
	keywords = {Software, Chandra, CXO, lightcurves },
	url = {https://github.com/sammarth-k/chandralc},
	publisher = {\url{{https://github.com/sammarth-k/chandralc}}},
	year = {2021},
	month = {May},
}
```
