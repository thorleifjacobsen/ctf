pragma solidity >=0.7.3;
contract Welcome {
   string public flag;   
   constructor(string memory f) {
      flag = f;
   }
   function solve() public view returns (string memory) {
      return flag;
   }
   function isHelseCTF2023() public pure returns (bool) {
      return true;
   }
}