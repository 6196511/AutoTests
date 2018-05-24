from model.certificate import Certificate


testdata = [
    Certificate(id_testdata="GoDo-32", certificate_type="Activity Tickets", first_name="John",
                last_name="Graham-Cumming", email="auto.godo@mailinator.com", initial_amount="120.00",
                activity="Dead of Night Tour", first_tickets_type="3", second_tickets_type="3",
                name_first_tickets_type="Adult", name_second_tickets_type="Child", charge_type="Check",
                check_number="123456789"),
    # GoDo-32 Purchasing certificate with number of tickets (120$, Check)

    Certificate(id_testdata="GoDo-21", certificate_type="Specific Dollar Amount", first_name="Patrick",
                last_name="McKenzie", email="auto.godo@mailinator.com", initial_amount="1000.00", charge_type="Cash"),
    # GoDo-21 Purchasing certificate with Specific Dollar Amount (1000$,cash)

    Certificate(id_testdata="GoDo-31", certificate_type="Activity Tickets", first_name="Jose Eduardo",
                last_name="Santos Tavares Melo Silva", email="auto.godo@mailinator.com", initial_amount="250.00",
                activity="Beyond Good and Evil Tours", first_tickets_type="5", second_tickets_type="5",
                name_first_tickets_type="Adult", name_second_tickets_type="Child", charge_type="creditcard",
                card_number="4242424242424242", card_date="1020", card_cvc="303", card_zip="70050"),
    # GoDo-31 Purchasing certificate with number of tickets (250$, credit card)

    Certificate(id_testdata="GoDo-22", certificate_type="Specific Dollar Amount", first_name="Lauren-May",
                last_name="de Silva", email="auto.godo@mailinator.com", initial_amount="500.00", charge_type="creditcard",
                card_number="4242424242424242", card_date="1020", card_cvc="303", card_zip="70050"),
    # GoDo-22 Purchasing certificate with Specific Dollar Amount (500$, credit card)

    Certificate(id_testdata="GoDo-23", certificate_type="Specific Dollar Amount", first_name="John Q.",
                last_name="Public", email="auto.godo@mailinator.com", initial_amount="100.00", charge_type="Check",
                check_number="123456789"),
    # GoDo-23 Purchasing certificate with Specific Dollar Amount (100$, Check)

    Certificate(id_testdata="GoDo-30", certificate_type="Activity Tickets", first_name="J", last_name="O'brian",
                email="auto.godo@mailinator.com", initial_amount="1000.00", activity="AlertTest", first_tickets_type="5",
                second_tickets_type="10", name_first_tickets_type="Adult", name_second_tickets_type="Child",
                charge_type="Cash"),
    # GoDo-30 Purchasing certificate with number of tickets (1000$, cash)

    Certificate(id_testdata="GoDo-47", certificate_type="Activity Tickets", first_name="de Medici", last_name="J",
                email="auto.godo@mailinator.com", initial_amount="500.00", activity="Beyond Good and Evil Tours",
                first_tickets_type="10", second_tickets_type="10", name_first_tickets_type="Adult",
                name_second_tickets_type="Child", charge_type="Cash"),
    # GoDo-47 Customer-Facing - Purchasing certificate with number of tickets
]