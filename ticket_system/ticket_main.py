from .logic import TicketSystemLogic

class TicketSystem:
    def __init__(self):
        self.logic = TicketSystemLogic()

    # Cria um novo ticket
    def new_ticket(self, priority=False):
        self.logic.push(priority)

    # Completa um atendimento
    def completed_service(self):
        self.logic.pop()

    # Retorna quem é o primeiro da fila
    def first_in_line(self):
        return self.logic.peek()
