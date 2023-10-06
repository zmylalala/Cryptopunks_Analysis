# Cryptopunks Analysis
## INTRODUCTION
Launched in June 2017 by product studio Larva Labs and acquired by Yuga Labs in 2022, CryptoPunks is one of the first 
NFT collections on the Ethereum blockchain. It consists of 10,000 unique 24×24 pixel art images depicting primarily 
humans (male and female). There are several other unique types that are considered more valuable due to their 
rarity. These include zombies (88), apes (24) and aliens (9).  
Each CryptoPunk can also exhibit a combination of 87 unique properties. These are called "features" and include hats, 
pipes, necklaces, earrings, eye patches, etc.  
The maximum number of features a single CryptoPunk can have is seven. However, only one CryptoPunk exists with seven 
features, #Punk 8348. It has cigarettes, earrings, moles, buck teeth, classic shades, top hats and a beard. CryptoPunks 
can also have zero features, but most tend to have two or three.
The following describes the basic information about blockchain and Ethereum.  
Blockchain is best described as a public database that is updated and shared by many computers in a network.  
"Block" means that data and status are stored in sequential batches or "chunks". If you send ETH to someone else, the 
transaction data needs to be added to a block for it to be successful.  
"Chain" refers to each block's cryptographic reference to its parent block. In other words, blocks are linked together. 
The data within the block cannot be changed without changing all subsequent blocks, but changing subsequent blocks 
requires the consensus of the entire network.
Every computer in the network must agree on each new block and chain. These computers are called "nodes". Nodes ensure 
that everyone interacting with the blockchain has the same data. To complete this distributed protocol, the blockchain 
requires a consensus mechanism.  
Ethereum is a blockchain with computers embedded within it. It is the foundation for building applications and 
organizations in a decentralized, permissionless, censorship-resistant way.
In the Ethereum universe, there is a canonical computer (called the Ethereum Virtual Machine, or EVM) whose state is 
unanimously agreed upon by everyone in the Ethereum network. Everyone participating in the Ethereum network 
(each Ethereum node) keeps a copy of the state of that computer. Additionally, any participant can broadcast requests 
to this computer to perform arbitrary computations. Whenever such a request is broadcast, other participants on the 
network inspect, verify, and perform ("perform") the computation. This execution causes a state change in the Ethereum 
Virtual Machine that is propagated throughout the network.    
This article aims to analyze the development history of Crypto-punks and give some insights.
## DATA EXTRACTION
There are three types of transactions in Ethereum:  
Regular Transaction: A transaction from one wallet to another.  
Contract deployment transaction: a transaction without a "to" address, the data field is used for the contract code.  
Execution Contract: A transaction that interacts with a deployed smart contract. In this case, the "to" address is the 
smart contract address  
Regular transactions refer to transfers that only involve Ether, the native token of Ethereum, and do not involve calls 
to contracts or transactions with other tokens in Ethereum. The data in regular transactions can be roughly divided into 
four blocks: transaction hash, time, etc. belong to the transaction index (index), which provides information to locate 
the transaction. The transaction amount specifically refers to the amount of Ether transferred. The sender and receiver 
of the transaction are each other's counterparties in this transaction. The consumption of gas fees is the transaction 
cost that the sender of this transaction needs to bear.   
In addition to the above data, transactions involving smart contracts will also have three additional pieces of content:  
(1) The internal process of Ethereum executing transactions (internal transactions);  
(2) The result of the token transfer (token transfer);  
(3) Input parameters (input data) for contract execution  
In a contract source code, not only the contract method (function) will be defined, but also the event abc() and 
the submission event emit abc(). The submitted event will be recorded in the log, and finally the log will be recorded 
in the receipt function of a transaction that calls the contract.  
Crypto-punk belongs to the third type of transaction. Using DUNE can save the work of decoding part of the hash bytecode.  
Dune preprocesses blockchain data into relational database (PostgreSQL and DatabricksSQL) tables, allowing users to 
query blockchain data using SQL and build dashboards based on query results. The data on the chain is divided into 4 
original tables: blocks, transactions, (event) logs and (call) traces. Popular contracts and protocols have been 
decoded, each with its own set of events and call tables.
## DATA ANALYSIS
After saving the downloaded csv table, we can use python to read it for further analysis and the construction of 
artificial intelligence models.  
We first explore the trade trend over the year. 
<figure>
    <img src="pics/date_usd.png">
</figure>

## CONCLUSION

