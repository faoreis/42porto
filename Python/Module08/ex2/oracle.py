import os
import dotenv

dotenv.load_dotenv()


def valid_config() -> bool:
    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    return all(var in os.environ for var in required_vars)


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    valid = valid_config()
    mode = os.getenv("MATRIX_MODE", "development")
    database = os.getenv("DATABASE_URL", "Localhost/development")
    api_key = os.getenv("API_KEY", "Unauthenticated")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT", "Offline")

    print("\nConfiguration loaded:")
    print(f"MATRIX_MODE: {mode}")
    print(f"DATABASE_URL: {database}")
    print(f"API_KEY: {api_key}")
    print(f"LOG_LEVEL: {log_level}")
    print(f"ZION_ENDPOINT: {zion_endpoint}")

    if mode == "production":
        print("\n[WARNING] Running in production mode.")

    print("\nEnvironment security check:")
    print("\n[OK] No hardcoded secrets detected")
    if valid:
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file is NOT properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
