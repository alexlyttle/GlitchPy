from setuptools import find_packages
from numpy.distutils.core import Extension, setup

glitch_fq = Extension(
    name="glitchpy.glitch_fq",
    sources=[
        "src/glitchpy/glitch_fq.f95",
    ]
)

glitch_sd = Extension(
    name="glitchpy.glitch_sd",
    sources=[
        "src/glitchpy/glitch_sd.f95",
    ]
)

icov_sd = Extension(
    name="glitchpy.icov_sd",
    sources=[
        "src/glitchpy/icov_sd.f95",
    ]
)

sd = Extension(
    name="glitchpy.sd",
    sources=[
        "src/glitchpy/sd.f95",
    ]
)

setup(
    name="glitchpy",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    ext_modules=[glitch_fq, glitch_sd, icov_sd, sd],
    install_requires=["matplotlib", "h5py", "scikit-learn", "seaborn", "tqdm"],
    python_requires=">=3.6,<3.12",
)
