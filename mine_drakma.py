from drakma import *

blockchain = BlockChain()

print("Mining Drakma...")
print(blockchain.chain)

lastBlock = blockchain.latestBlock
lastProofNo = lastBlock.proofNo
proofNo = blockchain.proofOfWork(lastProofNo)

blockchain.newData(
    sender = "0",
    recipient = "Gavin",
    quantity = 
    1,
)

lastHash = lastBlock.calculateHash
block = blockchain.constructBlock(proofNo, lastHash)

print("Mining successful.")
print(blockchain.chain)