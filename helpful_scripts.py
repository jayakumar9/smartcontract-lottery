# create this file under smartcontract-lottery/scripts refer video 2.solidity time 2:41:55

from brownie import accounts, network, config
FORKED_LOCAL_ENVIRONMENTS=["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development","ganache-local"]

def get_account(index=None,id=None):
    if(
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
      ):  
        RETURN ACCOUNTS[0]
     else:
        return accounts.add(config["wallets"]["from_key"])
            
