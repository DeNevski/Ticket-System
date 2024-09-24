import pytest
from ticket_system.logic import TicketSystemLogic

class TestLogic:

    def test_deve_retornar_e_adicionar_NOR01_na_fila_quando_priority_for_FALSE(self):
        expected = 'NOR01'

        test = TicketSystemLogic()
        test.push(False)

        result = test.peek()
        assert result == expected

    def test_deve_retornar_e_adicionar_PRE01_na_fila_quando_priority_for_TRUE(self):
        expected = 'PRE01'

        test = TicketSystemLogic()
        test.push(True)

        result = test.peek()
        assert result == expected

    def test_deve_adicionar_NOR01_e_NOR02_depois_remover_NOR01_e_retornar_NOR02(self):
        expected = 'NOR02'

        test = TicketSystemLogic()
        test.push(False)
        test.push(False)
        test.pop()

        result = test.peek()
        assert result == expected

    def test_deve_adicionar_NOR01_PRE01_NOR02_PRE02_e_PRE03_os_PREs_devem_ficar_na_frente_dos_NORs_depois_remover_o_PRE01_e_retonar_PRE02(self):
        expected = 'PRE02'

        test = TicketSystemLogic()
        test.push(False)
        test.push(True)
        test.push(False)
        test.push(True)
        test.push(True)
        test.pop()

        result = test.peek()
        assert result == expected

    def test_deve_retornar_como_na_lista_expected(self):
        expected = ['PRE01', 'PRE02', 'PRE03', 'NOR01', 'NOR02', 'NOR03']

        result = []

        test = TicketSystemLogic()
        test.push(True)
        test.push(False)
        test.push(True)
        test.push(False)
        test.push(True)
        test.push(False)

        for v in range(0, 6):
            result.append(test.peek())
            test.pop()

        assert result == expected