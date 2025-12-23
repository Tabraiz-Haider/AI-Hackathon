"""
Neon Database Information and Connection Tester
Shows where and how data is stored in Neon PostgreSQL
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, inspect
import json

load_dotenv()

def parse_database_url():
    """Parse and display Neon database connection details"""
    db_url = os.getenv("DATABASE_URL")

    if not db_url:
        print("❌ DATABASE_URL not found in .env file")
        return None

    # Parse the URL
    # Format: postgresql://username:password@host:port/database
    parts = db_url.replace("postgresql://", "").split("@")

    if len(parts) < 2:
        print("❌ Invalid database URL format")
        return None

    credentials = parts[0].split(":")
    host_db = parts[1].split("/")
    host_port = host_db[0].split(":")

    info = {
        "username": credentials[0],
        "password": "***" + credentials[1][-4:] if len(credentials) > 1 else "N/A",
        "host": host_port[0],
        "port": host_port[1] if len(host_port) > 1 else "6543",
        "database": host_db[1].split("?")[0] if len(host_db) > 1 else "N/A",
        "ssl_mode": "require" if "sslmode=require" in db_url else "prefer"
    }

    return info

def display_connection_info():
    """Display Neon database connection information"""
    print("\n" + "="*80)
    print("NEON POSTGRESQL DATABASE - CONNECTION INFORMATION")
    print("="*80)

    info = parse_database_url()

    if not info:
        return

    print("\n>> Database Location:")
    print(f"   Cloud Provider:  AWS (Amazon Web Services)")
    print(f"   Region:          US East (Virginia)")
    print(f"   Host:            {info['host']}")
    print(f"   Port:            {info['port']}")
    print(f"   Database Name:   {info['database']}")

    print("\n>> Authentication:")
    print(f"   Username:        {info['username']}")
    print(f"   Password:        {info['password']}")
    print(f"   SSL Mode:        {info['ssl_mode']}")

    print("\n>> Data Storage:")
    print(f"   Storage Type:    Cloud PostgreSQL (Serverless)")
    print(f"   Backup:          Automatic (Neon handles this)")
    print(f"   Replication:     Built-in high availability")

    print("="*80)

def check_tables():
    """Check what tables exist in the database"""
    try:
        engine = create_engine(os.getenv("DATABASE_URL"))
        inspector = inspect(engine)

        print("\n" + "="*80)
        print("DATABASE TABLES")
        print("="*80)

        tables = inspector.get_table_names()

        if not tables:
            print("\n[X] No tables found. Run 'python init_db.py' to create tables.")
            return

        print(f"\nFound {len(tables)} table(s):\n")

        for table_name in tables:
            print(f">> Table: {table_name}")
            columns = inspector.get_columns(table_name)

            print(f"   Columns ({len(columns)}):")
            for col in columns:
                col_type = str(col['type'])
                nullable = "NULL" if col['nullable'] else "NOT NULL"
                primary = " [PRIMARY KEY]" if col.get('primary_key') else ""
                print(f"      - {col['name']:<20} {col_type:<20} {nullable}{primary}")

            # Get row count
            with engine.connect() as conn:
                result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
                count = result.scalar()
                print(f"   Total Rows: {count}")

            print()

        print("="*80)

    except Exception as e:
        print(f"\n[X] Error checking tables: {str(e)}")

def test_connection():
    """Test database connection"""
    print("\n" + "="*80)
    print("TESTING DATABASE CONNECTION")
    print("="*80)

    try:
        engine = create_engine(os.getenv("DATABASE_URL"))

        with engine.connect() as conn:
            # Test query
            result = conn.execute(text("SELECT version()"))
            version = result.scalar()

            print("\n[OK] Connection Successful!")
            print(f"\nPostgreSQL Version:")
            print(f"   {version[:80]}...")

            # Get database size
            result = conn.execute(text("""
                SELECT pg_size_pretty(pg_database_size(current_database())) as size
            """))
            size = result.scalar()
            print(f"\nDatabase Size: {size}")

        print("\n" + "="*80)
        return True

    except Exception as e:
        print(f"\n[X] Connection Failed!")
        print(f"Error: {str(e)}")
        print("\n" + "="*80)
        return False

def show_sample_data():
    """Show sample data from users table"""
    try:
        engine = create_engine(os.getenv("DATABASE_URL"))

        print("\n" + "="*80)
        print("SAMPLE USER DATA (Latest 5 users)")
        print("="*80)

        query = """
        SELECT
            id,
            username,
            email,
            created_at
        FROM users
        ORDER BY created_at DESC
        LIMIT 5
        """

        with engine.connect() as conn:
            result = conn.execute(text(query))
            users = result.fetchall()

            if not users:
                print("\n[i] No users registered yet")
                print("\nTo create a user:")
                print("1. Open the app in browser")
                print("2. Click 'Sign Up'")
                print("3. Register a new account")
                print()
                return

            print(f"\n{'ID':<5} {'Username':<20} {'Email':<30} {'Created At':<20}")
            print("-"*80)

            for user in users:
                user_id, username, email, created_at = user
                created_str = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else "N/A"
                print(f"{user_id:<5} {username:<20} {email:<30} {created_str}")

            print("="*80)

            # Total count
            result = conn.execute(text("SELECT COUNT(*) FROM users"))
            total = result.scalar()
            print(f"\nTotal Registered Users: {total}\n")

    except Exception as e:
        print(f"\n[X] Error: {str(e)}\n")

def main():
    """Main function"""
    print("\n" + "="*80)
    print("NEON DATABASE ANALYZER")
    print("="*80)

    # Display connection info
    display_connection_info()

    # Test connection
    if test_connection():
        # Show tables
        check_tables()

        # Show sample data
        show_sample_data()

    print("\n[!] TIP: To access Neon Dashboard:")
    print("   1. Go to: https://console.neon.tech/")
    print("   2. Login with your Neon account")
    print("   3. Select your project: 'ep-restless-scene-ahp5h76l'")
    print("   4. View tables, run queries, and manage data\n")

if __name__ == "__main__":
    try:
        print("\n[*] Checking database connection...")
        engine = create_engine(os.getenv("DATABASE_URL"))
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("[OK] Database connection successful!\n")

        main()

    except Exception as e:
        print(f"\n[X] Database connection failed: {str(e)}")
        print("\nMake sure:")
        print("1. .env file exists with DATABASE_URL")
        print("2. Database is accessible")
        print("3. Backend dependencies are installed\n")
