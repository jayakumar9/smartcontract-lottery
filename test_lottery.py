# Today ETH price is 2598.29
# $50 minimum price lottery so, 50/2598.29=0.019243425
# 190000000000000000

from brownie import Lottery, accounts, confiq
from web3 import web3

test_get_entrance_fee():
  account=accounts[0]
  lottery=Lottery.deploy(confiq["networks"][network.show_active()]["eth_usd_price_feed"],{"from":account})
  assert lottery.getEntranceFee()>web3.toWei(0.018,"ether")
   assert lottery.getEntranceFee()<web3.toWei(0.022,"ether")
  
