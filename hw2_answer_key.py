"""
This program helps determine whether an event can be held in a room, tracks capacity
 and calculates the expected revenue from the event registration.

Inputs:
Registered: integer; the number of people registered for an event
Capacity: integer; the maximum number of people allowed in the room
Fee: float; the registration cost per person

Output:
String that returns the total expected revenue.
String that returns capacity status of the room.
"""

def validate_event(registered, capacity, fee):
   
    if registered < 0:
        return False

    if capacity <= 0:
        return False

    if registered > capacity:
        return False

    if fee < 0:
        return False

    return True


def event_status(registered, capacity):
    if registered == capacity:
        return "room is at full capacity"
    elif registered >= capacity / 2:
        return "room is at least half capacity"
    else:
        return "room is under half capacity"


def calculate_revenue(registered, fee):
    return registered * fee


if __name__ == "__main__":
    registered = int(input("What is the number of people registered for event?: "))
    capacity = int(input("What is the capacity of the room in which the event will be held?: "))
    fee = float(input("What is the registration fee per person?: "))

    if validate_event(registered, capacity, fee)== False:
        print("The event information is invalid.")

    else:
        status = event_status(registered, capacity)
        revenue = calculate_revenue(registered, fee)

        print(f"The {status}.")
        print(f"The total revenue is ${revenue:.2f}")