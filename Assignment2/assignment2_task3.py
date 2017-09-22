#####*****Airline reservation system*****######
####**Using 5 classes : Bookingclass, seat, person, passenger,flight**####



class BookingClass:                             ###BOOKING CLASS
    def __init__(self, y, z):                    ###INIT CONSTRUCTOR
        self.economy_class = y
        self.business_class = z

    def get_Economy_class(self):
        print("Class:" + str(self.economy_class))

    def get_business_class(self):
        print("Class:" + str(self.business_class))


class Flight:                                    ###FLIGHT CLASS
    def __init__(self, i, j):                     ###INIT CONSTRUCTOR
        self.flight_number = i
        self.flight_name = j

    def get_flight_number(self):
        print("FlightNumber:" + str(self.flight_number))

    def get_flight_name(Self):
        print("FlightName:" + str(self.flight_name))


class Seat:                                         ####SEAT CLASS
    def __init__(self, n, p):                      ###INIT CONSTRUCTOR
        self.seat_number = n
        self.seat_letter = p

    def get_seat_number(self):
        print("SeatNumber:" + str(self.seat_number))

    def get_seat_letter(self):
        print("SeatLetter:" + str(self.seat_letter))


class Person:                                      ####PERSON CLASS
    count = 0

    def __init__(self, a, b, c, d):              ###INIT CONSTRUCTOR
        self.person_first_name = a
        self.person_last_name = b
        self.__person_age = c
        self.person_ticket_ID = d

        Person.count += 1

    def get_person_first_name(self):
        print("PersonFirstName:" + str(self.person_first_name))

    def get_person_last_name(self):
        print("PersonLastName:" + str(self.person_last_name))

    def get_person_age(self):
        print("PersonAge:" + str(self.__person_age))

    def get_person_ticket_ID(self):
        print("PersonTicketID:" + str(self.person_ticket_ID))


person1 = Person("karthik", "burra", "24", "123456789")
person2 = Person("jon", "snow", "25", "98765432")

#####****PERSON1****###
person1.get_person_first_name()
person1.get_person_age()
person1.get_person_ticket_ID()

#####****PERSON2****###
person2.get_person_first_name()
person2.get_person_age()
person2.get_person_ticket_ID()


####*****MultipleInheritence****#####

#### created one class passenger to inherit person,seat,flight and Booking classes ####
###PASSENGER CLASS
class Passenger(Person, Seat, BookingClass, Flight):  ###using 4 primary classes##
    def __init__(self, a, b, c, d, n, p, y, z):            ###INIT CONSTRUCTOR
        Person.__init__(self, a, b, c, d)
        #Flight.__init__(self, i, j)
        Seat.__init__(self, n, p)
        BookingClass.__init__(self, y, z)  ###super class constructor calling####


### Person3 OBJECT###
person3 = Passenger("stannis", "baratheon", "60", "9999999999999", "00", "XX", "economy",
                    "business")
person3.get_person_first_name()
person3.get_person_last_name()
person3.get_person_age()
person3.get_seat_number()
person3.get_seat_letter()
person3.get_Economy_class()
