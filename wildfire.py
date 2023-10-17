"""Geographic clustering of historical wildfire data
CS 210, University of Oregon
Finn Fujimura
Credits: TBD
"""
import doctest
import doctest
import csv
import config
import graphics.utm_plot

'''
def make_map() -> graphics.utm_plot.Map:
    """Create and return a basemap display"""
    map = graphics.utm_plot.Map(
        config.BASEMAP_PATH,
        config.BASEMAP_SIZE,
        (config.BASEMAP_ORIGIN_EASTING, config.BASEMAP_ORIGIN_NORTHING),
        (config.BASEMAP_EXTENT_EASTING, config.BASEMAP_EXTENT_NORTHING),
    )
    return map
'''


def get_fires_utm(path: str) -> list[tuple[int, int]]:
    """Read CSV file specified by path, returning a list
    of (easting, northing) coordinate pairs within the
    study area.

    >>> get_fires_utm("data/test_locations_utm.csv")
    [(442151, 4729315), (442151, 5071453), (914041, 4729315), (914041, 5071453)]
    """
    coordinate_pairs = []
    with open(path, newline="", encoding="utf-8") as source_file:
        reader = csv.DictReader(source_file)
        for row in reader:
            easting = int(row["Easting"])
            northing = int(row["Northing"])
            coordinate_pairs.append((easting, northing))
    return coordinate_pairs


def main():
    doctest.testmod()
    # fire_map = make_map()
    input("Press enter to quit")


if __name__ == "__main__":
    main()
