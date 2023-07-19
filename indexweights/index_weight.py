from dataclasses import dataclass


@dataclass
class IndexWeight:
    """Dataclass for index weight. Used to store data from html table retrieved from Nasdaq website"""

    instrument_name: str
    instrument_symbol: str
    weight: float
