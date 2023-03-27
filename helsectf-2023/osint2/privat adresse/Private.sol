pragma solidity >=0.7.3;
contract Private {
   event updated(string s);
   string private adresse;   
   function set_adresse(string memory a) public {
      adresse = a ;
      emit updated(adresse);
   }
   function isHelseCTF2023() public pure returns (bool) {
      return true;
   }
}