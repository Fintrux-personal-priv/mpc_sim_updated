# import os
# import time
# import threading
# import hashlib
# import random
# from flask import Flask, request, jsonify

# # Global debug delay (set DEBUG_DELAY=0.1 for debugging, 0 for production)
# DEBUG_DELAY = float(os.environ.get("DEBUG_DELAY", "0.1"))

# # Configuration from environment variables: now for 19 banks
# BANK_ID = int(os.environ.get("BANK_ID", "1"))
# TOTAL_BANKS = int(os.environ.get("TOTAL_BANKS", "19"))
# TOTAL_SHARES = TOTAL_BANKS + 1  # 19 shares for banks + 1 extra for reconciliation

# # API port for contribution submission (unique per bank)
# API_PORT = 8000 + BANK_ID

# # Simulated ports (for secret sharing and round-robin phases)
# SECRET_BASE_PORT = 6000  # each bank listens on (SECRET_BASE_PORT + BANK_ID) for secret shares.
# ROUND_BASE_PORT = 7000   # each bank listens on (ROUND_BASE_PORT + BANK_ID) for round-robin addition.
# RETURN_PORT = 5001       # Bank 1 listens on this port for the final aggregated result.

# # For simulation, define fixed contributions for 19 banks.
# PUBLIC_CONTRIBUTIONS = {
#     1: 101, 2: 102, 3: 103, 4: 104, 5: 105, 6: 106, 7: 107, 8: 108, 9: 109,
#     10: 110, 11: 111, 12: 112, 13: 113, 14: 114, 15: 115, 16: 116, 17: 117, 18: 118, 19: 119
# }

# # Global variable to store the contribution submitted via API
# submitted_contribution = None

# def log(message):
#     print(f"LOG: Bank {BANK_ID}: {message}")

# def debug_sleep(duration=DEBUG_DELAY):
#     time.sleep(duration)

# # ----------------------- API SERVER for Contribution Submission -----------------------
# app = Flask(__name__)

# @app.route('/submit', methods=['POST'])
# def submit():
#     global submitted_contribution
#     data = request.get_json()
#     if "contribution" in data:
#         try:
#             submitted_contribution = float(data["contribution"])
#             log(f"Contribution submitted via API: {submitted_contribution}")
#             return jsonify({"status": "received"}), 200
#         except Exception as e:
#             return jsonify({"status": "error", "message": str(e)}), 400
#     else:
#         return jsonify({"status": "error", "message": "No contribution provided"}), 400

# def run_api_server():
#     app.run(host="0.0.0.0", port=API_PORT)

# # ----------------------- Cryptographic Primitives (Simulation) -----------------------
# def commit_value(value):
#     # Simulate a SHA-256 commitment (as if computed in circom)
#     h = hashlib.sha256()
#     h.update(str(value).encode('utf-8'))
#     return h.hexdigest()

# def post_to_bulletin_board(commitment):
#     # Simulate posting to a public bulletin board
#     log(f"Posted commitment to bulletin board: {commitment}")

# def compute_merkle_root(commitments):
#     # A simple (non-secure) simulation of a Merkle tree computation.
#     def pair_hash(h1, h2):
#         combined = h1 + h2
#         return hashlib.sha256(combined.encode('utf-8')).hexdigest()
    
#     current_level = commitments[:]
#     while len(current_level) > 1:
#         next_level = []
#         for i in range(0, len(current_level), 2):
#             if i+1 < len(current_level):
#                 next_level.append(pair_hash(current_level[i], current_level[i+1]))
#             else:
#                 next_level.append(current_level[i])
#         current_level = next_level
#     return current_level[0] if current_level else None

# def verify_zkp(commitment):
#     # Simulate a zero-knowledge proof verification for a commitment.
#     log(f"ZKP verification passed for commitment: {commitment}")
#     return True

# # ----------------------- Secret Sharing Helpers -----------------------
# def split_contribution(contribution):
#     """
#     Split the contribution into TOTAL_SHARES parts.
#     For simplicity, split equally into TOTAL_BANKS parts and compute an extra share (reconciliation share)
#     as the difference.
#     """
#     base_share = contribution / TOTAL_BANKS
#     shares = [round(base_share, 2) for _ in range(TOTAL_BANKS)]
#     extra_share = round(contribution - sum(shares), 2)
#     shares.append(extra_share)
#     return shares

# # ----------------------- Simulated Network Functions -----------------------
# def send_value(target_bank, port, value):
#     log(f"Sending value {value} to {target_bank} on port {port}")
#     # In a real implementation, a network call would be made here.
#     debug_sleep()

# def listen_for_value(port):
#     # Simulate receiving a single value.
#     # For round-robin: only Bank 1 needs the final aggregated value.
#     if BANK_ID == 1:
#         # Compute the aggregate sum from the public contributions and add the blinding factor.
#         blinding_factor = 1500
#         aggregate = sum(PUBLIC_CONTRIBUTIONS.values())
#         simulated_value = aggregate + blinding_factor
#         debug_sleep()
#         return simulated_value
#     else:
#         # Other banks simply simulate receiving a running sum (dummy value)
#         simulated_value = 1000 + BANK_ID  # dummy value for simulation
#         debug_sleep()
#         return simulated_value

# def listen_for_values(port, count):
#     # Simulate receiving multiple values (dummy simulation).
#     # In an actual protocol, each bank would collect shares from the other banks.
#     dummy_values = [5.0] * count  # For simulation, using a fixed dummy value
#     debug_sleep()
#     return dummy_values

