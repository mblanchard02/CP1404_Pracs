from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """simulating taxi journey program"""
    total_trip_cost = 0
    selected_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer baby", 200, 4)]
    print("drive time")
    print(MENU)
    choice = input("> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis that are available:")
            display_taxis(taxis)
            chosen_taxi = int(input("Choose a taxi: "))
            try:
                selected_taxi = taxis[chosen_taxi]
            except IndexError:
                print("not valid taxi choice")
        elif choice == "d":
            print("d")
            if selected_taxi:
                selected_taxi.start_fare()
                drive_distance = float(input("what distance? "))
                selected_taxi.drive(drive_distance)
                trip_cost = selected_taxi.get_fare()
                total_trip_cost += trip_cost
                print(f"Your {selected_taxi.name} journey will be ${trip_cost:.2f}")
            else:
                print("A taxi must be selected before you set off")
        else:
            print("Invalid choice")
        print(f"Bill to date: ${total_trip_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total cost: ${total_trip_cost}")
    print("Taxis is now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """shows the available taxi's"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()