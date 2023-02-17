# Acoustic glitches

This is a fork of [kuldeepv89/GlitchPy](https://github.com/kuldeepv89/GlitchPy).

This repository can be used to study the glitch signatures arising from the helium ionization zone and the base of convective envelope. Their properties can be extracted following two different approaches:

1. by fitting individual oscillation frequencies
2. by fitting second differences of frequencies w.r.t. the radial order.  

The above methods are described in Verma et al. (2019) in some detail (https://ui.adsabs.harvard.edu/abs/2019MNRAS.483.4678V/abstract).

## Changes

* Package code into `glitchpy`
* Add pip-install functionality

## Requirements

* GNU Fortran (GCC 12.2.0)
* Python (3.6 to 3.11)

## Installation

To install the latest version of this package to your Python environment, use these commands in your terminal emulator,

```bash
git clone https://github.com/alexlyttle/GlitchPy.git
pip install GlitchPy
```

## Testing

The test case is the star 16 Cyg A. Run,

```bash
python 16cyga.py
```

and check it completes without error.
