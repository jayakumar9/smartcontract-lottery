# create this file under smartcontract-lottery/scripts refer video 2.solidity time 2:41:55

from brownie import accounts, network, config
FORKED_LOCAL_ENVIRONMENTS=["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development","ganache-local"]

def get_account(index=None,id=None):
    #accounts[0]
    #accounts.add("env")
    #accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if(
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
      ):  
        return accounts[0]
     else:
        return accounts.add(config["wallets"]["from_key"])
    
 def get_contract(contract_name):
    """ This function will grab the contract address from the brownie config 
    if defined, otherwise, it will deploy a mock version of that contract, and
    return that mock contract.
    
    Args:
        contract_name(string)
        
    Returns:
        brownie.network.contract.projectContract:The most recently deployed version of this contract.    
    
    """
            
