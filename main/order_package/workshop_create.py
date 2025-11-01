class Workshop:
    registered_objects = {'register_car': [], 'register_mechanic': [], 'create_order': []}
    def register_car(self, car: list):
        self.registered_objects['register_car'] = self.registered_objects.get('register_car').append(car)

    def register_mechanic(self, mechanic: list):
        self.registered_objects['register_mechanic'] = self.registered_objects.get('register_mechanic').append(mechanic)

    def create_order(self, car: list, mechanic: list, services: list):
        list_order = [car, mechanic, services]
        self.registered_objects['create_order'] = self.registered_objects.get('create_order').append(list_order)






