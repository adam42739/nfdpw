from setuptools import setup

setup(
    name="nfldpw",
    version="0.1.0",
    description="Wrapper for nfl_data_py",
    url="https://github.com/adam42739/nfldpw",
    author="Adam Lynch",
    author_email="aclynch@umich.edu",
    license="MIT License",
    packages=[
        "nfldpw",
        "nfldpw.cache",
        "nfldpw.pbp",
        "nfldpw.schedules",
        "nfldpw.rosters",
        "nfldpw.players"
    ],
    install_requires=[
        "nfl_data_py>=0.3.3",
        "requests>=2.32.3",
        "lxml>=5.3.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licesnse :: MIT License",
        "Operating System :: OS Independent",
    ],
)
