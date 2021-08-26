pragma solidity ^0.5.5;

import "./BuddyToken.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract BuddyTokenCrowdsale is Crowdsale, MintedCrowdsale {
    constructor(
        uint rate,
        address payable wallet,
        BuddyToken token
    )
        Crowdsale(rate, wallet, token) 
        public 
    {
        //empty constructor
    }
}
    
contract BuddyTokenCrowdsaleDeployer {
    address public buddy_token_address;
    address public buddy_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    ) public {
        
        BuddyToken token = new BuddyToken(name, symbol);
        buddy_token_address = address(token);
        
        BuddyTokenCrowdsale buddy_crowdsale = new BuddyTokenCrowdsale(1, wallet, token);
        buddy_crowdsale_address = address(buddy_crowdsale);
        
        token.addMinter(buddy_crowdsale_address);
        token.renounceMinter();    
    }
}  

//Streamlit ideas
//1. user to convert ether to buddy token from personal ether wallet
//2. view balance of buddy wallet
//3. exchange buddy token between other users 
//4. view transactions 
//5. view current value of buddy token/ethereum in usd 
//6. give them your buddy wallet address, they withdraw correct value to cover purchase

