//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";//copied fromhttps://docs.openzeppelin.com/contracts/4.x/api/access#Ownable

contract Lottery is Ownable {
    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;
    enum LOTTERY_STATE{
        OPEN,
        CLOSED,
        CALCULATING_WINNER
    }
    LOTTERY_STATE public lottery_state;
    
    constructor(address _priceFeedAddress) public{
        usdEntryFee=50*(10**18);
        ethUsdPriceFeed=AggregatorV3Interface(_priceFeedAddress)
        lottery_state=LOTTERY_STATE.CLOSED;
     }   

    function enter() public{} payable {
    //$50 minimum
    require(lottery_state)==LOTTERY_STATE.OPEN();
    require(msg.value >=getEntranceFee(),"Not Enough ETH!");    
    players.push(msg.sender);
    }
    function getEntranceFee() public view returns(uint256){
        (,int256 price, , , )=ethUsdPriceFeed.latestRoundData;
        uint256 adjustedPrice=uint256(price)*10**10;//18 decimals
        //$50,$2000/ETH
        //50/2,000
        //50*100000/2000
        uint256 costToEnter=(usdEntryFee *10**18)/adjustedPrice;
        return costToEnter;
    }
    function startLottery() public onlyOwner{
        require(lottery_state==LOTTERY_STATE.CLOSED,"can't start a new lottery yet!");
        lottery_state==LOTTERY_STATE.OPEN;
        
    }
    function endLottery() public onlyOwner{
        uint256(keccack256(abi.encodePacked(
                                nonce,// nonce is predictable(aka,tranaction number
                                msg.sender,// msg.sender is predictable
                                block.difficulty,//csn actually be manipulated by the miners!
                                block.timestamp // timestamp is predictable
                                )
                                )
                                )%players.length;
    }
    
}
