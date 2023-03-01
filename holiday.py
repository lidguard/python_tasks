#hotel cost
nights = int(input("How many nights do you want to stay? "))
def hotelcost():
    nightscost = 100 * nights
    return(nightscost)
hotelcost()

#plane cost
flights = input("Where do you want to go? ").capitalize()
def planecost():
    if flights == "London":
        flightscost = 400
        return(flightscost)
    elif flights == "Vancouver":
        flightscost = 800
        return(flightscost)
    elif flights == "Singapore":
        flightscost = 950
        return(flightscost)
    else:
        print("Sorry, that's not an option yet.")
        exit()
planecost()

#car rental cost
car = int(input("Enter how many days you want to rent a car for: "))
def car_rental():
    carcost = 105 * car
    return(carcost)

car_rental()

#calculate and print the full cost of the holiday
def holiday_cost():
    totalcost = hotelcost() + planecost() + car_rental()
    print(f"The total cost of your {nights} day trip to {flights} with a {car} day car hire will cost £{totalcost}.")
holiday_cost()