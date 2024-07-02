import os
from dotenv import load_dotenv
import sys

load_dotenv()

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')

    @classmethod
    def validate_configuration(cls):
        errors = []
        if not cls.DATABASE_URI:
            errors.append("DATABASE_URI is not set or is empty in the environment variables.")
        
        if errors:
            print("Configuration Error:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            sys.exit(1)

Config.validate_configuration()