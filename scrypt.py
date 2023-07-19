from web3 import Web3

# Infura API endpoint for the Ethereum mainnet
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY"

# Your Ethereum wallet private key and the destination address to send ETH
private_key = "YOUR_WALLET_PRIVATE_KEY"
destination_address = "DESTINATION_ETH_ADDRESS"

# Connect to the Ethereum node using Infura
web3 = Web3(Web3.HTTPProvider(infura_url))

def transfer_eth():
    if not web3.isConnected():
        print("Failed to connect to the Ethereum node.")
        return

    # Convert the private key to bytes
    private_key_bytes = bytes.fromhex(private_key)

    # Get the sender's address from the private key
    sender_address = web3.eth.account.from_key(private_key_bytes).address

    print("Sender Address:", sender_address)
    print("Destination Address:", destination_address)

    # Get the sender's balance
    balance = web3.eth.get_balance(sender_address)
    print("Sender Balance:", web3.fromWei(balance, "ether"), "ETH")

    # Transaction details
    value_ether = 0.1  # Amount of ETH to send
    value_wei = web3.toWei(value_ether, "ether")

    transaction = {
        "to": destination_address,
        "value": value_wei,
        "gas": 21000,
        "gasPrice": web3.toWei("30", "gwei"),
        "nonce": web3.eth.getTransactionCount(sender_address),
    }

    # Sign the transaction with the private key
    signed_transaction = web3.eth.account.signTransaction(transaction, private_key_bytes)

    # Send the transaction
    tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    print("Transaction Hash:", web3.toHex(tx_hash))

    # Wait for the transaction to be mined
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print("Transaction Mined!")
    print("Gas Used:", receipt["gasUsed"])

if __name__ == "__main__":
    transfer_eth()
