# create this file under smartcontract-lottery/scripts refer video 2.solidity time 2:40:42
from scripts.helpful_scripts import get_account
from brownie import Lottery


def deploy_lottery():
    account=get_account()
    lottery=Lottery.deploy(

def main()
    deploy_lottery()