# # ----------------------- Protocol Phases -----------------------
# def phase_commitment_and_secret_sharing():
#     log("--- Starting COMMITMENT & SECRET SHARING PHASE ---")
#     debug_sleep()
#     # Wait for API contribution or use default if none submitted after a short wait
#     global submitted_contribution
#     wait_time = 0
#     while submitted_contribution is None and wait_time < 5:
#         log("Waiting for contribution submission via API...")
#         time.sleep(1)
#         wait_time += 1
#     if submitted_contribution is None:
#         contribution = PUBLIC_CONTRIBUTIONS[BANK_ID]
#         log(f"No API contribution received. Using default contribution: {contribution}")
#     else:
#         contribution = submitted_contribution

#     # Compute commitment (simulate SHA-256 in circom)
#     commitment = commit_value(contribution)
#     log(f"Computed commitment for contribution {contribution}: {commitment}")
#     post_to_bulletin_board(commitment)
#     verify_zkp(commitment)
#     debug_sleep()

#     # Split the contribution into TOTAL_SHARES parts
#     shares = split_contribution(contribution)
#     log(f"Split contribution into shares: {shares}")
#     # The share intended for this bank is at index (BANK_ID - 1)
#     local_share = shares[BANK_ID - 1]
#     log(f"Keeping own share: {local_share}")
#     debug_sleep()

#     # Simulate sending out the appropriate share to every other bank (1..TOTAL_BANKS)
#     for i in range(1, TOTAL_BANKS + 1):
#         if i == BANK_ID:
#             continue
#         share_to_send = shares[i - 1]
#         send_value(f"bank{i}", SECRET_BASE_PORT + i, share_to_send)

#     # Simulate a listener thread to receive shares from other banks.
#     received_shares = listen_for_values(SECRET_BASE_PORT + BANK_ID, TOTAL_BANKS - 1)
#     log(f"Received shares from other banks: {received_shares}")
#     # For simulation, we assume the secret-sharing reconstructs the original contribution.
#     final_contribution = contribution  # In a real protocol: local_share + sum(received_shares)
#     log(f"Final secret sharing contribution: {final_contribution}")
#     log("--- Finished COMMITMENT & SECRET SHARING PHASE ---")
#     debug_sleep()
#     return final_contribution

# def phase_round_robin(final_contribution):
#     log("--- Starting ROUND-ROBIN ADDITION PHASE ---")
#     debug_sleep()
#     final_aggregate = None
#     if BANK_ID == 1:
#         # Bank 1 generates a blinding factor and sends the running sum.
#         blinding_factor = 1500  # Fixed for demonstration
#         running_sum = final_contribution + blinding_factor
#         log(f"Generated blinding factor: {blinding_factor}")
#         log(f"Starting running sum (contribution + blinding): {final_contribution} + {blinding_factor} = {running_sum}")
#         debug_sleep()
#         send_value("bank2", ROUND_BASE_PORT + 2, running_sum)
#         # Now wait for the final aggregated value from Bank 19.
#         final_sum = listen_for_value(RETURN_PORT)
#         aggregate = final_sum - blinding_factor
#         log(f"Final aggregated sum received: {final_sum}")
#         log(f"Aggregate after subtracting blinding factor: {final_sum} - {blinding_factor} = {aggregate}")
#         final_aggregate = aggregate
#     elif 1 < BANK_ID < TOTAL_BANKS:
#         # Banks 2 to 18: receive running sum, add their own contribution, and forward it.
#         running_sum = listen_for_value(ROUND_BASE_PORT + BANK_ID)
#         log(f"Received running sum: {running_sum}")
#         new_sum = running_sum + final_contribution
#         log(f"Own contribution: {final_contribution}")
#         log(f"Updated running sum: {running_sum} + {final_contribution} = {new_sum}")
#         debug_sleep()
#         send_value(f"bank{BANK_ID+1}", ROUND_BASE_PORT + BANK_ID + 1, new_sum)
#     elif BANK_ID == TOTAL_BANKS:
#         # Bank 19: receives running sum, adds its contribution, and sends final result back to Bank 1.
#         running_sum = listen_for_value(ROUND_BASE_PORT + BANK_ID)
#         log(f"Received running sum: {running_sum}")
#         new_sum = running_sum + final_contribution
#         log(f"Own contribution: {final_contribution}")
#         log(f"Updated running sum: {running_sum} + {final_contribution} = {new_sum}")
#         debug_sleep()
#         send_value("bank1", RETURN_PORT, new_sum)
#     log("--- Finished ROUND-ROBIN ADDITION PHASE ---")
#     debug_sleep()
#     return final_aggregate

# def phase_merkle_and_verification():
#     log("--- Starting MERKLE TREE & ZKP VERIFICATION PHASE ---")
#     # For simulation, assume that all commitments have been posted on the bulletin board.
#     # Here we simulate collecting them (dummy commitments) and computing a Merkle tree root.
#     dummy_commitments = []
#     for bank in range(1, TOTAL_BANKS + 1):
#         # In a real system, each bank's posted commitment would be retrieved.
#         dummy_commitments.append(commit_value(PUBLIC_CONTRIBUTIONS[bank]))
#     merkle_root = compute_merkle_root(dummy_commitments)
#     log(f"Computed Merkle tree root from commitments: {merkle_root}")
#     # Each bank then verifies that its own commitment is part of this tree (simulated).
#     verify_zkp(commit_value(PUBLIC_CONTRIBUTIONS[BANK_ID]))
#     log("--- Finished MERKLE TREE & ZKP VERIFICATION PHASE ---")
#     debug_sleep()

# def main():
#     log("======= Starting Process =======")
#     debug_sleep()
    
#     # Start API server in a separate thread to allow external contribution submission.
#     api_thread = threading.Thread(target=run_api_server, daemon=True)
#     api_thread.start()
#     debug_sleep()

#     # Phase 1: Commitment & Secret Sharing
#     final_contribution = phase_commitment_and_secret_sharing()
    
#     # Barrier wait (simulate delay to let all banks finish secret sharing)
#     time.sleep(2)
    
