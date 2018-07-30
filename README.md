# Jumo-Test

This is an technical assignment from JUMO. This project reads an excel files and the result is a file called Output.csv with a line detailing the totals by the tuple of (Network, Product, Month) summing the amount and count of loans.

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

Table of Contents
-----------------

  * [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Languages](#languages)
  * [Installation](#installation)
  * [Performance and Scaling](#performance-and-scaling)
  * [Assumptions](#assumptions)
  * [Authors](#authors)

## Getting Started

To get this project up and running on your computer, clone or download the project on your local machine and run jumo-test.py

## Prerequisites

You will need to install Pandas and Python 3.6 to get up and running. There is a requirements.txt for this

```
Pandas for data analysis
```
## Languages

### Python 3.6
The reason for using Python is that it is simple enough for things to happen (really) quickly and powerful enough to allow the implementation of the most complex ideas. In addition, it has a lot (tons) of pre-built packages (most things are ready to use)

### Pandas(Python Library)
I've used Pandas for data analysis. It gives Python the ability to work with spreadsheet-like data for fast data loading, manipulating, aligning, and merging, among other functions

### Dateutil (Python module)
I've used this python module to parse the date string into known formats to represent date and time. In our case, month.


## Installation

To get you local environment running, install the prerequisites from the requirements.txt and then run jumo-test.py

```
pip install -r requirements.txt
```

## Performance and Scaling

Since we are dealing with small amounts of data currently, preformance should not be a problem. However, if the Loans.csv is a big file (100MB to severals GBs), we are likely to run into performance issues where run times are much longer, and/or cause code to fail entirely to insufficicent memory.

A few things to consider in this scenario:

1. #### Use other tools suited to handle large amounts of data - While tools like Spark and Dask can handle large data sets (100 gigabytes to multiple terabytes), taking full advantage of their capabilities usually requires more expensive hardware. And unlike pandas, they lack rich feature sets for high quality data cleaning, exploration, and analysis. For medium-sized data, we're better off trying to get more out of pandas, rather than switching to a different tool. 

2. #### Processing chunks of the data - This involved loading chunks of it into RAM, and processing each chunk before loading the next chunk.

3. #### Increase the RAM of the development server

## Assumptions

There are several assumptions that I've made in the course of building this project.

1. I've assumed the order of the columns on the Loans.csv will always remain the same.
2. I've also assumed the loans amount column will always have number values.
3. I've also assumed that the date format column will always a correct date format.

## Authors

* **Daniel Irungu** - *Initial work* - [dan214](https://github.com/dan214)


