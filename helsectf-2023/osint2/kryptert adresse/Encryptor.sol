pragma solidity >=0.7.3;
contract Encryptor {
    bytes private adresse = bytes("dette_er_feil_adresse") ;
    uint256 private s0 = ? ;
    function encrypt(bytes memory pt) private view returns (bytes memory) {           
        bytes memory ct = new bytes(pt.length);
        uint256 s = s0 ;
        for (uint i = 0; i < pt.length; i++) {
            s = (0x13*s + 0x32)%0xff ;          
            ct[i] = bytes(pt)[i]^bytes1(uint8(s));
        }
        return ct;
    }     
    function set_encrypted_adresse(bytes memory a) public {        
        adresse = encrypt(a) ;
    }          
    function get_encrypted_adresse() public view returns (bytes memory) {
        return encrypt(adresse) ;
    } 
    function isHelseCTF2023() public pure returns (bool) {
      return true;
   }
}