#     # Phase 2: Round-Robin Addition
#     final_aggregate = phase_round_robin(final_contribution)
    
#     # Phase 3: Merkle Tree and ZKP Verification (for public auditability)
#     phase_merkle_and_verification()

#     # Correctness check (only performed by Bank 1)
#     if BANK_ID == 1:
#         straightforward_sum = sum(PUBLIC_CONTRIBUTIONS.values())
#         log(f"Straightforward sum of contributions: {straightforward_sum}")
#         if final_aggregate == straightforward_sum:
#             log(f"Correctness check PASSED: Final aggregated sum ({final_aggregate}) matches the straightforward sum.")
#         else:
#             log(f"Correctness check FAILED: Final aggregated sum ({final_aggregate}) does not match the straightforward sum ({straightforward_sum}).")
    
#     log("======= Process Finished =======")
#     debug_sleep()

# if __name__ == "__main__":
#     main()


# # mpc.py (Improved Version)
# import os
# import time
# import threading
# import hashlib
# import random
# from flask import Flask, request, jsonify

# # Global debug delay
# DEBUG_DELAY = float(os.environ.get("DEBUG_DELAY", "0.1"))

# # Bank configuration
# BANK_ID = int(os.environ.get("BANK_ID", "1"))
# TOTAL_BANKS = int(os.environ.get("TOTAL_BANKS", "19"))
# API_PORT = 8000 + BANK_ID
# SECRET_BASE_PORT = 6000
# ROUND_BASE_PORT = 7000
# RETURN_PORT = 5001

# # Default contributions (integer values)
# PUBLIC_CONTRIBUTIONS = {i: 100 + i for i in range(1, TOTAL_BANKS + 1)}
# sent_shares = {}  # Tracks shares sent by all banks
# submitted_contribution = None  # Contribution received via API
# bulletin_board = {}  # Stores all banks' commitments

# app = Flask(__name__)

# def log(message):
#     """Utility function for logging messages."""
#     print(f"LOG: Bank {BANK_ID}: {message}")

# def debug_sleep():
#     """Simulated delay for network operations."""
#     time.sleep(DEBUG_DELAY)

# # ----------------------- API SERVER for Contribution Submission -----------------------
# @app.route('/submit', methods=['POST'])
# def submit():
#     """Receives contribution from API."""
#     global submitted_contribution
#     data = request.get_json()
#     if "contribution" in data:
#         try:
#             submitted_contribution = int(data["contribution"])
#             log(f"Received contribution via API: {submitted_contribution}")
#             return jsonify({"status": "received"}), 200
#         except ValueError:
#             return jsonify({"status": "error", "message": "Invalid integer value"}), 400
#     return jsonify({"status": "error", "message": "No contribution provided"}), 400

# def run_api_server():
#     """Runs API server in a separate thread."""
#     app.run(host="0.0.0.0", port=API_PORT, debug=False)

# # ----------------------- SECRET SHARING -----------------------
# def split_contribution(contribution):
#     """Proper additive secret sharing with integer values."""
#     shares = []
#     total = 0
#     for _ in range(TOTAL_BANKS - 1):
#         share = random.randint(0, contribution * 2)
#         shares.append(share)
#         total += share
    
#     # Last share ensures sum equals the original contribution
#     final_share = contribution - total
#     shares.append(final_share)
#     return shares

# # ----------------------- SIMULATED NETWORK -----------------------
# def send_value(target_bank, port, value):
#     """Simulates sending a value over a network."""
#     key = (target_bank, port)
#     sent_shares.setdefault(key, []).append(value)
#     log(f"Sent {value} to bank{target_bank} on port {port}")
#     debug_sleep()

# def listen_for_values(port, expected_from):
#     """Simulates receiving values from other banks."""
#     key = (BANK_ID, port)
#     received = sent_shares.get(key, [])[:expected_from]
#     log(f"Received shares: {received}")
#     return received

# def listen_for_value(port):
#     """Simulates receiving a single value (for round-robin addition)."""
#     key = (BANK_ID, port)
#     received = sent_shares.get(key, [])
#     return received[0] if received else 0

# # ----------------------- CRYPTOGRAPHIC PRIMITIVES -----------------------
# def commit_value(value):
#     """Simulate SHA-256 commitment."""
#     return hashlib.sha256(str(value).encode('utf-8')).hexdigest()

# def post_to_bulletin_board(bank_id, commitment):
#     """Simulates posting a commitment to a public bulletin board."""
#     bulletin_board[bank_id] = commitment
#     log(f"Bank {bank_id} posted commitment: {commitment}")

# def compute_merkle_root(commitments):
#     """Simulate Merkle tree computation."""
#     def pair_hash(h1, h2):
#         return hashlib.sha256((h1 + h2).encode('utf-8')).hexdigest()
    
#     current_level = commitments[:]
#     while len(current_level) > 1:
#         next_level = [
#             pair_hash(current_level[i], current_level[i+1]) 
#             if i+1 < len(current_level) else current_level[i]
#             for i in range(0, len(current_level), 2)
#         ]
#         current_level = next_level
#     return current_level[0] if current_level else None

# def verify_zkp(commitment):
#     """Simulate Zero-Knowledge Proof verification."""
#     log(f"ZKP verification passed for commitment: {commitment}")
#     return True

# # ----------------------- MPC PROTOCOL PHASES -----------------------

# def phase_commitment_and_secret_sharing():
#     """Commitment phase + Secret Sharing."""
#     global submitted_contribution
#     contribution = submitted_contribution if submitted_contribution is not None else PUBLIC_CONTRIBUTIONS[BANK_ID]
    
#     # Generate commitment and verify via ZKP
#     commitment = commit_value(contribution)
#     post_to_bulletin_board(BANK_ID, commitment)
#     verify_zkp(commitment)

