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
    return accounts.add(config["wallets"]["from_key"])

contract_to_mock={"eth_usd_price_feed":MockV3Aggregator}
    
 def get_contract(contract_name):
    """ This function will grab the contract address from the brownie config 
    if defined, otherwise, it will deploy a mock version of that contract, and
    return that mock contract.
    
    Args:
        contract_name(string)
        
    Returns:
        brownie.network.contract.projectContract:The most recently deployed version of this contract.    
    
    """
    contract_type=contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type)<=0:
            # MockV3Aggregator.length
            deploy_mocks()
        contract=contract_type[-1]  
         # MockV3Aggregator[-1]
    else:
        contract_address=config["networks"][network.show_active()][contract_name]
        #address
        #ABI
        contract=contract.from_abi(contract_type._name, contract_address, contract_type.abi)
        # MockV3Aggregator.abi
    return contract    
        
            
DECIMALS=8
INITIAL_VALUE=200000000000
            
 def deploy_mock(decimals=DECIMALS,initial_value=INITIAL_VALUE):
    account=get_account()
    MockV3Aggregator.deploy(decimals, initial_value, {"from":account})
    print("Deployed!")
            
