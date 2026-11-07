from notification_channel import NotificationChannel

class NotificationService(NotificationChannel):
    def __init__(self, channel : NotificationChannel):
        self.channel = channel

    def send(self, messege : str):
        self.channel.send(messege)

    