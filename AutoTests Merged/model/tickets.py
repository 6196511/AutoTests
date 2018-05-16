

class Tickets:

    def __init__(self, **kwargs):
        self.id_testdata = kwargs.get('id_testdata')
        self.customer_URL = kwargs.get('customer_URL')
        self.activity = kwargs.get('activity')
        self.first_tickets_type = kwargs.get('first_tickets_type')
        self.second_tickets_type = kwargs.get('second_tickets_type')
        self.third_tickets_type = kwargs.get('third_tickets_type')
        self.fourth_tickets_type = kwargs.get('fourth_tickets_type')
        self.name_first_tickets_type = kwargs.get('name_first_tickets_type')
        self.name_second_tickets_type = kwargs.get('name_second_tickets_type')
        self.name_third_tickets_type = kwargs.get('name_third_tickets_type')
        self.name_fourth_tickets_type = kwargs.get('name_fourth_tickets_type')
        self.year = kwargs.get('year')
        self.month = kwargs.get('month')
        self.day = kwargs.get('day')
        self.time = kwargs.get('time')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.phone = kwargs.get('phone')
        self.email = kwargs.get('email')
        self.zip_code = kwargs.get('zip_code')
        self.promo_code = kwargs.get('promo_code')
        self.gift_certificate_code = kwargs.get('gift_certificate_code')
        self.payment_type = kwargs.get('payment_type')
        self.saved_card = kwargs.get('saved_card')
        self.card_number = kwargs.get('card_number')
        self.declined_card_number = kwargs.get('declined_card_number')
        self.card_date = kwargs.get('card_date')
        self.card_cvc = kwargs.get('card_cvc')
        self.card_zip = kwargs.get('card_zip')
        self.cash_recieved = kwargs.get('cash_recieved')
        self.ticket_total = kwargs.get('ticket_total')
        self.discount = kwargs.get('discount')
        self.gift_certificate = kwargs.get('gift_certificate')
        self.taxes = kwargs.get('taxes')
        self.booking_fee = kwargs.get('booking_fee')
        self.grand_total = kwargs.get('grand_total')

    def __repr__(self):
        return self.id_testdata
