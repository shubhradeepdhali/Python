
from notification_service import NotificationService
from sms_notification import SMSNotification
from email_notification import EmailNotification
from whatsapp_notification import WhatsappNotification

# instantiate the notification_service class
email_notification_1 = EmailNotification()

notification_service_1 = NotificationService(email_notification_1)
notification_service_1.send("Hello I need some Dark Fantasies")

whatsapp_notification_1 = WhatsappNotification()
notification_service_2 = NotificationService(whatsapp_notification_1)
notification_service_2.send("Hello, we welcome all from Jio")

