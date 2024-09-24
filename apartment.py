"""Apartment example."""
import math
from typing import List
from dataclasses import dataclass
from cs110 import expect, summarize


@dataclass
class Apartment:
    """A class to describe an apartment."""
    address: str
    price: int
    latitude: float   #  -90 to  90
    longitude: float  # -180 to 180

# The database is a list of apartments
# The data is real data from Google Maps
database = [
    Apartment(
        address = "1104-1157 Jepson-Young Ln, Vancouver, BC, Canada",
        price = 2050,
        latitude = 49.28268912323915, 
        longitude = -123.13115296063464
    ),
    Apartment(
        address = "718 Davie St, Vancouver, BC, Canada",
        price = 3050,
        latitude = 49.27736281422789, 
        longitude = -123.12668440036572
    ),
    Apartment(
        address = "1399 Homer St, Vancouver, BC, Canada",
        price = 2875,
        latitude = 49.27352901325701, 
        longitude = -123.12602017298748
    )
]


def cheapest(loa: List[Apartment]) -> Apartment | None:
    """
    Purpose: Returns the cheapest Apartment in the list
    Examples:
        database = [
            Apartment(
                price = 2050,
                ...
            ),
            Apartment(
                price = 3050,
                ...
            ),
            Apartment(
                price = 2875,
                ...
            )
        ]
        cheapest(database) -> Apartment(price = 2050 ...)
    """
    if len(loa) == 0:
        return None

    lowest = loa[0]
    for apartment in loa:
        if apartment.price < lowest.price:
            lowest = apartment
    return lowest

expect(cheapest(database), equals = database[0])

def closest(loa: List[Apartment], mine: Apartment) -> Apartment | None:
    """
    Purpose: Returns the closest apartment to another appartment.
    Examples:
        database = [
            Apartment(
                latitude = 49.28268912323915, 
                longitude = -123.13115296063464
                ...
            ),
            Apartment(
                latitude = 49.27736281422789, 
                longitude = -123.12668440036572
                ...
            ),
            Apartment(
                latitude = 49.27352901325701, 
                longitude = -123.12602017298748
                ...
            )
        ]
        closest([], database[0]) -> None
        closest(database, database[0]) -> database[1]

    """
    close: Apartment | None = None
    for apartment in loa:
        # Skip if it's the same apartment as the reference
        if apartment == mine:
            continue

        if close is None:
            close = apartment

        else:
            distance_cls_lat = mine.latitude - close.latitude
            distance_cls_lon = mine.longitude - close.longitude
            distance_cls = math.sqrt(distance_cls_lat ** 2 + distance_cls_lon ** 2)

            distance_apt_lat = mine.latitude - apartment.latitude
            distance_apt_lon = mine.longitude - apartment.longitude
            distance_apt = math.sqrt(distance_apt_lat ** 2 + distance_apt_lon ** 2)
            
            if distance_apt < distance_cls:
                close = apartment
    return close


expect(closest([], database[0]), None)
expect(closest(database, database[0]), database[1])
summarize()