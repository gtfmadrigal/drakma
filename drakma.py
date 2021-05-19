import hashlib
import time

class Block:

    def __init__(self, index, proofNo, prevHash, data, timestamp = None):
        self.index = index
        self.proofNo = proofNo
        self.prevHash = prevHash
        self.data = data
        self.timestamp = timestamp or time.time()
    
    @property
    def calculateHash(self):
        blockOfString = "{}{}{}{}{}".format(self.index, self.proofNo, self.prevHash, self.data, self.timestamp)
    
    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index,self.proofNo, self.prevHash, self.data, self.timestamp)

class BlockChain:

    def __init__(self):
        self.chain = []
        self.currentData = []
        self.nodes = set()
        self.constructGenesis()

    def constructGenesis(self):
        self.constructBlock(proofNo = 0, prevHash = 0)

    def constructBlock(self, proofNo, prevHash):
        block = Block(
            index = len(self.chain),
            proofNo = proofNo,
            prevHash = prevHash,
            data = self.currentData
            )
        self.currentData = []
        self.chain.append(block)
        return block
    
    @staticmethod
    def checkValidity(block, prevBlock):
        if prevBlock.index + 1 != block.index:
            return False
        elif prevBlock.calculateHash != block.prevHash:
            return False
        elif not BlockChain.verifyingProof(block.proofNo, prevBlock.proofNo):
            return False
        elif block.timestamp <= prevBlock.timestamp:
            return False
        return True

    def newData(self, sender, recipient, quantity):
        self.currentData.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })
        return True

    @staticmethod
    def proofOfWork(lastProof):
        proofNo = 0
        while BlockChain.verifyingProof(proofNo, lastProof) is False:
            proofNo += 1
        return proofNo
    
    @staticmethod
    def verifyingProof(lastProof, proof):
        guess = f'{lastProof}{proof}'.encode()
        guessHash = hashlib.sha256(guess).hexdigest()
        return guessHash[:4] == "0000"
    
    @property
    def latestBlock(self):
        return self.chain[-1]
    
    def blockMining(self, detailsMiner):
        self.newData(
            sender = "0",
            receiver = detailsMiner,
            quantity =
            1,
        )
        lastBlock = self.latestBlock
        lastProofNo = lastBlock.proofNo
        proofNo = self.proofOfWork(lastProofNo)
        lastHash = lastBlock.calculateHash
        block = self.constructBlock(proofNo, lastHash)
        return vars(block)
    
    def createNode(self, address):
        self.nodes.add(address)
        return True
    
    @staticmethod
    def obtainBlockObject(blockData):
        return Block(
            blockData['index'],
            blockData['proofNo'],
            blockData['prevHash'],
            blockData['data'],
            timestamp = blockData['timestamp']
        )
