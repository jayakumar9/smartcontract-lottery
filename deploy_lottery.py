# create this file under smartcontract-lottery/scripts refer video 2.solidity time 2:40:42
from scripts.helpful_scripts import get_account, get_contract
from brownie import Lottery, network


def deploy_lottery():
    account=get_account()
    lottery=Lottery.deploy(get_contract("eth_usd_price_feed").address,get_contract("vrf_coordinator").address,get_contract("link_token".address,
                           config["networks"][network.show_active()]["fee"],config["networks"][network.show_active()]["keyhash"],{"from":account},
                            publish_source=config["networks"][network.show_active().get("verify",False),)
    print("Deployed lottery!")
                                                              
                                                       
                                                              
def start_lottery():
    account=get_account()
    lottery=Lottery[-1]                                                              
    lottery.startLottery({"from":account})
    print("The lottery is started!")                                                              

def main()
    deploy_lottery()
