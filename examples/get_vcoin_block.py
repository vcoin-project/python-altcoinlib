#!/usr/bin/env python3

# Copyright (C) 2015 The python-altcoinlib developers
#
# This file is part of python-altcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

"""Pull the latest block in from a VCoin testnet client"""

# import sys
import os.path

import altcoin
from altcoin.rpc import AltcoinProxy
from bitcoin.core import lx

# Select VCoin test network
altcoin.SelectParams('000007e14c52364cee2d4d9483541d473e3e73c896df75882273b91313b44816')
# Set up RPC connection
rpc = AltcoinProxy(service_port=55535, btc_conf_file=os.path.expanduser('~/.vcoincore/vcoin.conf'))
best_block_hash = rpc.getblockchaininfo()['bestblockhash']
print(rpc.getblock(lx(best_block_hash)))
