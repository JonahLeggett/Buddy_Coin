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
        Crowdsale(rate, wallet, token) public {
        }
}
    
contract BuddyTokenCrowdsaleDeployer {

    address public buddy_token_address;
    address public buddy_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public {
        BuddyToken token = new BuddyToken(name, symbol, 0);
        buddy_token_address = address(token);
        BuddyTokenCrowdsale buddy_crowdsale = new BuddyTokenCrowdsale(1, wallet, token);
        buddy_crowdsale_address = address(buddy_crowdsale);
        token.addMinter(buddy_crowdsale_address);
        token.renounceMinter();    
        }
}  