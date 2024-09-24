from utils.node import Node
from utils.ticket_generator import NormalTicket, PreferentialTicket
from utils.helpers import is_empty

class TicketSystemLogic:
    def __init__(self):
        self._first = None
        self._last = None
        self.normal = NormalTicket()
        self.preferential = PreferentialTicket()

    '''Adiciona um novo ticket na fila para ser atendido
        Se o ticket for preferencial, ele passará na frente dos tickets normais'''
    def push(self, priority):
        ticket = self._ticket_type(priority)
        node = Node(ticket, priority)

        if self._first is None:
            self._first = node
            self._last = node

        if priority:
            self._is_priority(node)

        else:
            self._last.next = node
            self._last = node

        self._last.next = None

    # Verifica o tipo de ticket requerido e o retorna
    def _ticket_type(self, priority):
        if priority:
            return self.preferential.next_ticket()
        else:
            return self.normal.next_ticket()
        
    # Adiciona os tickets prioritários na frente dos normais
    def _is_priority(self, node):
        pointer = self._first
        while pointer.next:

            if pointer.next.priority == False:
                node.next = pointer.next
                pointer.next = node
                break

            pointer = pointer.next 

    # "Deleta" o primeiro da fila
    def pop(self):
        if self._first is not None:
            self._first = self._first.next
        else:
            is_empty()

    # Retona quem é o primeiro da fila
    def peek(self):
        if self._first is not None:
            return self._first.data
        
        raise IndexError('The queue is empty')
