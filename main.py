# main.py

from app.app import App  # Importing the App class from your app module

if __name__ == "__main__":
    app = App()  # Create an instance of the App class
    app.start()  # Start the REPL loop
