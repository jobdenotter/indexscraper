# Stock Index Weights Retriever

## Description

This is a simple Python package for retrieving the weights of the stocks in a given index. At the moment, it supports retrieving the weights of the stocks in the NASDAQ 100 index, the S&P 500 index, and the Dow Jones Industrial Average index. It retrieves this data from the [slickcharts.com](https://www.slickcharts.com/) website.

## Installation

To install this package, run the following command:

```bash
pip install indexweights
```

You need to have Python 3.6 or higher installed on your system. If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/).

You also need to have the chromedriver and Google Chrome installed on your system. You can download the chromedriver from [here](https://chromedriver.chromium.org/downloads). Easiest is to put the chromedriver executable in the same directory as your Python script. Make sure to download the version that matches your Google Chrome version. You can check your Google Chrome version by going to the following URL in Google Chrome: `chrome://settings/help`.

## Usage

Web scraping can damage the website you are scraping from. Please use this package responsibly.

Example usage:

```python
from indexweights import get_nasdaq_index_data

data = get_nasdaq_index_data()
print(data)
```
