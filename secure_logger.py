import datetime # Para saber CUÁNDO ocurre el evento

def log_event(message):
    """Guarda eventos en un archivo de texto"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 'a' significa 'append' (añadir al final sin borrar lo anterior)
    with open("security.log", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

def start_system():
    allowed_fruits = ["apple", "pear", "banana"]
    
    print("--- SECURE INVENTORY SYSTEM ---")
    user_input = input("Register fruit: ").strip().lower()

    if user_input in allowed_fruits:
        print(f"[OK] {user_input} registered.")
        log_event(f"SUCCESS: Resource '{user_input}' accessed.")
    else:
        print("[ALERT] Unauthorized entry!")
        log_event(f"WARNING: Unauthorized attempt with input: '{user_input}'")

if __name__ == "__main__":
    start_system()
