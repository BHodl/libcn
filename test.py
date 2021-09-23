from libcn.libcn import CypherNode
cn = CypherNode(cnid="003", key="7b6f9de5d752ff9c37b199b01cd557d7ffd195805dd2c9800a300c0cdbee513d", url="https://doc:2009/v0")
def test_blockchaininfo():
    #for call in cn.all_cmd:
    #assert eval('cn.{}()'.format(call)['chain']) == 'test'
    good = cn.getblockchaininfo()['chain']
    return good
if __name__=='__main__':
    print(test_blockchaininfo())
