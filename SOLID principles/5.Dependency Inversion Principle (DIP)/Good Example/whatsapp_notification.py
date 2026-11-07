from notification_channel import NotificationChannel

class WhatsappNotification(NotificationChannel):
    def send(self, messege):
        print(f"sending whatsapp message: {messege}")

