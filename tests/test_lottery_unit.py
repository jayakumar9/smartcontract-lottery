# create this file under smartcontract-lottery/tests


#0.019
# 190000000000000000
from brownie import Lottery. accounts. config, network
from web3 import web3


def test_get_entrance_fee():
    account=accounts[0]
    lottery=Lottery.deploy(config["network"][network.show_active()]["eth_usd_price_feed"],{"from":account},)
    #assert lottery.getEntranceFee()>web3.towei(0.018,"ether")
    #assert lottery.getEntranceFee()<web3.towei(0.022,"ether")

