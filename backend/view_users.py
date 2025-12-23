"""
Script to view all registered users in the database
Usage: python view_users.py
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd

# Load environment variables
load_dotenv()

def view_all_users():
    """View all users in the database"""
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        print("❌ DATABASE_URL not found in .env file")
        return

    try:
        # Create database engine
        engine = create_engine(database_url)

        # Query all users (without passwords for security)
        query = """
        SELECT
            id,
            username,
            email,
            created_at
        FROM users
        ORDER BY created_at DESC
        """

        # Execute query
        with engine.connect() as conn:
            result = conn.execute(text(query))
            users = result.fetchall()

            if not users:
                print("\n📋 No users found in database")
                return

            # Convert to pandas DataFrame for better display
            df = pd.DataFrame(users, columns=['ID', 'Username', 'Email', 'Created At'])

            print("\n" + "="*80)
            print("👥 REGISTERED USERS")
            print("="*80)
            print(f"\nTotal Users: {len(users)}\n")
            print(df.to_string(index=False))
            print("\n" + "="*80)

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nMake sure:")
        print("1. Backend is running")
        print("2. Database connection is working")
        print("3. Users table exists")

def check_database_connection():
    """Check if database connection is working"""
    database_url = os.getenv("DATABASE_URL")

    try:
        engine = create_engine(database_url)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("\n🔍 Checking database connection...")
    if check_database_connection():
        view_all_users()
