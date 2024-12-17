import random
import time
from datetime import datetime

# Simulated Treasury Funds and Token Supply
TREASURY_FUNDS_SOL = x
TOKEN_SUPPLY_SLOT = 1_000_000  # Total supply of SLOT tokens

# Placeholder for token holders
HOLDERS = ["..."]

# Simulated blockchain transaction log
TRANSACTION_LOG = []

# Slot Machine Winning Outcomes Configuration
OUTCOMES = {
    "Token Burn": {"probability": 0.1, "impact": "burn_tokens"},
    "Small Buy": {"probability": 0.1, "impact": "small_buy"},
    "Big Buy": {"probability": 0.075, "impact": "big_buy"},
    "Airdrop": {"probability": 0.05, "impact": "airdrop_tokens"},
    "Charity Donation": {"probability": 0.05, "impact": "donate_charity"},
    "Jackpot": {"probability": 0.001, "impact": "jackpot_outcome"},
    "No Win": {"probability": 0.624, "impact": "Null"},
}

# Utility Functions
def burn_tokens():
    global TOKEN_SUPPLY_SLOT
    burned = random.randint(100, 1000)  # Burn between 100 and 1000 SLOT
    TOKEN_SUPPLY_SLOT -= burned
    log_transaction("Token Burn", burned, f"Reduced supply by burning {burned} tokens.")

def small_buy():
    global TREASURY_FUNDS_SOL
    if TREASURY_FUNDS_SOL >= 2:
        TREASURY_FUNDS_SOL -= 2
        log_transaction("Small Buy", 2, "Executed 2 SOL buy order on open market.")
    else:
        log_transaction("Small Buy Failed", 0, "Insufficient treasury funds for small buy.")

def big_buy():
    global TREASURY_FUNDS_SOL
    if TREASURY_FUNDS_SOL >= 5:
        TREASURY_FUNDS_SOL -= 5
        log_transaction("Big Buy", 5, "Executed 5+ SOL buy order on open market.")
    else:
        log_transaction("Big Buy Failed", 0, "Insufficient treasury funds for big buy.")

def airdrop_tokens():
    recipient = random.choice(HOLDERS)
    amount = random.randint(100, 500)  # Airdrop between 100-500 SLOT
    log_transaction("Airdrop", amount, f"Airdropped {amount} tokens to {recipient}.")

def donate_charity():
    global TREASURY_FUNDS_SOL
    if TREASURY_FUNDS_SOL >= 3:
        TREASURY_FUNDS_SOL -= 3
        log_transaction("Charity Donation", 3, "Donated 3 SOL to International Red Cross.")
    else:
        log_transaction("Charity Donation Failed", 0, "Insufficient funds for charity donation.")

def jackpot_outcome():
    log_transaction("Jackpot", 0, "Jackpot hit! Special event pending future implementation.")

# Core Slot Machine Spin
def slot_machine_spin():
    """Simulates the Slot Machine Spin."""
    print("\n🎰 Spinning the Slot AI Machine...")
    outcome = weighted_random_choice()
    print(f"🔔 Outcome: {outcome}")
    
    # Trigger the appropriate impact
    if outcome == "Token Burn":
        burn_tokens()
    elif outcome == "Small Buy":
        small_buy()
    elif outcome == "Big Buy":
        big_buy()
    elif outcome == "Airdrop":
        airdrop_tokens()
    elif outcome == "Charity Donation":
        donate_charity()
    elif outcome == "Jackpot":
        jackpot_outcome()

# Weighted Random Choice for Slot Outcomes
def weighted_random_choice():
    outcomes, weights = zip(*[(k, v["probability"]) for k, v in OUTCOMES.items()])
    return random.choices(outcomes, weights=weights, k=1)[0]

# Logging Function
def log_transaction(action, amount, description):
    timestamp = datetime.utcnow().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "action": action,
        "amount": amount,
        "description": description
    }
    TRANSACTION_LOG.append(log_entry)
    print(f"✅ {description} | Time: {timestamp}")

# Display the Transaction Log
def display_transaction_log():
    print("\n📝 Transaction Log:")
    for tx in TRANSACTION_LOG:
        print(f"[{tx['timestamp']}] {tx['action']}: {tx['description']}")

# Main Program
if __name__ == "__main__":
    print("🚀 Welcome to Slot AI - The AI-Powered On-Chain Slot Machine 🚀")
    print("Spins will occur every 10 seconds. Press Ctrl+C to stop.\n")

    try:
        while True:
            slot_machine_spin()
            time.sleep(10)  # Wait 10 seconds between spins
    except KeyboardInterrupt:
        print("\n🛑 Slot AI Stopped. Displaying transaction history...")
        display_transaction_log()
