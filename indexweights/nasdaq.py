from bs4 import BeautifulSoup


from . import html_getter
from .index_weight import IndexWeight


URL = "https://www.slickcharts.com/nasdaq100"


def _parse_html(html: str) -> list[IndexWeight]:
    """Extract index data from html table retrieved from Nasdaq website"""
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")

    index_data = []
    for row in table.tbody.find_all("tr"):
        columns = row.find_all("td")

        index_data.append(
            IndexWeight(
                instrument_name=columns[1].a.text,
                instrument_symbol=columns[2].a.text,
                weight=float(columns[3].text),
            )
        )

    return index_data


def get_index_data() -> list[IndexWeight]:
    """Get index data from Nasdaq website"""
    html = html_getter.get(URL)
    index_data = _parse_html(html)
    return index_data
