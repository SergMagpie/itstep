class Car():
    def __init__(self,
                 model_name,
                 year_of_manufacture,
                 manufacturer,
                 engine_capacity,
                 car_color,
                 price) -> None:
        self.model_name = model_name
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.car_color = car_color
        self.price = price

    def get_model_name(self) -> str:
        return self.model_name

    def get_year_of_manufacture(self) -> str:
        return self.year_of_manufacture

    def get_manufacturer(self) -> str:
        return self.manufacturer

    def get_engine_capacity(self) -> str:
        return self.engine_capacity

    def get_car_color(self) -> str:
        return self.car_color

    def get_price(self) -> str:
        return self.price

    def show_car_characteristics(self) -> None:
        print(self.get_model_name(),
              self.get_year_of_manufacture(),
              self.get_manufacturer(),
              self.get_engine_capacity(),
              self.get_car_color(),
              self.get_price())


bentley_continental_gt = Car('Bentley Continental GT III',
                             '2018',
                             'Volkswagen',
                             '6.0',
                             'blue',
                             '207176.40')

bentley_continental_gt.show_car_characteristics()
