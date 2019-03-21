from .views import *
import payplug

payplug.set_secret_key('sk_test_6sTDt5xbcqQiqlXTDeZCnJ')


def send_paiment():
    pass

def create_payment(amount,email,customer_id):
    payment_data = {
      'amount': amount,
      'currency': 'EUR',
      'customer': {
        'email': email
      },
      'hosted_payment': {
        'return_url': 'https://localhost:5000/payment/sucess',
        'cancel_url': 'https://localhost:5000/payment/cancel',
      },
      'notification_url': 'https://localhost:5000/payment/notification',
      'metadata': {
        'customer_id': customer_id,
      },
    }
    payment = payplug.Payment.create(**payment_data)
    payment_id = str(payment.id)
    return payment



def get_payment_link(payment):
    return payment.hosted_payment.payment_url


def retrieve_payment(payment_id,mail):
    try:
        payment = payplug.Payment.retrieve(payment_id)
        #Evoyer un mail de confirmation
    except Exception as e:
        #notifier l'echec
        pass


def abort_payment(payment_id):
    # Abort from a payment ID
    payment_id = payment_id
    payment = payplug.Payment.abort(payment_id)



def get_payments():
    payments = payplug.Payment.list()
    payment = next(payments)
    return payment
