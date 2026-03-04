import os

# Aapka Data Verification
ACCOUNT_ID = "AC76b2bde6569c5fefb1ad2bbca8cd628d"
AUTH_TOKEN = "71426b6771aef7b779bc123a8edba680"

def start_demo():
    print(f"--- HACKING SIMULATOR v1.0 ---")
    print(f"Logged in: {ACCOUNT_ID}")
    print("-" * 30)
    
    print("1. Generate Fake Camera Link")
    print("2. View Captured Data")
    print("3. Exit")
    
    choice = input("\nSelect Option: ")
    
    if choice == '1':
        # Hacker yahan ek attractive link banata hai
        print("\n[!] Generating Link...")
        print("Link: http://free-recharge-offer.ngrok.io")
        print("[*] Waiting for victim to click 'Allow' on Camera...")
    elif choice == '2':
        print("\n[+] Checking 'captured_images' folder...")
        # Asli hack mein yahan photos dikhayi jati hain
        print("Status: No data found yet.")
    else:
        print("Exiting...")

if __name__ == "__main__":
    start_demo()
