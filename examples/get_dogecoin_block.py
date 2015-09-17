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

"""Pull the latest block in from a Dogecoin testnet client"""

import os.path

import altcoin
from altcoin.rpc import AltcoinProxy
from bitcoin.core import lx

altcoin.SelectParams('bb0a78264637406b6360aad926284d544d7049f45189db5664f3c4d07350559e')

rpc = AltcoinProxy(service_port=44555, btc_conf_file=os.path.expanduser('~/.dogecoin/dogecoin.conf'))
best_block_hash = rpc.getblockchaininfo()['bestblockhash']
print(rpc.getblock(lx(best_block_hash)))
