

class Certificate:

    def __init__(self, id_testdata=None, certificate_type=None, first_name=None, last_name=None, email=None,
                 initial_amount=None, remain_amount=None, activity=None, first_tickets_type=None,
                 second_tickets_type=None, third_tickets_type=None, name_first_tickets_type=None,
                 name_second_tickets_type=None, name_third_tickets_type=None, charge_type=None, check_number=None,
                 card_number=None, card_date=None, card_cvc=None, card_zip=None):
        self.id_testdata = id_testdata
        self.certificate_type = certificate_type
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.initial_amount = initial_amount
        self.remain_amount = remain_amount
        self.activity = activity
        self.first_tickets_type = first_tickets_type
        self.second_tickets_type = second_tickets_type
        self.third_tickets_type = third_tickets_type
        self.name_first_tickets_type = name_first_tickets_type
        self.name_second_tickets_type = name_second_tickets_type
        self.name_third_tickets_type = name_third_tickets_type
        self.charge_type = charge_type
        self.check_number = check_number
        self.card_number = card_number
        self.card_date = card_date
        self.card_cvc = card_cvc
        self.card_zip = card_zip

    def __repr__(self):
        return "%s" % (self.id_testdata)