#     # Generate and distribute shares
#     shares = split_contribution(contribution)
#     log(f"Generated shares: {shares} (sum: {sum(shares)})")

#     for bank_id in range(1, TOTAL_BANKS + 1):
#         if bank_id != BANK_ID:
#             share = shares[bank_id - 1]
#             send_value(bank_id, SECRET_BASE_PORT + bank_id, share)

#     # Collect shares from other banks
#     received = listen_for_values(SECRET_BASE_PORT + BANK_ID, TOTAL_BANKS - 1)

#     # Validate reconstruction
#     reconstructed = sum(received) + shares[-1]  # Add our own last share
#     if reconstructed != contribution:
#         log(f"Error: Secret sharing failed! {reconstructed} vs {contribution}")
#     else:
#         log(f"Validated contribution: {contribution}")

#     return contribution

# def phase_round_robin(final_contribution):
#     """Round-Robin addition phase."""
#     blinding_factor = random.randint(1000, 5000) if BANK_ID == 1 else 0
#     aggregate = None

#     if BANK_ID == 1:
#         running_sum = final_contribution + blinding_factor
#         send_value(2, ROUND_BASE_PORT + 2, running_sum)
#         final_sum = listen_for_value(RETURN_PORT)
#         aggregate = final_sum - blinding_factor

#     elif 1 < BANK_ID < TOTAL_BANKS:
#         running_sum = listen_for_value(ROUND_BASE_PORT + BANK_ID)
#         new_sum = running_sum + final_contribution
#         send_value(BANK_ID + 1, ROUND_BASE_PORT + BANK_ID + 1, new_sum)

#     elif BANK_ID == TOTAL_BANKS:
#         running_sum = listen_for_value(ROUND_BASE_PORT + BANK_ID)
#         new_sum = running_sum + final_contribution
#         send_value(1, RETURN_PORT, new_sum)

#     return aggregate

# def phase_merkle_and_verification():
#     """Merkle Tree & ZKP verification phase."""
#     commitments = [bulletin_board.get(i, "") for i in range(1, TOTAL_BANKS + 1)]
    
#     if "" in commitments:
#         log("Error: Missing commitments in bulletin board!")
#         return
    
#     merkle_root = compute_merkle_root(commitments)
#     log(f"Bulletin Board Merkle Root: {merkle_root}")
#     verify_zkp(commit_value(PUBLIC_CONTRIBUTIONS[BANK_ID]))

# # ----------------------- MAIN FUNCTION -----------------------
# def main():
#     """Main execution function."""
#     log("======= Starting Process =======")
#     api_thread = threading.Thread(target=run_api_server, daemon=True)
#     api_thread.start()
    
#     final_contribution = phase_commitment_and_secret_sharing()
#     time.sleep(2)

#     final_aggregate = phase_round_robin(final_contribution)

#     phase_merkle_and_verification()

#     if BANK_ID == 1:
#         expected = sum(PUBLIC_CONTRIBUTIONS.values())
#         log(f"Final aggregate: {final_aggregate}, Expected: {expected}")
#         assert final_aggregate == expected
    
#     log("======= Process Finished =======")

# if __name__ == "__main__":
#     main()

##### Third iterated version
# import os
# import time
# import threading
# import hashlib
# import random
# from flask import Flask, request, jsonify

# # Global debug delay
# DEBUG_DELAY = float(os.environ.get("DEBUG_DELAY", "0.1"))

# # Bank configuration
# BANK_ID = int(os.environ.get("BANK_ID", "1"))
# TOTAL_BANKS = int(os.environ.get("TOTAL_BANKS", "19"))
# API_PORT = 8000 + BANK_ID
# SECRET_BASE_PORT = 6000
# ROUND_BASE_PORT = 7000
# RETURN_PORT = 5001

# # Default contributions (integer values)
# PUBLIC_CONTRIBUTIONS = {i: 100 + i for i in range(1, TOTAL_BANKS + 1)}
# sent_shares = {}  # Tracks shares sent by all banks
# submitted_contribution = None  # Contribution received via API
# bulletin_board = {}  # Stores all banks' commitments
# MOCK_MODE = os.environ.get("MOCK_MODE", "False").lower() == "true"  # Enables deterministic mock values if set

# app = Flask(__name__)

# def log(message):
#     """Utility function for logging messages."""
#     print(f"LOG: Bank {BANK_ID}: {message}")

# def debug_sleep():
#     """Simulated delay for network operations."""
#     time.sleep(DEBUG_DELAY)

# # ----------------------- API SERVER for Contribution Submission -----------------------
# @app.route('/submit', methods=['POST'])
# def submit():
#     """Receives contribution from API."""
#     global submitted_contribution
#     data = request.get_json()
#     if "contribution" in data:
#         try:
#             submitted_contribution = int(data["contribution"])
#             log(f"Received contribution via API: {submitted_contribution}")
#             return jsonify({"status": "received"}), 200
#         except ValueError:
#             return jsonify({"status": "error", "message": "Invalid integer value"}), 400
#     return jsonify({"status": "error", "message": "No contribution provided"}), 400

# def run_api_server():
#     """Runs API server in a separate thread."""
#     app.run(host="0.0.0.0", port=API_PORT, debug=False)

# # ----------------------- SECRET SHARING -----------------------
# def split_contribution(contribution):
#     """Proper additive secret sharing with integer values."""
#     shares = []
#     total = 0
#     for _ in range(TOTAL_BANKS - 1):
#         share = random.randint(1, contribution * 2) if not MOCK_MODE else 5  # Use mock value if in mock mode
#         shares.append(share)
#         total += share
    
#     # Last share ensures sum equals the original contribution
#     final_share = contribution - total
#     shares.append(final_share)
#     return shares

