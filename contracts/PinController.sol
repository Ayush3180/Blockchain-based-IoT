// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract PinController {
    address owner;

    constructor() {
        owner = msg.sender;
    }

    mapping(uint8 => bool) public gpiopinStatus;

    function controlPin(uint8 pin, bool isActive)  external{
        require(msg.sender == owner);
        gpiopinStatus[pin] = isActive;
    }
}
