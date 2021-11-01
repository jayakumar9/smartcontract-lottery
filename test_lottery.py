# Today ETH price is 2598.29
# $50 minimum price lottery so, 50/2598.29=0.019243425
# 190000000000000000

from brownie import Lottery, accounts

test_get_entrance_fee():
  account=accounts[0]
  lottery=Lottery.deploy(????,{"from":account})
  
