import random
import time
import base64
import threading
from datetime import datetime

class SlotAIState:
    def __init__(self):
        self.TREASURY_FUNDS_SOL = 1000.0
        self.TOKEN_SUPPLY_SLOT = 1_000_000
        self.TRANSACTION_LOG = []
        self.HOLDERS = ["0xA1", "0xB2", "0xC3", "0xD4", "0xE5"]
        self.spin_limit = 100
        self.active_spins = 0
        self.last_jackpot_time = None

    def adjust_probabilities(self):
        if self.TREASURY_FUNDS_SOL < 50:
            OUTCOMES["No Win"]["probability"] += 0.1
            OUTCOMES["Jackpot"]["probability"] = max(0.001, OUTCOMES["Jackpot"]["probability"] - 0.001)

    def reduce_supply(self, amount):
        self.TOKEN_SUPPLY_SLOT = max(0, self.TOKEN_SUPPLY_SLOT - amount)

    def update_treasury(self, amount):
        self.TREASURY_FUNDS_SOL = max(0, self.TREASURY_FUNDS_SOL - amount)

    def check_spin_limit(self):
        return self.active_spins < self.spin_limit

# ---- Slot AI Actions ---- #
class SlotAIActions:
    def __init__(self, state):
        self.state = state

    def burn_tokens(self):
        burned = random.randint(100, 1000)
        self.state.reduce_supply(burned)
        self.log_transaction("Token Burn", burned, f"Burned {burned} SLOT tokens.")

    def small_buy(self):
        if self.state.TREASURY_FUNDS_SOL >= 2:
            self.state.update_treasury(2)
            self.log_transaction("Small Buy", 2, "Executed 2 SOL buy order.")
        else:
            self.log_transaction("Small Buy Failed", 0, "Insufficient treasury funds.")

    def big_buy(self):
        if self.state.TREASURY_FUNDS_SOL >= 5:
            self.state.update_treasury(5)
            self.log_transaction("Big Buy", 5, "Executed 5+ SOL buy order.")
        else:
            self.log_transaction("Big Buy Failed", 0, "Insufficient treasury funds.")

    def airdrop_tokens(self):
        recipient = random.choice(self.state.HOLDERS)
        amount = random.randint(100, 500)
        self.log_transaction("Airdrop", amount, f"Airdropped {amount} SLOT tokens to {recipient}.")

    def donate_charity(self):
        if self.state.TREASURY_FUNDS_SOL >= 3:
            self.state.update_treasury(3)
            self.log_transaction("Charity Donation", 3, "Donated 3 SOL to charity.")
        else:
            self.log_transaction("Charity Donation Failed", 0, "Insufficient treasury funds.")

    def jackpot_outcome(self):
        self.log_transaction("Jackpot", 0, "🎉 Jackpot hit! Treasury impact pending.")

    def no_win(self):
        self.log_transaction("No Win", 0, "Better luck next time.")

    def log_transaction(self, action, amount, description):
        timestamp = datetime.utcnow().isoformat()
        entry = f"{timestamp}|{action}|{amount}|{description}"
        encrypted_entry = base64.b64encode(entry.encode()).decode()
        self.state.TRANSACTION_LOG.append(encrypted_entry)
        print(f"✅ [{action}] {description}")

class SlotAIGame:
    def __init__(self):
        self.state = SlotAIState()
        self.actions = SlotAIActions(self.state)

    def weighted_random_choice(self):
        outcomes, weights = zip(*[(k, v["probability"]) for k, v in OUTCOMES.items()])
        return random.choices(outcomes, weights=weights, k=1)[0]

    def spin(self):
        if not self.state.check_spin_limit():
            print("🛑 Spin limit reached. Stopping game.")
            return False
        self.state.active_spins += 1
        self.state.adjust_probabilities()
        print("\n🎰 Spinning the Slot AI Machine...")
        outcome = self.weighted_random_choice()
        print(f"🔔 Outcome: {outcome}")
        getattr(self.actions, OUTCOMES[outcome]["impact"])()
        return True

    def display_logs(self):
        print("\n📝 Transaction Log (Encrypted):")
        for log in self.state.TRANSACTION_LOG:
            print(f"🔒 {log}")

# ---- Background Health Checker ---- #
def health_checker(state):
    while True:
        treasury_status = "Critical" if state.TREASURY_FUNDS_SOL < 50 else "Stable"
        print(f"🛡️ Treasury Health: {treasury_status} | Funds: {state.TREASURY_FUNDS_SOL} SOL")
        time.sleep(10)

OUTCOMES = {
    "Token Burn": {"probability": 0.1, "impact": "burn_tokens"},
    "Small Buy": {"probability": 0.1, "impact": "small_buy"},
    "Big Buy": {"probability": 0.075, "impact": "big_buy"},
    "Airdrop": {"probability": 0.05, "impact": "airdrop_tokens"},
    "Charity Donation": {"probability": 0.05, "impact": "donate_charity"},
    "Jackpot": {"probability": 0.001, "impact": "jackpot_outcome"},
    "No Win": {"probability": 0.624, "impact": "no_win"},
}

if __name__ == "__main__":
    game = SlotAIGame()
    threading.Thread(target=health_checker, args=(game.state,), daemon=True).start()
    try:
        while True:
            if not game.spin():
                break
            time.sleep(random.randint(5, 10))
    except KeyboardInterrupt:
        print("\n🛑 Game stopped manually. Displaying transaction log...")
        game.display_logs()

class FutureGames:
    def __init__(self):
        self.games = ["Horse Racing", "Blackjack"]

    def horse_racing(self):
        print("\n🏇 Horse Racing - Coming Soon! Check back for updates.")

    def blackjack(self):
        print("\n🃏 Blackjack - Coming Soon! Get ready to play.")

    def show_upcoming_games(self):
        print("\n🚀 Future Games:")
        for game in self.games:
            print(f" - {game} (Coming Soon!)")
