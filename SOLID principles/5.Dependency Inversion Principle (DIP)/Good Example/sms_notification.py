from notification_channel import NotificationChannel

class SMSNotification(NotificationChannel):
    def send(self, messege):
        print (f'sending sms : {messege}')