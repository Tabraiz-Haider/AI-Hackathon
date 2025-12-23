# 🗄️ Neon Database - Data Storage Location

## 📍 Kahan Hai Aapka Data?

Aapka saara login/signup data **Neon PostgreSQL** cloud database mein store hai:

```
┌─────────────────────────────────────────────────────────────────┐
│                    🌐 INTERNET / CLOUD                          │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │           🏢 AWS (Amazon Web Services)                     │ │
│  │           Region: US East (Virginia)                       │ │
│  │                                                            │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │        🗄️  NEON POSTGRESQL DATABASE                 │ │ │
│  │  │        Project: ep-restless-scene-ahp5h76l          │ │ │
│  │  │                                                      │ │ │
│  │  │   ┌─────────────────────────────────────┐          │ │ │
│  │  │   │  📊 Database: neondb                │          │ │ │
│  │  │   │                                      │          │ │ │
│  │  │   │  ┌────────────────────────────┐    │          │ │ │
│  │  │   │  │  📋 Table: users           │    │          │ │ │
│  │  │   │  │                             │    │          │ │ │
│  │  │   │  │  Columns:                   │    │          │ │ │
│  │  │   │  │  ├─ id (Primary Key)        │    │          │ │ │
│  │  │   │  │  ├─ username (Unique)       │    │          │ │ │
│  │  │   │  │  ├─ email (Unique)          │    │          │ │ │
│  │  │   │  │  ├─ hashed_password         │    │          │ │ │
│  │  │   │  │  └─ created_at              │    │          │ │ │
│  │  │   │  │                             │    │          │ │ │
│  │  │   │  │  YOUR DATA IS HERE! ⬆️      │    │          │ │ │
│  │  │   │  └────────────────────────────┘    │          │ │ │
│  │  │   │                                      │          │ │ │
│  │  │   └─────────────────────────────────────┘          │ │ │
│  │  │                                                      │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  │                                                            │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              ↕️  SSL/TLS Encrypted
┌─────────────────────────────────────────────────────────────────┐
│                    💻 YOUR BACKEND SERVER                       │
│                    (localhost:8000)                             │
│                                                                 │
│         Connects to Neon Database using:                        │
│         postgresql://neondb_owner:password@                     │
│         ep-restless-scene-ahp5h76l-pooler.                      │
│         c-3.us-east-1.aws.neon.tech/neondb                     │
└─────────────────────────────────────────────────────────────────┘
```

## 🔗 Database Connection Details

### **Host Information:**
```
Host:     ep-restless-scene-ahp5h76l-pooler.c-3.us-east-1.aws.neon.tech
Port:     6543 (Default Neon port)
Database: neondb
Username: neondb_owner
Region:   US East (Virginia) - AWS
SSL:      Required (Encrypted connection)
```

### **Table Structure:**

```sql
CREATE TABLE users (
    id              SERIAL PRIMARY KEY,
    username        VARCHAR UNIQUE NOT NULL,
    email           VARCHAR UNIQUE NOT NULL,
    hashed_password VARCHAR NOT NULL,
    created_at      TIMESTAMP DEFAULT NOW()
);
```

## 🔍 Data Kaise Dekhen?

### **Option 1: Python Script (Terminal)**
```bash
cd backend
python neon_database_info.py
```
Ye command aapko dikhayega:
- Database location details
- Connection status
- Table information
- Sample user data

### **Option 2: Neon Web Dashboard**
```
1. Visit: https://console.neon.tech/
2. Login with your Neon account
3. Select project: ep-restless-scene-ahp5h76l
4. Click "Tables" to see data
5. Run SQL queries directly
```

### **Option 3: User Manager Tool**
```bash
cd backend
python user_manager.py
```
Interactive menu se:
- View all users
- Search users
- Get user details
- Count total users

## 💾 Data Storage Path

```
Your App (Browser)
       ↓
   POST /auth/signup or /auth/login
       ↓
Backend Server (FastAPI)
       ↓
   Validates & Hashes Password
       ↓
Neon PostgreSQL (Cloud)
   └─ AWS Data Center (US East)
      └─ Project: ep-restless-scene-ahp5h76l
         └─ Database: neondb
            └─ Table: users
               └─ YOUR DATA STORED HERE!
```

## 🔒 Security Features

1. **Password:** Never stored in plain text (bcrypt hashed)
2. **Connection:** SSL/TLS encrypted
3. **Access:** Only through authenticated API
4. **Backup:** Automatic by Neon
5. **Location:** AWS secure data center

## 📊 Example Data Format

When you signup, data is stored like this:

```
id  | username | email           | hashed_password              | created_at
----+----------+-----------------+------------------------------+-------------------
1   | shayan   | shayan@test.com | $2b$12$xxxxxxxxxxxxxxxxxxx...  | 2024-12-22 10:30:00
2   | ahmed    | ahmed@test.com  | $2b$12$xxxxxxxxxxxxxxxxxxx...  | 2024-12-22 10:35:00
```

## ⚡ Quick Commands

```bash
# View database info
cd backend
python neon_database_info.py

# View all users
python view_users.py

# Interactive manager
python user_manager.py

# Initialize database (if needed)
python init_db.py
```

## 🌐 Access URLs

- **Neon Console:** https://console.neon.tech/
- **Your Project:** ep-restless-scene-ahp5h76l
- **Database Name:** neondb
- **Connection Pooler:** Yes (for better performance)

---

**Note:** Aapka data safely AWS ke servers par stored hai. Neon automatic backups bhi leta hai!
