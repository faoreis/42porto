import os
import dotenv

if not dotenv.load_dotenv():
    print("No configuration found")
else:
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("")
    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    print(mode)
    if os.getenv("DATABASE_URL"):
    print(database)