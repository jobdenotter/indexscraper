from enum import Enum
import re

from .index_weight import IndexWeight
from . import html_getter


ROOT_URL = "https://www.slickcharts.com/"

class IndexUrl(Enum):
    NASDAQ = "nasdaq100"
    DOW_JONES = "dowjones"
    S_AND_P = "sp500"


def get_nasdaq_index_data() -> list[IndexWeight]:
    """Get Nasdaq index data from Nasdaq website"""
    return _get_index_data(IndexUrl.NASDAQ)

def get_dow_jones_index_data() -> list[IndexWeight]:
    """Get Dow Jones index data from Nasdaq website"""
    return _get_index_data(IndexUrl.DOW_JONES)

def get_s_and_p_index_data() -> list[IndexWeight]:
    """Get S&P 500 index data from Nasdaq website"""
    return _get_index_data(IndexUrl.S_AND_P)


def _get_index_data(index: IndexUrl) -> list[IndexWeight]:
    """Get index data from SlickCharts website"""
    html = html_getter.get(ROOT_URL + index.value)
    index_data = _parse_html(html)
    return index_data


def _parse_html(html_data):
    pattern = (
        r"<tr>\s*<td>\d+</td>\s*<td><a href=\"[^\"]+\">(.*?)</a></td>\s*<td><a href=\"[^\"]+\">(.*?)</a></td>\s*"
        r"<td>([\d.]+)</td>"
    )

    index_weights = []
    matches = re.findall(pattern, html_data)
    for match in matches:
        instrument_name = match[0]
        instrument_symbol = match[1]
        weight = float(match[2])

        index_weight = IndexWeight(
            instrument_name=instrument_name,
            instrument_symbol=instrument_symbol,
            weight=weight
        )

        index_weights.append(index_weight)

    return index_weights
