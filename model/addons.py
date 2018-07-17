

class Addons:

    def __init__(self, **kwargs):
        self.id_testdata = kwargs.get('id_testdata')
        self.addon_name = kwargs.get('addon_name')
        self.addon_price = kwargs.get('addon_price')
        self.addon_description = kwargs.get('addon_description')
        self.addon_status = kwargs.get('addon_status')
        self.type_addon = kwargs.get('type_addon')
        self.type_name = kwargs.get('type_name')
        self.type_price = kwargs.get('type_price')
        self.type_status = kwargs.get('type_status')
        self.activity = kwargs.get('activity')

    def __repr__(self):
        return self.id_testdata
