# create this file under smartcontract-lottery/tests


#0.019
# 190000000000000000
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import Lottery. accounts. config, network
from scripts.deploy_lottery import deploy_lottery
from web3 import web3
import pytest


def test_get_entrance_fee():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # Arrange
    lottery=deploy_lottery()
    # Act
    # 2,000 eth/usd
    # usdEntryFee is 50
    # 2000/1==50/x==0.025
    expected_entrance_fee=web3.towei(0.025,"ether")
    entrance_fee=lottery.getEntranceFee()
    # Assert
    assert expected_entrance_fee==entrance_fee
    
 

