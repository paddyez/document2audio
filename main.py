# main.py

import model_manager

def main():
    """
    Main entry point of the program.
    """
    print("Fetching available engines...")
    model_manager.info_from_model_manager()

if __name__ == "__main__":
    main()