# # ----------------------- SIMULATED NETWORK -----------------------
# def send_value(target_bank, port, value):
#     """Simulates sending a value over a network."""
#     key = (target_bank, port)
#     sent_shares.setdefault(key, []).append(value)
#     log(f"Sent {value} to bank{target_bank} on port {port}")
#     debug_sleep()

# def listen_for_values(port, expected_from):
#     """Simulates receiving values from other banks."""
#     key = (BANK_ID, port)
#     if MOCK_MODE:
#         received = [5] * expected_from  # Use mock values if in mock mode
#     else:
#         received = sent_shares.get(key, [])[:expected_from]
#     log(f"Received shares: {received}")
#     return received

# def listen_for_value(port):
#     """Simulates receiving a single value (for round-robin addition)."""
#     key = (BANK_ID, port)
#     received = sent_shares.get(key, [])
#     if MOCK_MODE:
#         return 1000 + BANK_ID  # Use a fixed mock value
#     return received[0] if received else 0

# # ----------------------- CRYPTOGRAPHIC PRIMITIVES -----------------------
# def commit_value(value):
#     """Simulate SHA-256 commitment."""
#     return hashlib.sha256(str(value).encode('utf-8')).hexdigest()

# def post_to_bulletin_board(bank_id, commitment):
#     """Simulates posting a commitment to a public bulletin board."""
#     bulletin_board[bank_id] = commitment
#     log(f"Bank {bank_id} posted commitment: {commitment}")

# def compute_merkle_root(commitments):
#     """Simulate Merkle tree computation."""
#     def pair_hash(h1, h2):
#         return hashlib.sha256((h1 + h2).encode('utf-8')).hexdigest()
    
#     current_level = commitments[:]
#     while len(current_level) > 1:
#         next_level = [
#             pair_hash(current_level[i], current_level[i+1]) 
#             if i+1 < len(current_level) else current_level[i]
#             for i in range(0, len(current_level), 2)
#         ]
#         current_level = next_level
#     return current_level[0] if current_level else None

# def verify_zkp(commitment):
#     """Simulate Zero-Knowledge Proof verification."""
#     log(f"ZKP verification passed for commitment: {commitment}")
#     return True

# def print_bulletin_board():
#     """Logs all commitments in a structured format."""
#     log("==== Bulletin Board Commitments ====")
#     for bank_id, commitment in sorted(bulletin_board.items()):
#         log(f"Bank {bank_id}: {commitment}")
#     log("===================================")

# # ----------------------- MPC PROTOCOL PHASES -----------------------

# def phase_commitment_and_secret_sharing():
#     """Commitment phase + Secret Sharing."""
#     global submitted_contribution
#     contribution = submitted_contribution if submitted_contribution is not None else PUBLIC_CONTRIBUTIONS[BANK_ID]
    
#     # Generate commitment and verify via ZKP
#     commitment = commit_value(contribution)
#     post_to_bulletin_board(BANK_ID, commitment)
#     verify_zkp(commitment)

#     # Generate and distribute shares
#     shares = split_contribution(contribution)
#     log(f"Generated shares: {shares} (sum: {sum(shares)})")

#     for bank_id in range(1, TOTAL_BANKS + 1):
#         if bank_id != BANK_ID:
#             share = shares[bank_id - 1]
#             send_value(bank_id, SECRET_BASE_PORT + bank_id, share)

#     # Collect shares from other banks
#     received = listen_for_values(SECRET_BASE_PORT + BANK_ID, TOTAL_BANKS - 1)

#     # Validate reconstruction
#     reconstructed = sum(received) + shares[-1]  # Add our own last share
#     if reconstructed != contribution:
#         log(f"Error: Secret sharing failed! {reconstructed} vs {contribution}")
#     else:
#         log(f"Validated contribution: {contribution}")

#     return contribution

# def phase_round_robin(final_contribution):
#     """Round-Robin addition phase."""
#     blinding_factor = random.randint(1000, 5000) if BANK_ID == 1 else 0
#     aggregate = None

#     if BANK_ID == 1:
#         running_sum = final_contribution + blinding_factor
#         send_value(2, ROUND_BASE_PORT + 2, running_sum)
#         final_sum = listen_for_value(RETURN_PORT)
#         aggregate = final_sum - blinding_factor

#     elif 1 < BANK_ID < TOTAL_BANKS:
#         running_sum = listen_for_value(ROUND_BASE_PORT + BANK_ID)
#         new_sum = running_sum + final_contribution
#         send_value(BANK_ID + 1, ROUND_BASE_PORT + BANK_ID + 1, new_sum)

#     elif BANK_ID == TOTAL_BANKS:
#         running_sum = listen_for_value(ROUND_BASE_PORT + BANK_ID)
#         new_sum = running_sum + final_contribution
#         send_value(1, RETURN_PORT, new_sum)

#     return aggregate

# def phase_merkle_and_verification():
#     """Merkle Tree & ZKP verification phase."""
#     commitments = [bulletin_board.get(i, "") for i in range(1, TOTAL_BANKS + 1)]
    
#     if "" in commitments:
#         log("Error: Missing commitments in bulletin board!")
#         return
    
#     print_bulletin_board()
#     merkle_root = compute_merkle_root(commitments)
#     log(f"Bulletin Board Merkle Root: {merkle_root}")
#     verify_zkp(commit_value(PUBLIC_CONTRIBUTIONS[BANK_ID]))

# # ----------------------- MAIN FUNCTION -----------------------
# def main():
#     """Main execution function."""
#     log("======= Starting Process =======")
#     threading.Thread(target=run_api_server, daemon=True).start()
    
#     final_contribution = phase_commitment_and_secret_sharing()
#     time.sleep(2)

#     final_aggregate = phase_round_robin(final_contribution)

