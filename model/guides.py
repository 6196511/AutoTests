

class Guides:

    def __init__(self, **kwargs):
        self.id_testdata = kwargs.get('id_testdata')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.email = kwargs.get('email')
        self.timezone = kwargs.get('timezone')
        self.phone_number = kwargs.get('phone_number')
        self.secondary_phone_number = kwargs.get('secondary_phone_number')
        self.emergency_contact = kwargs.get('emergency_contact')
        self.emergency_phone = kwargs.get('emergency_phone')
        self.hire_date = kwargs.get('hire_date')
        self.end_date = kwargs.get('end_date')
        self.bank_name = kwargs.get('bank_name')
        self.account_type = kwargs.get('account_type')
        self.bank_routing_number = kwargs.get('bank_routing_number')
        self.account_number = kwargs.get('account_number')
        self.pay_rate_type = kwargs.get('pay_rate_type')
        self.rate = kwargs.get('rate')
        self.trained_activities = kwargs.get('trained_activities')

    def __repr__(self):
        return self.id_testdata
