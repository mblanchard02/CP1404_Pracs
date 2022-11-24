from prac_09.taxi import Taxi
my_taxi = Taxi("prius 1", 100, 1.23)
my_taxi.drive(40)
print(my_taxi)
print("The cost is:", my_taxi.get_fare())
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print("The cost is:", my_taxi.get_fare())