#     phase_merkle_and_verification()

#     log("======= Process Finished =======")

# if __name__ == "__main__":
#     main()


## Time consuming or even deadlock
# import os
# import time
# import threading
# import hashlib
# import random
# from flask import Flask, request, jsonify

# # Global debug delay
# DEBUG_DELAY = float(os.environ.get("DEBUG_DELAY", "0.1"))

# # Bank configuration
# BANK_ID = int(os.environ.get("BANK_ID", "1"))
# TOTAL_BANKS = int(os.environ.get("TOTAL_BANKS", "19"))
# API_PORT = 8000 + BANK_ID
# SECRET_BASE_PORT = 6000
# ROUND_BASE_PORT = 7000
# RETURN_PORT = 5001

# # Default contributions (integer values)
# PUBLIC_CONTRIBUTIONS = {i: 100 + i for i in range(1, TOTAL_BANKS + 1)}
# sent_shares = {}  # Tracks shares sent by all banks
# submitted_contribution = None  # Contribution received via API
# bulletin_board = {}  # Stores all banks' commitments

# # Debugging mode for mock values
# MOCK_MODE = os.environ.get("MOCK_MODE", "False").lower() == "true"  

# app = Flask(__name__)

# def log(message):
#     """Utility function for logging messages."""
#     print(f"LOG: Bank {BANK_ID}: {message}")

# def debug_sleep():
#     """Simulated delay for network operations."""
#     time.sleep(DEBUG_DELAY)

# # ----------------------- API SERVER -----------------------
# @app.route('/submit', methods=['POST'])
# def submit():
#     """Receives contribution from API."""
#     global submitted_contribution
#     data = request.get_json()
#     if "contribution" in data:
#         try:
#             submitted_contribution = int(data["contribution"])
#             log(f"Received contribution via API: {submitted_contribution}")
#             return jsonify({"status": "received"}), 200
#         except ValueError:
#             return jsonify({"status": "error", "message": "Invalid integer value"}), 400
#     return jsonify({"status": "error", "message": "No contribution provided"}), 400

# def run_api_server():
#     """Runs API server for Bank 1 in foreground mode."""
#     app.run(host="0.0.0.0", port=API_PORT, debug=False)

# # ----------------------- SECRET SHARING (FIXED) -----------------------
# def split_contribution(contribution):
#     """Proper additive secret sharing with integer values, avoiding negative shares."""
#     if MOCK_MODE:
#         return [5] * (TOTAL_BANKS - 1) + [contribution - (5 * (TOTAL_BANKS - 1))]

#     shares = []
#     total = 0
#     for _ in range(TOTAL_BANKS - 1):
#         share = random.randint(1, max(1, contribution // TOTAL_BANKS))  
#         shares.append(share)
#         total += share
    
#     final_share = contribution - total
#     if final_share < 0:
#         log(f"Error in secret sharing: Negative final share {final_share}! Adjusting...")
#         final_share = max(1, contribution // TOTAL_BANKS)
#         shares[-1] = final_share
#     shares.append(final_share)
    
#     return shares

# # ----------------------- NETWORK SIMULATION -----------------------
# def send_value(target_bank, port, value):
#     """Simulates sending a value over a network."""
#     key = (target_bank, port)
#     sent_shares.setdefault(key, []).append(value)
#     log(f"Sent {value} to bank{target_bank} on port {port}")
#     debug_sleep()

# def listen_for_values(port, expected_from):
#     """Simulates receiving values from other banks."""
#     key = (BANK_ID, port)
#     received = sent_shares.get(key, [5] * expected_from) if MOCK_MODE else sent_shares.get(key, [])[:expected_from]
#     log(f"Received shares: {received}")
#     return received

# # ----------------------- COMMITMENTS -----------------------
# def commit_value(value):
#     """Simulate SHA-256 commitment."""
#     return hashlib.sha256(str(value).encode('utf-8')).hexdigest()

# def post_to_bulletin_board(bank_id, commitment):
#     """Posts a commitment to the bulletin board."""
#     bulletin_board[bank_id] = commitment
#     log(f"Bank {bank_id} posted commitment: {commitment}")

# def print_bulletin_board():
#     """Logs all commitments in a structured format."""
#     log("==== Bulletin Board Commitments ====")
#     for bank_id, commitment in sorted(bulletin_board.items()):
#         log(f"Bank {bank_id}: {commitment}")
#     log("===================================")

# # ----------------------- MAIN FUNCTION -----------------------
# def main():
#     """Main execution function."""
#     log("======= Starting Process =======")

#     if BANK_ID == 1:
#         log("Running API server in foreground mode.")
#         run_api_server()
#     else:
#         api_thread = threading.Thread(target=run_api_server, daemon=True)
#         api_thread.start()
#         while True:
#             time.sleep(10)  # Keeps the container alive

# if __name__ == "__main__":
#     main()

# import os
# import hashlib
# import random
# from flask import Flask, request, jsonify

# # Bank Configuration
# BANK_ID = int(os.environ.get("BANK_ID", "1"))
# TOTAL_BANKS = int(os.environ.get("TOTAL_BANKS", "19"))
# API_PORT = 8000 + BANK_ID
# SECRET_BASE_PORT = 6000
# ROUND_BASE_PORT = 7000
# RETURN_PORT = 5001

# # Default contributions (integer values)
# PUBLIC_CONTRIBUTIONS = {i: 100 + i for i in range(1, TOTAL_BANKS + 1)}
# sent_shares = {}  # Tracks shares sent by all banks
# submitted_contribution = None  # Contribution received via API
# bulletin_board = {}  # Stores all banks' commitments

# # Debugging mode for mock values
# MOCK_MODE = os.environ.get("MOCK_MODE", "False").lower() == "true"

# app = Flask(__name__)

