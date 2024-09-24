# Gera tickets normais
class NormalTicket:

    def __init__(self):
        self._num = 0

    def next_ticket(self):
        self._num += 1
        ticket = f'NOR0{self._num}'
        return ticket

# Gera tickets preferênciais
class PreferentialTicket:

    def __init__(self):
        self._num = 0

    def next_ticket(self):
        self._num += 1
        ticket = f'PRE0{self._num}'
        return ticket
