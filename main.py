from ticket_system.ticket_main import TicketSystem

def main():
    test = TicketSystem()
    test.new_ticket(True)
    test.new_ticket()
    test.new_ticket(True)
    test.new_ticket()
    test.new_ticket(True)
    test.new_ticket()

    # test.completed_service()
    # test.completed_service()
    # test.completed_service()
    # test.completed_service()
    # test.completed_service()
    # test.completed_service()

    print(test.first_in_line())


if __name__ == '__main__':
    main()
