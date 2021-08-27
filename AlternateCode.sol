Token:

pragma solidity 0.5.5

contract WeedToken {
    
    string public name=“WeedToken”;
    string public symbol = “WEED”;
    string public standard = “WEED Token v1.0”
    string public decimals = 18;
    string public totalSupply;
    
    mapping(address=> uint256) public balanceOf;
    mapping(address=>mapping(address=>uint256)) public allowance;
    
    event Transfer(
        address indexed _from,
        address indexed _to,
        uint_value
    );
    
    event Approval(
        address indexed _owner,
        address indexed _spender,
        uint256 _value
    );
    
    function WeedToken (uint256_initialSupply) public{
        balanceOf[msg,sender]= _initialSupply;
        totalSupply = _initialSupply;
}

Sale contract:

pragma solidity 0.5.5;

import “./WeedToken.sol”;

contract WeedCrowdsale {
    
    address admin;
    WeedToken public tokenContract;
    uint256 public tokenPrice;
    uint256 public tokenSold;
    
    event Sell(address _buyer, uint256 _amount);
    
    function WeedCrowdsale(WeedToken _tokenContract, uint256 _tokenPrice) public {
        admin = msg.sender;
        tokenContract = _tokenContract;
        tokenPrice = _tokenPrice;
    }
    
    function multiply(uint x, uint y) internal pure returns (uint z) {
        require(y == 0 || (z=x*y)/ y == x);
    }
    
    function buyTokens (uint x,uint y) internal pure returns (uint z) {
        require (msg.value == multiply(_numberOfTokens, tokenPrice));
        require(tokenContract.balance(this) >= _numberOfTokens);
        require(tokenContract.transfer(msg.sender, _numberOfTokens));
        tokenSold +- _numberOfTokens;
    }