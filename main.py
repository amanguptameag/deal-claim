# Limited Time Deals

# A limited-time deal implies that a seller will put up an item on sale for a limited time period, say, 2 hours, 
# and will keep a maximum limit on the number of items that would be sold as part of that deal.

# Users cannot buy the deal if the deal time is over
# Users cannot buy if the maximum allowed deal has already been bought by other users.
# One user cannot buy more than one item as part of the deal.

# The task is to create APIs to enable the following operations

# Create a deal with the price and number of items to be sold as part of the deal
# End a deal
# Update a deal to increase the number of items or end time
# Claim a deal

#entity 
# 1. User
# 2. Deal
# 3. Item

from app import App
from datetime import datetime, timedelta
import time
import pdb

app = App()

user_id_1 = 1
user_id_2 = 2

# add deals
deal_1 = app.add_deal(1, 100, 2, datetime.now() + timedelta(seconds=1))
deal_2 = app.add_deal(2, 200, 3, datetime.now() + timedelta(minutes=1))

# time.sleep(2)

# claim_1 = app.claim_deal(user_id_1, deal_1.id)
# claim_2 = app.claim_deal(user_id_1, deal_2.id)

# deal_2 = app.update_deal(deal_2.id, 3, datetime.now() + timedelta(minutes=2))

# pdb.set_trace()
