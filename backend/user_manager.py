"""
User Management Tool - View, Search, and Manage Users
Usage: python user_manager.py
"""
import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from datetime import datetime

# Load environment variables
load_dotenv()

def get_engine():
    """Get database engine"""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        print("❌ DATABASE_URL not found in .env file")
        sys.exit(1)
    return create_engine(database_url)

def view_all_users():
    """View all users"""
    engine = get_engine()

    query = """
    SELECT id, username, email, created_at
    FROM users
    ORDER BY created_at DESC
    """

    try:
        with engine.connect() as conn:
            result = conn.execute(text(query))
            users = result.fetchall()

            if not users:
                print("\n📋 No users found in database\n")
                return

            print("\n" + "="*90)
            print("👥 ALL REGISTERED USERS")
            print("="*90)
            print(f"{'ID':<5} {'Username':<20} {'Email':<30} {'Created At':<20}")
            print("-"*90)

            for user in users:
                user_id, username, email, created_at = user
                created_str = created_at.strftime("%Y-%m-%d %H:%M") if created_at else "N/A"
                print(f"{user_id:<5} {username:<20} {email:<30} {created_str:<20}")

            print("="*90)
            print(f"\nTotal Users: {len(users)}\n")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")

def search_user(search_term):
    """Search for a user by username or email"""
    engine = get_engine()

    query = """
    SELECT id, username, email, created_at
    FROM users
    WHERE username LIKE :search OR email LIKE :search
    """

    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), {"search": f"%{search_term}%"})
            users = result.fetchall()

            if not users:
                print(f"\n❌ No users found matching '{search_term}'\n")
                return

            print(f"\n🔍 Search Results for '{search_term}':")
            print("="*90)
            print(f"{'ID':<5} {'Username':<20} {'Email':<30} {'Created At':<20}")
            print("-"*90)

            for user in users:
                user_id, username, email, created_at = user
                created_str = created_at.strftime("%Y-%m-%d %H:%M") if created_at else "N/A"
                print(f"{user_id:<5} {username:<20} {email:<30} {created_str:<20}")

            print("="*90 + "\n")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")

def get_user_details(username):
    """Get detailed info about a specific user"""
    engine = get_engine()

    query = """
    SELECT id, username, email, created_at
    FROM users
    WHERE username = :username
    """

    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), {"username": username})
            user = result.fetchone()

            if not user:
                print(f"\n❌ User '{username}' not found\n")
                return

            user_id, username, email, created_at = user
            created_str = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else "N/A"

            print("\n" + "="*60)
            print(f"👤 USER DETAILS: {username}")
            print("="*60)
            print(f"ID:           {user_id}")
            print(f"Username:     {username}")
            print(f"Email:        {email}")
            print(f"Created At:   {created_str}")
            print("="*60 + "\n")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")

def count_users():
    """Count total users"""
    engine = get_engine()

    query = "SELECT COUNT(*) FROM users"

    try:
        with engine.connect() as conn:
            result = conn.execute(text(query))
            count = result.scalar()
            print(f"\n📊 Total Registered Users: {count}\n")
            return count

    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")
        return 0

def main_menu():
    """Display main menu"""
    while True:
        print("\n" + "="*60)
        print("🔧 USER MANAGEMENT TOOL")
        print("="*60)
        print("1. View All Users")
        print("2. Search User")
        print("3. Get User Details")
        print("4. Count Users")
        print("5. Exit")
        print("="*60)

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            view_all_users()
        elif choice == "2":
            search_term = input("\nEnter username or email to search: ").strip()
            if search_term:
                search_user(search_term)
            else:
                print("\n❌ Search term cannot be empty\n")
        elif choice == "3":
            username = input("\nEnter username: ").strip()
            if username:
                get_user_details(username)
            else:
                print("\n❌ Username cannot be empty\n")
        elif choice == "4":
            count_users()
        elif choice == "5":
            print("\n👋 Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    try:
        print("\n🔍 Checking database connection...")
        engine = get_engine()
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Database connection successful!\n")

        main_menu()

    except Exception as e:
        print(f"\n❌ Database connection failed: {str(e)}")
        print("\nMake sure:")
        print("1. .env file exists with DATABASE_URL")
        print("2. Database is accessible")
        print("3. Backend dependencies are installed\n")
