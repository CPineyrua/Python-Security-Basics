# PROJECT: Inventory Input Validation
# Goal: Use whitelisting to prevent unauthorized data entry
# Standards: PEP 8 compliant | Author: @CPineyrua

def start_system():
    # Whitelist: Only these items are secure and allowed
    allowed_items = ["apple", "pear", "banana", "grape"]
    
    print("--- SECURE INVENTORY SYSTEM ---")
    user_input = input("Enter item name to register: ").strip().lower()

    # Security Logic: Whitelisting (Positive Security Model)
    if user_input in allowed_items:
        print(f"[SUCCESS] '{user_input}' is authorized and registered.")
    elif not user_input:
        print("[ERROR] Input cannot be empty.")
    else:
        # We log unauthorized attempts for security auditing
        print(f"[SECURITY ALERT] Unauthorized entry attempt: '{user_input}'")

if __name__ == "__main__":
    start_system()
