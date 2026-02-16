class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print("Sending Email Notification...")
        print("Message:", message)

class SMSNotification(Notification):
    def send(self, message):
        print("Sending SMS Notification...")
        print("Message:", message)

class PushNotification(Notification):
    def send(self, message):
        print("Sending Push Notification...")
        print("Message:", message)

print("Choose Notification Channel:")
print("1. Email")
print("2. SMS")
print("3. Push")

choice = int(input("Enter choice: "))
msg = input("Enter message: ")

if choice == 1:
    notify = EmailNotification()

elif choice == 2:
    notify = SMSNotification()

elif choice == 3:
    notify = PushNotification()

else:
    print("Invalid choice")
    exit()

notify.send(msg)
