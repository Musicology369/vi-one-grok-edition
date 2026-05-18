// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract RoyaltySplitter369 {
    uint256 public constant ARTIST_SHARE = 9630;   // 96.30%
    uint256 public constant PLATFORM_FEE = 369;    // 3.69%
    uint256 public constant BURN_SHARE = 1;        // 0.01%

    event Distributed(address indexed artist, uint256 artistAmount, uint256 platformAmount, uint256 burned);

    function distribute(uint256 totalAmount, address artistWallet) external {
        uint256 artist = (totalAmount * ARTIST_SHARE) / 10000;
        uint256 platform = (totalAmount * PLATFORM_FEE) / 10000;
        uint256 burn = (totalAmount * BURN_SHARE) / 10000;

        // TODO: Later we connect this to Onda USDC for real payouts
        // For now this just shows the math is working perfectly

        emit Distributed(artistWallet, artist, platform, burn);
    }
}
