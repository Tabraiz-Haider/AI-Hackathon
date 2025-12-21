# Google OAuth Setup Guide

## Problem
You're getting "Error 401: invalid_client" because the Google OAuth client ID doesn't exist or isn't properly configured.

## Solution: Follow These Steps

### Step 1: Go to Google Cloud Console
1. Open: https://console.cloud.google.com/
2. Login with: shahyanqamar540@gmail.com

### Step 2: Create a New Project
1. Click "Select a project" in the top bar
2. Click "New Project"
3. Project name: **Physical AI Textbook**
4. Click "Create"

### Step 3: Configure OAuth Consent Screen
1. In left sidebar: **APIs & Services** > **OAuth consent screen**
2. Select **External** user type
3. Click "Create"
4. Fill in the form:
   - **App name**: Physical AI Textbook
   - **User support email**: shahyanqamar540@gmail.com
   - **Developer contact email**: shahyanqamar540@gmail.com
5. Click "Save and Continue" (3 times through all screens)
6. On "Test users" screen, add your email: shahyanqamar540@gmail.com
7. Click "Save and Continue"

### Step 4: Create OAuth Credentials
1. In left sidebar: **APIs & Services** > **Credentials**
2. Click **"Create Credentials"** > **"OAuth client ID"**
3. Application type: **Web application**
4. Name: **Physical AI Web Client**
5. **Authorized JavaScript origins** - Add these URLs:
   ```
   http://localhost:3000
   http://localhost:8000
   ```
6. **Authorized redirect URIs** - Add:
   ```
   http://localhost:3000
   ```
7. Click **"Create"**

### Step 5: Copy Your Credentials
After clicking Create, you'll see a popup with:
- **Client ID**: Looks like `688653693393-xxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com`
- **Client Secret**: Looks like `GOCSPX-xxxxxxxxxxxxxxxxxxxx`

**COPY BOTH OF THESE!**

### Step 6: Update Your .env File
1. Open: `backend/.env`
2. Replace these lines:
   ```
   GOOGLE_CLIENT_ID=YOUR_CLIENT_ID_HERE
   GOOGLE_CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE
   ```
   With your actual credentials from Step 5

3. Also update in: `src/components/Auth/Login.tsx` line 34:
   Replace the client_id with your new Client ID

### Step 7: Restart Backend Server
```bash
cd backend
python main.py
```

### Step 8: Test Login
1. Open http://localhost:3000
2. Click "Login"
3. Click the Google button
4. It should work now!

## Important Notes
- Make sure your Google account (shahyanqamar540@gmail.com) is added as a Test User
- The app will be in "Testing" mode, only test users can sign in
- For production, you'll need to publish the app (but for now testing mode is fine)

## Troubleshooting
If you still get errors:
1. Double-check the Client ID in both files
2. Make sure JavaScript origins include http://localhost:3000
3. Make sure your email is in the Test Users list
4. Try clearing browser cache and cookies
