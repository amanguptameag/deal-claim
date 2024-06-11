import uuid
from datetime import datetime
from user import User
from deal import Deal

class App:
    def __init__(self):
        self.users = {1: "Aman", 2: "Rahul"}
        self.items = {1: 'Apple', 2: 'Banana'}
        self.deals = {}
        self.claimed_deal = {}


    def add_deal(self, item_id: int, price: float, count: int, expiry_time: datetime):
        item = self.items[item_id]
        deal = Deal(item, price, count, expiry_time)
        self.deals[deal.id] = deal
        print("deal added")
        return deal


    def end_deal(self, deal_id: str):
        if deal_id not in self.deals:
            print("deal does not exist")
            return
        
        del deal_id
        print("deal successfully ended")


    def update_deal(self, deal_id: str, count: int = None, expiry_time: datetime = None):
        if deal_id not in self.deals:
            print("deal does not exist")
            return
        
        deal = self.deals[deal_id]
        if expiry_time:
            deal.expiry_time = expiry_time
        if count:
            deal.count = count
        print("deal updated")
        return deal


    def claim_deal(self, user_id: int, deal_id: str):
        if user_id not in self.users:
            print("user does not exist")
            return
        
        if deal_id not in self.deals:
            print("deal does not exist")
            return
        
        user = self.users[user_id]
        deal = self.deals[deal_id]

        # validating deal
        if deal.count == 0:
            print("this deal items are out of stock")
            return
        
        if deal.expiry_time < datetime.now():
            print("this deal has been ended")
            return
        
        key = f"{user_id}_{deal_id}"
        if key in self.claimed_deal:
            print("you have alreay claimed this deal")
            return

        # create claim
        deal.count -= 1
        self.claimed_deal[key] = 1

        print("deal claimed")