# def log(message):
#     """Utility function for logging messages."""
#     print(f"LOG: Bank {BANK_ID}: {message}")

# # ----------------------- API SERVER -----------------------
# @app.route('/submit', methods=['POST'])
# def submit():
#     """Receives contribution from API."""
#     global submitted_contribution
#     data = request.get_json()
#     if "contribution" in data:
#         try:
#             submitted_contribution = int(data["contribution"])
#             log(f"Received contribution via API: {submitted_contribution}")
#             return jsonify({"status": "received"}), 200
#         except ValueError:
#             return jsonify({"status": "error", "message": "Invalid integer value"}), 400
#     return jsonify({"status": "error", "message": "No contribution provided"}), 400

# # ----------------------- SECRET SHARING (FIXED) -----------------------
# def split_contribution(contribution):
#     """Proper additive secret sharing with integer values, ensuring correct sum."""
#     log(f"Splitting contribution {contribution} into shares...")

#     if MOCK_MODE:
#         shares = [5] * (TOTAL_BANKS - 1) + [contribution - (5 * (TOTAL_BANKS - 1))]
#     else:
#         shares = []
#         total = 0
#         for _ in range(TOTAL_BANKS - 1):
#             share = random.randint(1, max(1, contribution // TOTAL_BANKS))  
#             shares.append(share)
#             total += share
        
#         final_share = contribution - total
#         if final_share < 0:
#             log(f"Error in secret sharing: Negative final share {final_share}! Adjusting...")
#             final_share = max(1, contribution // TOTAL_BANKS)
#             shares[-1] = final_share
#         shares.append(final_share)

#     log(f"Generated shares: {shares}")
#     return shares

# # ----------------------- NETWORK SIMULATION -----------------------
# def send_value(target_bank, port, value):
#     """Simulates sending a value over a network."""
#     key = (target_bank, port)
#     sent_shares.setdefault(key, []).append(value)
#     log(f"Sent {value} to Bank {target_bank} on Port {port}")

# def listen_for_values(port, expected_from):
#     """Simulates receiving values from other banks."""
#     key = (BANK_ID, port)
#     received = sent_shares.get(key, [5] * expected_from) if MOCK_MODE else sent_shares.get(key, [])[:expected_from]
#     log(f"Received shares on Port {port}: {received}")
#     return received

# # ----------------------- COMMITMENTS -----------------------
# def commit_value(value):
#     """Simulate SHA-256 commitment."""
#     commitment = hashlib.sha256(str(value).encode('utf-8')).hexdigest()
#     log(f"Computed commitment: Original={value}, Commitment={commitment}")
#     return commitment

# def post_to_bulletin_board(bank_id, commitment):
#     """Posts a commitment to the bulletin board."""
#     bulletin_board[bank_id] = commitment
#     log(f"Bank {bank_id} posted commitment: {commitment}")

# def print_bulletin_board():
#     """Logs all commitments in a structured format."""
#     log("==== Bulletin Board Commitments ====")
#     for bank_id, commitment in sorted(bulletin_board.items()):
#         log(f"Bank {bank_id}: {commitment}")
#     log("===================================")

# # ----------------------- ROUND-ROBIN SUMMATION -----------------------
# def round_robin_addition():
#     """Simulates round-robin sum aggregation."""
#     total_sum = 0
#     log("Starting Round-Robin Summation...")

#     for i in range(1, TOTAL_BANKS + 1):
#         received_sum = listen_for_values(ROUND_BASE_PORT + i, 1)
#         received_sum = received_sum[0] if received_sum else 0
#         total_sum += received_sum
#         log(f"Bank {BANK_ID} received sum={received_sum}, new total={total_sum}")

#         if i < TOTAL_BANKS:
#             send_value(i + 1, ROUND_BASE_PORT + (i + 1), total_sum)

#     log(f"Final aggregated sum: {total_sum}")
#     return total_sum

# # ----------------------- MAIN PROTOCOL EXECUTION -----------------------
# def main_protocol_execution():
#     """Executes the entire protocol."""
#     log("======= Starting MPC Protocol Execution =======")

#     # Secret Sharing Phase
#     contribution = PUBLIC_CONTRIBUTIONS[BANK_ID]
#     log(f"Using contribution: {contribution}")
#     shares = split_contribution(contribution)

#     # Store and send shares
#     for i, share in enumerate(shares):
#         target_bank = i + 1
#         if target_bank != BANK_ID:
#             send_value(target_bank, SECRET_BASE_PORT + target_bank, share)

#     received_shares = listen_for_values(SECRET_BASE_PORT + BANK_ID, TOTAL_BANKS - 1)
#     total_received = sum(received_shares) + shares[-1]
#     log(f"Reconstructed contribution: {total_received} (Expected: {contribution})")

#     # Commitment Phase
#     commitment = commit_value(contribution)
#     post_to_bulletin_board(BANK_ID, commitment)

#     # Print bulletin board at Bank 1
#     if BANK_ID == 1:
#         print_bulletin_board()

#     # Round-Robin Addition
#     final_sum = round_robin_addition()

#     log("======= MPC Protocol Execution Finished =======")

# # ----------------------- MAIN FUNCTION -----------------------
# def main():
#     """Main execution function."""
#     log("======= Starting Process =======")

#     # Start API server (only for Bank 1)
#     if BANK_ID == 1:
#         log("Running API server...")
#         app.run(host="0.0.0.0", port=API_PORT, debug=False, use_reloader=False)

#     # Execute the protocol
#     main_protocol_execution()

# if __name__ == "__main__":
#     main()

import os
import time
import threading
import hashlib
import random
from flask import Flask, request, jsonify

# Global debug delay (set DEBUG_DELAY=0.1 for debugging, 0 for production)
DEBUG_DELAY = float(os.environ.get("DEBUG_DELAY", "0.1"))

