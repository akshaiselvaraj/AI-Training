class Order:
    def __init__(self,order_id,customer_name,amount):
        self.order_id=order_id
        self.customer_name=customer_name
        self.amount=amount

    def process_payment():
        pass

class Card_payment(Order):
    def process_payment(self):
        print(f"Processing card payment of ₹{self.amount} for Order ID{self.order_id}")
        print("Validating card details")
        print("Payment Successfull via card")


class UPI_payment(Order):
    def process_payment(self):
        print(f"Processing UPI Payment of ₹{self.amount} for Order ID {self.order_id}")
        print("Verifying UPI ID...")
        print("Payment successful via UPI!")

class NetBanking_payment(Order):
     def process_payment(self):
        print(f"Processing Net Banking Payment of ₹{self.amount} for Order ID {self.order_id}")
        print("Redirecting to bank portal...")
        print("Payment successful via Net Banking!")


order_id=input("Enter Order ID: ")
customer_name=input("Enter Customer name: ")
amount=float(input("Enter Order Amount: "))

print("\nChoose payment method:")
print("1. Card")
print("2. UPI")
print("3. Net Banking")

ch=int(input("Enter choice: "))
if ch== 1:
    order = Card_payment(order_id, customer_name, amount)

elif ch == 2:
    order = UPI_payment(order_id, customer_name, amount)

elif ch== 3:
    order = NetBanking_payment(order_id, customer_name, amount)

else:
    print("Invalid choice")
    exit()

print("\nOrder details")
print("Customer:",customer_name)

order.process_payment()
