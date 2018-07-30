# Jumo-Test

This is an technical assignment from JUMO. This project reads an excel files and the result is a file called Output.csv with a line detailing the totals by the tuple of (Network, Product, Month) summing the amount and count of loans.

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

Table of Contents
-----------------

  * [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Assumptions](#assumptions)
  * [Authors](#authors)

## Getting Started

To get this project up and running on your computer, clone or download the project on your local machine and run jumo-test.py

### Prerequisites

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


### Installation

To get you local environment running, install the prerequisites from the requirements.txt and then run jumo-test.py

```
pip install -r requirements.txt
```
## Assumptions

There are several assumptions that I've made in the course of building this project.

1. I've assumed the order of the columns on the Loans.csv will always remain the same.
2. I've also assumed the loans amount column will always have number values.
3. I've also assumed that the date format column will always a correct date format.

## Authors

* **Daniel Irungu** - *Initial work* - [dan214](https://github.com/dan214)


