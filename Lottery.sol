//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
//copied fromhttps://docs.openzeppelin.com/contracts/4.x/api/access#Ownable
import "@openzeppelin/contracts/access/Ownable.sol";
// Copied fromhttps://docs.chain.link/docs/get-a-random-number/
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract Lottery is VRFConsumerBase,Ownable {
    address payable[] public players;
    address public recentWinner;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;
    enum LOTTERY_STATE{
        OPEN,
        CLOSED,
        CALCULATING_WINNER
    }
    LOTTERY_STATE public lottery_state;
    uint256 public fee;
    bytes32 public keyhash;
    
    
    constructor(address _priceFeedAddress,address _vrfCoordinator,address _link,uint256 _fee,bytes32 _keyhash) public VRFConsumerBase(_vrfCoordinator,_link) {
        usdEntryFee=50*(10**18);
        ethUsdPriceFeed=AggregatorV3Interface(_priceFeedAddress)
        lottery_state=LOTTERY_STATE.CLOSED;
        fee=_fee;
        keyhash=_keyhash;
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
     //  uint256(keccack256(abi.encodePacked(
     //                           nonce,// nonce is predictable(aka,tranaction number
     //                           msg.sender,// msg.sender is predictable
     //                           block.difficulty,//csn actually be manipulated by the miners!
     //                           block.timestamp // timestamp is predictable
     //                           )
     //                          )
     //                         )%players.length;
     lottery_state=LOTTERY_STATE.CALCULATING_WINNER;
     bytes32 requestId=requestRandomness(keyhash,fee);//refer video 2.solidity time 2:30:38
     
    }
    function fulfillRandomness(bytes _requestId,uint256 _randomness) internal override{
        require(lottery_state==LOTTERY_STATE.CALCULATING_WINNER,"You aren't there yet!");
        require(_randomness>0,""random-not-found");
        uint256 indexOfWinner=_randomness%players.length;
        recentWinner=players[indexOfWinner];
        recentWinner.transfer(address(this).balance);
        
    }
}
