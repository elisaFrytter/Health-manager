import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from healthmanager.app import main

if __name__ == "__main__":
    main().main_loop()
