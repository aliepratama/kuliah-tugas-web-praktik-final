import os

class PaymentConfig(object):
    API_KEY = os.environ.get('TRIPAY_KEY')
    PRVT_KEY = os.environ.get('TRIPAY_PRIVATE_KEY')
    MERCH_CODE = 'T26785'
