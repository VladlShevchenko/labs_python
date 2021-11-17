import json
import os


class RegularTicket:
    __current_id = 0
    __tickets_list = []

    def __init__(self):
        self.ticket_id = self.__generate_id()
        RegularTicket.__tickets_list.append({self.ticket_id: self})

    @property
    def ticket_id(self):
        return self.__ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        self.__ticket_id = value

    @property
    def get_ticket_price(self):
        return self.__price

    def __generate_id(self):
        if RegularTicket.__current_id + 1 > self.__num_of_tickets:
            raise OverflowError('All tickets for an event are over')

        RegularTicket.__current_id += 1

        return RegularTicket.__current_id

    @classmethod
    def deserialization(cls, filepath):

        if not os.path.exists(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as f:
            tickets = json.load(f)

        cls.__price = tickets['price']
        cls.__num_of_tickets = tickets['num0fTickets']

    @classmethod
    def find_ticket_by_id(cls, ticket_id):
        for ticket in cls.__tickets_list:
            if ticket.get(ticket_id):
                return ticket.get(ticket_id)

        raise Exception(f"Ticket with id {ticket_id} wasn't found")

    def __get_ticket_dict(self):
        return {
            "id": self.ticket_id,
            "price": self.get_ticket_price
        }

    def serialization(self):
        with open(f'{self.ticket_id}.json', 'w', encoding='utf-8') as f:
            json.dump(self.__get_ticket_dict(), f, indent=2)

    def __str__(self):
        return f'Ticket id: {self.ticket_id}, price: {self.get_ticket_price}'


class AdvanceTicket(RegularTicket):
    def __init__(self):
        super().__init__()

    @classmethod
    def deserialization(cls, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as f:
            tickets = json.load(f)

        cls.__coefficient = tickets['advance_ticket_coefficient']

    @property
    def get_ticket_price(self):
        return round(super().get_ticket_price * AdvanceTicket.__coefficient)


class StudentTicket(RegularTicket):
    def __init__(self):
        super().__init__()

    @classmethod
    def deserialization(cls, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as f:
            tickets = json.load(f)

        cls.__coefficient = tickets['student_ticket_coefficient']

    @property
    def get_ticket_price(self):
        return round(super().get_ticket_price * StudentTicket.__coefficient)


class LateTicket(RegularTicket):
    def __init__(self):
        super().__init__()

    @classmethod
    def deserialization(cls, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as f:
            tickets = json.load(f)

        cls.__coefficient = tickets['late_ticket_coefficient']

    @property
    def get_ticket_price(self):
        return round(super().get_ticket_price * LateTicket.__coefficient)


file = "tickets.json"
RegularTicket.deserialization(file)
AdvanceTicket.deserialization(file)
StudentTicket.deserialization(file)
LateTicket.deserialization(file)

ticket1 = RegularTicket()
ticket2 = StudentTicket()
ticket3 = LateTicket()
ticket3.serialization()

print(ticket1)
print(ticket2)
print(ticket3)
print(RegularTicket.find_ticket_by_id(3))
