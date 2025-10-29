# Google Sheets Setup Checklist

## Before You Start
- [ ] Your Google Sheet URL: https://docs.google.com/spreadsheets/d/1aYIGNvU9p9PJBH7S8asro1_CMpL5kk0l/edit
- [ ] Make sure you have tabs named "Police" and "Fire" in your sheet
- [ ] First row has the correct column headers

---

## Setup Tasks

### Part 1: Google Cloud Console
- [ ] Go to https://console.cloud.google.com
- [ ] Create new project named "Hayward-Dashboard"
- [ ] Enable "Google Sheets API"
- [ ] Enable "Google Drive API"
- [ ] Create service account named "hayward-dashboard"
- [ ] Download JSON key file (creates google_credentials.json)
- [ ] Copy the service account email address

### Part 2: Share Your Sheet
- [ ] Open your Google Sheet
- [ ] Click "Share" button
- [ ] Paste the service account email
- [ ] Set permission to "Editor"
- [ ] Uncheck "Notify people"
- [ ] Click "Share"

### Part 3: Install Credentials
- [ ] Find the downloaded JSON file in Downloads folder
- [ ] Rename it to: `google_credentials.json`
- [ ] Move it to the fire-hiring-app folder
- [ ] Verify file exists in the app folder

### Part 4: Test Connection
- [ ] Restart the app (I'll help with this)
- [ ] Check for "Google Sheets: Connected" indicator (green)
- [ ] Click "Refresh from Google Sheets" button
- [ ] Verify data loads correctly

---

## ✅ When You're Done

Let me know when you've completed Parts 1-3, and I'll:
1. Restart the app
2. Test the connection
3. Show you how to use it!

---

## 📝 Notes

**Service Account Email** (save this for reference):
- Format: `hayward-dashboard@hayward-dashboard-XXXXXX.iam.gserviceaccount.com`
- Your actual email: _______________________________________________

**Credentials File Location**:
- Must be at: `/Users/osheen/Desktop/MSBA/3rd Term/Capstone /City of Hayward/fire-hiring-app/google_credentials.json`

---

## ❓ Need Help?

- **Detailed instructions**: See `CONNECT_YOUR_SHEET.md`
- **Full guide**: See `GOOGLE_SHEETS_SETUP.md`
- **Ask me**: I'm here to help with any step!
