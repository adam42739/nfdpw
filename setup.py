from setuptools import setup

setup(
    name="nfldpw",
    version="0.1.0",
    description="Wrapper for nfl_data_py",
    url="https://github.com/adam42739/nfldpw",
    author="Adam Lynch",
    author_email="aclynch@umich.edu",
    license="MIT License",
    packages=["nfldpw", "nfldpw.pbp", "nfldpw.schedules"],
    install_requires=[
        "nfl_data_py>=0.3.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licesnse :: MIT License",
        "Operating System :: OS Independent",
    ],
)
