#/usr/bin/env bash
complete -W """
getblockchaininfo
getblockhash
helloworld
installation_info
getmempoolinfo
bitcoin_estimatesmartfee
watch
unwatch
watchxpub
unwatchxpubbyxpub
unwatchxpubbylabel
getactivewatchesbyxpub
getactivewatchesbylabel
getactivexpubwatches
watchtxid
getactivewatches
get_txns_by_watchlabel
get_txns_spending
get_unused_addresses_by_watchlabel
getbestblockhash
getbestblockinfo
getblockinfo
gettransaction
ln_getinfo
ln_create_invoice
ln_getconnectionstring
ln_decodebolt11
getbalance
getbalances
getbalancebyxpub
getbalancebyxpublabel
getnewaddress
spend
bumpfee
addtobatch
batchspend
deriveindex
derivepubpath
ln_pay
ln_newaddr
ots_stamp
ots_getfile
ots_verify
ots_info
ln_getroute
ln_getinvoice
ln_decodebolt11
ln_connectfund
conf
newblock
executecallbacks
ots_backoffice
ln_listpeers
ln_listfunds
ln_listpays
ln_delinvoice
ln_withdraw
getmininginfo
getnetworkhashps
""" cn cnt cnm cn-cli
