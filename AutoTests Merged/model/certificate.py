

class Certificate:

    def __init__(self, **kwargs):
        self.id_testdata = kwargs.get('id_testdata')
        self.customer_URL = kwargs.get('customer_URL')
        self.certificate_type = kwargs.get('certificate_type')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.email = kwargs.get('email')
        self.initial_amount = kwargs.get('initial_amount')
        self.remain_amount = kwargs.get('remain_amount')
        self.activity = kwargs.get('activity')
        self.first_tickets_type = kwargs.get('first_tickets_type')
        self.second_tickets_type = kwargs.get('second_tickets_type')
        self.third_tickets_type = kwargs.get('third_tickets_type')
        self.name_first_tickets_type = kwargs.get('name_first_tickets_type')
        self.name_second_tickets_type = kwargs.get('name_second_tickets_type')
        self.name_third_tickets_type = kwargs.get('name_third_tickets_type')
        self.booking_fee = kwargs.get('booking_fee')
        self.total_amount = kwargs.get('total_amount')
        self.charge_type = kwargs.get('charge_type')
        self.check_number = kwargs.get('check_number')
        self.card_number = kwargs.get('card_number')
        self.declined_card_number = kwargs.get('declined_card_number')
        self.card_date = kwargs.get('card_date')
        self.card_cvc = kwargs.get('card_cvc')
        self.card_zip = kwargs.get('card_zip')

    def __repr__(self):
        return self.id_testdata
