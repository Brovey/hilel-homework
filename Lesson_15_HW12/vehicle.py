class Vehicle:
    def __init__(self,  weight, construction_year, material):
        self.weight = weight
        self.construction_year = construction_year
        self.material = material

    def print_base_characteristics(self):
        print(f"Vehicle base characteristics:\nMade of {self.material}\n"
              f"Weight {self.weight} kg\nCreated in {self.construction_year}\n")

    def moving(self):
        return "It's moving somehow"


class Train(Vehicle):
    def __init__(self, weight,  construction_year, material, engine_type, number_of_carriage=0):
        super().__init__(weight, construction_year, material)
        self.engine_type = engine_type
        self.number_of_carriage = number_of_carriage

    def print_base_characteristics(self):
        super().print_base_characteristics()
        return f"Engine type: {self.engine_type}\nNumber of carriage: {self.number_of_carriage}"

    def add_carriage(self, number):
        self.number_of_carriage += number
        return self.number_of_carriage


class Airplane(Vehicle):
    def __init__(self, weight, construction_year, material, model, flight_altitude, color):
        super().__init__(weight, construction_year, material)
        self.model = model
        self.flight_altitude = flight_altitude
        self.color = color

    def print_base_characteristics(self):
        super().print_base_characteristics()
        return f"Model: {self.model}\nFlight altitude:" \
               f" {self.flight_altitude}\nColor: {self.color}"

    def set_new_color(self, new_color):
        self.color = new_color


my_train = Train(10000, 1999, "Iron", "Steam")
my_plane = Airplane(2500, 2020, "Aluminium", "Airbus a330",  7000, "Black")
