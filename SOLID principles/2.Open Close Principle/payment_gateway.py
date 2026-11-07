from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount: int):
        pass

class UPIPayment(PaymentGateway):
    def pay(self, amount: int):
        print(f"Payment via UPI successful. Amount : {amount}")


class DebitCardPayment(PaymentGateway):
    def pay(self, amount: int):
        print(f"Payment via Debit Card successful. Amount: {amount}")

class CreditCardPayment(PaymentGateway):
    def pay(self, amount: int):
        print(f"Payment via Credit Card successful. Amount: {amount}")

class PaymentProcessor:
    def process_payment(self, payment_method :PaymentGateway, amount: int):
        payment_method.pay(amount)

debitcard = DebitCardPayment()

creditcard = CreditCardPayment()

payment = PaymentProcessor()
payment.process_payment(creditcard, 500)