import uuid
from datetime import datetime

class Deal:
    def __init__(self, item: str, price: float, count: int, expiry_time: datetime):
        self.id = str(uuid.uuid4())
        self.item = item
        self.price = price
        self.count = count
        self.expiry_time = expiry_time