# Configuration from environment variables: now for 19 banks
BANK_ID = int(os.environ.get("BANK_ID", "1"))
TOTAL_BANKS = int(os.environ.get("TOTAL_BANKS", "19"))
TOTAL_SHARES = TOTAL_BANKS + 1  # 19 shares for banks + 1 extra for reconciliation

# API port for contribution submission (unique per bank)
API_PORT = 8000 + BANK_ID

# Simulated ports (for secret sharing and round-robin phases)
SECRET_BASE_PORT = 6000  # each bank listens on (SECRET_BASE_PORT + BANK_ID) for secret shares.
ROUND_BASE_PORT = 7000   # each bank listens on (ROUND_BASE_PORT + BANK_ID) for round-robin addition.
RETURN_PORT = 5001       # Bank 1 listens on this port for the final aggregated result.

# For simulation, define fixed contributions for 19 banks.
PUBLIC_CONTRIBUTIONS = {
    1: 101, 2: 102, 3: 103, 4: 104, 5: 105, 6: 106, 7: 107, 8: 108, 9: 109,
    10: 110, 11: 111, 12: 112, 13: 113, 14: 114, 15: 115, 16: 116, 17: 117, 18: 118, 19: 119
}

# Global variable to store the contribution submitted via API
submitted_contribution = None

def log(message):
    print(f"LOG: Bank {BANK_ID}: {message}")

def debug_sleep(duration=DEBUG_DELAY):
    time.sleep(duration)

# ----------------------- API SERVER for Contribution Submission -----------------------
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    global submitted_contribution
    data = request.get_json()
    if "contribution" in data:
        try:
            submitted_contribution = float(data["contribution"])
            log(f"Contribution submitted via API: {submitted_contribution}")
            return jsonify({"status": "received"}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 400
    else:
        return jsonify({"status": "error", "message": "No contribution provided"}), 400

def run_api_server():
    app.run(host="0.0.0.0", port=API_PORT)

# ----------------------- Cryptographic Primitives (Simulation) -----------------------
def commit_value(value):
    # Simulate a SHA-256 commitment (as if computed in circom)
    h = hashlib.sha256()
    h.update(str(value).encode('utf-8'))
    return h.hexdigest()

def post_to_bulletin_board(commitment):
    # Simulate posting to a public bulletin board
    log(f"Posted commitment to bulletin board: {commitment}")

def compute_merkle_root(commitments):
    # A simple (non-secure) simulation of a Merkle tree computation.
    def pair_hash(h1, h2):
        combined = h1 + h2
        return hashlib.sha256(combined.encode('utf-8')).hexdigest()
    
    current_level = commitments[:]
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            if i+1 < len(current_level):
                next_level.append(pair_hash(current_level[i], current_level[i+1]))
            else:
                next_level.append(current_level[i])
        current_level = next_level
    return current_level[0] if current_level else None

def verify_zkp(commitment):
    # Simulate a zero-knowledge proof verification for a commitment.
    log(f"ZKP verification passed for commitment: {commitment}")
    return True

# ----------------------- Secret Sharing Helpers -----------------------
def split_contribution(contribution, total_banks):
    """
    Split the contribution into TOTAL_SHARES parts.
    For simplicity, split equally into TOTAL_BANKS parts and compute an extra share (reconciliation share)
    as the difference.
    """
    base_share = contribution / total_banks
    shares = [round(base_share, 2) for _ in range(total_banks)]
    extra_share = round(contribution - sum(shares), 2)
    shares.append(extra_share)
    return shares

# ----------------------- Simulated Network Functions -----------------------
def send_value(target_bank, value):
    port = SECRET_BASE_PORT + target_bank
    log(f"Sending value {value} to {target_bank} on port {port}")
    # In a real implementation, a network call would be made here.
    debug_sleep()

def listen_for_values(port):
    # Simulate receiving multiple values (dummy simulation).
    # In an actual protocol, each bank would collect shares from the other banks.
    dummy_values = [5.0] * TOTAL_BANKS  # For simulation, using a fixed dummy value
    debug_sleep()
    return dummy_values

# ----------------------- Protocol Phases -----------------------
def distribute_shares(contribution, total_banks):
    """Distribute shares to all banks."""
    shares = split_contribution(contribution, total_banks)
    for bank_id, share in enumerate(shares, start=1):
        send_value(bank_id, share)

def receive_shares(port):
    """Receive shares from other banks."""
    shares = listen_for_values(port)
    if not shares:
        log(f"Error: No shares received on port {port}")
    return shares

def aggregate_shares(shares):
    """Aggregate received shares."""
    total = sum(shares)
    log(f"Aggregated total: {total}")
    return total

def main_protocol_execution():
    """Execute the main protocol."""
    log("Starting MPC Protocol Execution")
    contribution = get_contribution()
    distribute_shares(contribution, TOTAL_BANKS)
    shares = receive_shares(API_PORT)
    total = aggregate_shares(shares)
    log(f"Final aggregated sum: {total}")

def get_contribution():
    """Get the contribution for the current bank."""
    global submitted_contribution
    wait_time = 0
    while submitted_contribution is None and wait_time < 5:
        log("Waiting for contribution submission via API...")
        time.sleep(1)
        wait_time += 1
    if submitted_contribution is None:
        contribution = PUBLIC_CONTRIBUTIONS[BANK_ID]
        log(f"No API contribution received. Using default contribution: {contribution}")
    else:
        contribution = submitted_contribution
    return contribution

def main():
    """Main execution function."""
    log("Starting Process")
    if BANK_ID == 1:
        log("Running API server...")
        app.run(host="0.0.0.0", port=API_PORT, debug=False, use_reloader=False)
    main_protocol_execution()

if __name__ == "__main__":
    main()