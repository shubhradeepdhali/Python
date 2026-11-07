class PaymentGateway:
    def __init__(self, payment_method : str, amount : int) -> None:
        self.payment_method = payment_method
        self.amount = amount

        if payment_method == "UPI":
            print('paying with UPI')
        elif payment_method == "Debit Card":
            print('paying with Debit Card')
        elif payment_method == "Credit Card":
            print('paying with Credit Card')