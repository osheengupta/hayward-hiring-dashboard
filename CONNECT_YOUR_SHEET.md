# Connect Your Google Sheet - Quick Guide

Your sheet is already configured in the app!
**Sheet URL**: https://docs.google.com/spreadsheets/d/1aYIGNvU9p9PJBH7S8asro1_CMpL5kk0l/edit

## Prerequisites

Your Google Sheet needs:
1. Two worksheets (tabs) named exactly: **"Police"** and **"Fire"**
2. First row with these column headers (exact names):
   ```
   role | vacancies | job_class | total_ot_hrs | total_ot_pay | no_ot_employees | avg_salary_per_hr | ot_factor | overtime_pay_hr | work_hrs_35_weeks | pension_pct
   ```
3. Data in rows below headers

**Important**:
- `pension_pct` must be decimal format: use `0.1877` not `18.77%`
- Column names are case-sensitive

---

## Setup Steps (10 minutes)

### Step 1: Set Up Google Cloud Service Account

1. **Go to**: https://console.cloud.google.com

2. **Create a project**:
   - Click "Select a project" dropdown at top
   - Click "NEW PROJECT"
   - Project name: `Hayward-Dashboard`
   - Click "CREATE"
   - Wait 30 seconds for creation

3. **Enable Google Sheets API**:
   - In search bar at top, type: `Google Sheets API`
   - Click on "Google Sheets API"
   - Click blue "ENABLE" button
   - Wait for it to enable

4. **Enable Google Drive API**:
   - Click back arrow or search again
   - Type: `Google Drive API`
   - Click on "Google Drive API"
   - Click blue "ENABLE" button

5. **Create Service Account**:
   - Click hamburger menu (☰) at top left
   - Go to: **IAM & Admin** → **Service Accounts**
   - Click "+ CREATE SERVICE ACCOUNT" at top
   - Service account name: `hayward-dashboard`
   - Service account ID: (auto-fills)
   - Click "CREATE AND CONTINUE"
   - Skip the optional steps (click "CONTINUE" then "DONE")

6. **Create and Download Key**:
   - You'll see your service account listed
   - Click on the email address (hayward-dashboard@...)
   - Click the "KEYS" tab
   - Click "ADD KEY" → "Create new key"
   - Choose "JSON"
   - Click "CREATE"
   - **A file downloads automatically** - keep it!

7. **Copy the service account email**:
   - Still on the Keys page, look at the top
   - You'll see an email like: `hayward-dashboard@hayward-dashboard-abc123.iam.gserviceaccount.com`
   - **Copy this entire email address**

---

### Step 2: Share Your Google Sheet

1. **Open your sheet**: https://docs.google.com/spreadsheets/d/1aYIGNvU9p9PJBH7S8asro1_CMpL5kk0l/edit

2. **Click "Share" button** (top right corner, next to your profile picture)

3. **In the "Add people and groups" field**:
   - Paste the service account email you copied
   - It will look like: `hayward-dashboard@hayward-dashboard-abc123.iam.gserviceaccount.com`

4. **Set permission**:
   - Change from "Viewer" to **"Editor"**
   - Uncheck "Notify people" (the service account doesn't need notifications)
   - Click "Share" or "Send"

---

### Step 3: Install the Credentials File

1. **Find the downloaded JSON file**:
   - Look in your Downloads folder
   - It's named something like: `hayward-dashboard-1234567890.json`

2. **Rename it**:
   - Right-click → Rename
   - New name: **`google_credentials.json`** (exactly this)

3. **Move it to the app folder**:

   Open Terminal and run:
   ```bash
   mv ~/Downloads/google_credentials.json "/Users/osheen/Desktop/MSBA/3rd Term/Capstone /City of Hayward/fire-hiring-app/"
   ```

   Or manually:
   - Drag the file from Downloads
   - Drop it in the `fire-hiring-app` folder

4. **Verify it's there**:
   ```bash
   ls -la "/Users/osheen/Desktop/MSBA/3rd Term/Capstone /City of Hayward/fire-hiring-app/google_credentials.json"
   ```
   Should show the file exists.

---

### Step 4: Restart the App

The app is currently running. Let's restart it to detect the Google Sheets connection.

I'll help you restart it once you've completed Steps 1-3 above!

---

## After Setup - How to Use

Once connected:

1. **Green indicator** at the top will say: "Google Sheets: Connected" ✅

2. **Update data in Google Sheet**:
   - Edit any cell in the Police or Fire tabs
   - Changes save automatically in Google Sheets

3. **Refresh the dashboard**:
   - Click "Refresh from Google Sheets" button in the app
   - Changes appear immediately!

4. **City of Hayward can now**:
   - Update salaries, OT hours, pension percentages
   - Add or remove roles
   - Make changes anytime without touching code

---

## Troubleshooting

**"Google Sheets: Not Connected" shows:**

✓ Check the file `google_credentials.json` is in the app folder
✓ Verify you shared the sheet with the service account email
✓ Make sure permission is set to "Editor" not "Viewer"
✓ Ensure both "Police" and "Fire" tabs exist in your sheet
✓ Verify column headers match exactly (case-sensitive)

**Permission Error:**
- Go back to Google Sheet → Share
- Make sure service account email is listed with "Editor" access

**Can't find service account email:**
- Open the downloaded `google_credentials.json` in a text editor
- Look for `"client_email":` line
- Copy the email address from there

---

## Next Steps

1. Complete Steps 1-3 above
2. Let me know when done
3. I'll restart the app to connect to your sheet
4. Test the connection!

Need help with any step? Just ask!
