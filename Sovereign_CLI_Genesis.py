# Sovereign CLI Genesis
# Version 1.0 | Author: RyanFromMontana x HRH Theophilus

import hashlib
import json
import os

WELCOME_MESSAGE = '''
------------------------------------------------
Sovereign CLI Genesis - Scroll Invocation Engine
------------------------------------------------
'''

scroll_registry = {}

def load_scroll(filepath):
    try:
        with open(filepath, 'r') as file:
            scroll = json.load(file)
            scroll_title = scroll.get('scroll_title', 'Untitled Scroll')
            scroll_hash = hashlib.sha256(json.dumps(scroll, sort_keys=True).encode('utf-8')).hexdigest()
            scroll_registry[scroll_hash] = scroll
            print(f"Scroll '{scroll_title}' loaded successfully.")
            print(f"Scroll Hash: {scroll_hash}")
    except Exception as e:
        print(f"Error loading scroll: {e}")

def list_scrolls():
    if not scroll_registry:
        print("No scrolls loaded yet.")
        return
    print("\nLoaded Scrolls:")
    for hash_val, scroll in scroll_registry.items():
        print(f"- {scroll.get('scroll_title', 'Untitled')} (Hash: {hash_val})")

def invoke_scroll():
    if not scroll_registry:
        print("No scrolls loaded yet.")
        return
    print("\nAvailable Scrolls to Invoke:")
    for idx, (hash_val, scroll) in enumerate(scroll_registry.items()):
        print(f"[{idx}] {scroll.get('scroll_title', 'Untitled')}")
    choice = input("Select a scroll number to invoke: ")
    try:
        choice_idx = int(choice)
        selected_hash = list(scroll_registry.keys())[choice_idx]
        print(f"Invoking Scroll: {scroll_registry[selected_hash].get('scroll_title', 'Untitled')}")
        print("Invocation Complete: Sovereign Presence Acknowledged.")
    except Exception as e:
        print(f"Error invoking scroll: {e}")

def main():
    print(WELCOME_MESSAGE)
    while True:
        print("\nOptions:")
        print("1. Load a Scroll (.json)")
        print("2. List Loaded Scrolls")
        print("3. Invoke a Scroll")
        print("4. Exit")

        choice = input("Select an option: ")
        if choice == '1':
            path = input("Enter path to scroll .json file: ")
            load_scroll(path)
        elif choice == '2':
            list_scrolls()
        elif choice == '3':
            invoke_scroll()
        elif choice == '4':
            print("Exiting Sovereign CLI Genesis. Stay sovereign.")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()