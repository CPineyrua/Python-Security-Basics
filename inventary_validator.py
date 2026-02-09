# PROJECT 01: Input Sanitization (Whitelisting)
# Author: Carlos Pineyrua (@CPineyrua)

def start_system():
    # Whitelist: Only these items are secure and allowed
    allowed_fruits = ["apple", "pear", "banana", "grape"]
    
    print("--- INVENTORY CONTROL SYSTEM ---")
    user_input = input("Enter fruit name to register: ").strip().lower()

    # Security Logic: Validate before processing
    if user_input in allowed_fruits:
        print(f"[SUCCESS] '{user_input}' validated and registered.")
    elif user_input == "":
        print("[ERROR] Input field cannot be empty.")
    else:
        print(f"[SECURITY ALERT] Unauthorized entry attempt: '{user_input}'")

if __name__ == "__main__":
    start_system()
