# nfldpw

## Introduction

nfldpw wraps [nfl_data_py](https://github.com/nflverse/nfl_data_py) providing full data caching and built-in documentation for column headers via `.__doc__` docstrings.

## Installation

```python
pip install git+https://github.com/adam42739/nfldpw.git#egg=nfldpw
```

## Package structure

```
nfldpw
|__ pbp
|    |__ cols
|__ players
|    |__ cols
|__ rosters
|    |__ cols
|__ schedules
     |__ cols
```

## General Usage

### Getting data

```python
>>> df = nfldpw.pbp.get([2022, 2023], "path_to_cache/")
```

### Manipulating Data

Headers names and categorical values are given for most data columns. This is intended for added convenience and is not necessary for general usage.

```python
>>> import nfldpw.pbp.cols as cols
>>>
>>> middle_passes = df[df[cols.PassLocation.header] == cols.PassLocation.MIDDLE]
```
