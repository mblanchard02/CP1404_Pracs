from prac_06.car import Car


class Taxi(Car):
    """car with the cost of the fare"""
    price_per_km = 1.23

    def __init__(self, name, fuel, price_per_km):
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        """gives the string."""
        return f"{super().__str__()}, {self.current_fare_distance}km cost, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """gives the cost for the taxis journey."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """starts a new fare"""
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
