import math

from Model.planet import Planet


class PlanetCoordinates:
    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __repr__(self):
        return f"{self.latitude:.6f}°, {self.longitude:.6f}°"

    def distance_to(self, other): # in Km
        if not isinstance(other, PlanetCoordinates):
            raise TypeError("distance_to expects a PlanetCoordinates object")

        # Convert degrees to radians
        lat1 = math.radians(self.latitude)
        lon1 = math.radians(self.longitude)
        lat2 = math.radians(other.latitude)
        lon2 = math.radians(other.longitude)

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (math.sin(dlat / 2) ** 2 +
             math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = Planet.radius * c
        return distance
