# Stock Index Weights Retriever

## Description

This is a simple Python package for retrieving the weights of the stocks in a given index. At the moment, it only supports the Nasdaq-100 index, but it can be easily extended to support other indices.

## Usage

Web scraping can damage the website you are scraping from. Please use this package responsibly.

```python
from indexweights import get_nasdaq_index_data

data = get_nasdaq_index_data()
print(data)
```
