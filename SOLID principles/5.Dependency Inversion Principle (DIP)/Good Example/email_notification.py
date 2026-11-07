from notification_channel import NotificationChannel

class EmailNotification(NotificationChannel):
    def send(self, messege):
        print(f'sending email : {messege}')
