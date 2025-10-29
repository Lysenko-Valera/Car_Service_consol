class MechanicNotFoundError(Exception):
    """Отлавливает ошибки связанные с механиком"""

class Mechanic:
    def __init__(self, name: str, specialization: str, experience_years: float):
        if not isinstance(name, str):
            raise MechanicNotFoundError('Ошибка имя механика должно быть строкой')
        if not isinstance(specialization, str):
            raise MechanicNotFoundError('Ошибка специализация механника должна быть строкой')
        if not isinstance(experience_years, float):
            raise MechanicNotFoundError('Ошибка. Опыт работы должен быть вещественным числом')
        self.name = name
        self.specialization = specialization
        self.experience_years = experience_years
        self.mechanic_id = self.generation_id()

    def perform_service(self, car_service):
        pass

    list_id = [0]
    def generation_id(self):
        new_id = self.list_id[-1] + 1
        self.list_id.append(new_id)
        id_mex = self.mechanic_id = new_id
        return id_mex

    __list_completed_services = []
    @property
    def set_get_complectid_serv(self):
        return self.__list_completed_services

    @set_get_complectid_serv.setter
    def set_get_complectid_serv(self, new_completed_services):
        self.__list_completed_services.append(new_completed_services)

m = Mechanic('Jon', 'Мех', 4.0)
m2 = Mechanic('Jon', 'Мех', 24.5)
print(m2.mechanic_id)
print(m.mechanic_id)
