# Google Sheets Connection Setup

## Your Google Sheet
URL: https://docs.google.com/spreadsheets/d/1aYIGNvU9p9PJBH7S8asro1_CMpL5kk0l/edit

## Quick Setup Steps

### Part 1: Set Up Google Cloud (5 minutes)

1. **Go to Google Cloud Console**: https://console.cloud.google.com

2. **Create a new project**:
   - Click "Select a project" → "New Project"
   - Project name: `Hayward-Hiring-Dashboard`
   - Click "Create"
   - Wait for project creation (about 30 seconds)

3. **Enable APIs**:
   - In the search bar at top, type "Google Sheets API"
   - Click on "Google Sheets API"
   - Click "Enable" button
   - Go back and search for "Google Drive API"
   - Click on "Google Drive API"
   - Click "Enable" button

4. **Create Service Account**:
   - Go to menu (☰) → "IAM & Admin" → "Service Accounts"
   - Click "Create Service Account"
   - Service account name: `hayward-dashboard`
   - Click "Create and Continue"
   - Skip permissions (click "Continue")
   - Click "Done"

5. **Create Key (Download JSON)**:
   - Click on the service account you just created (hayward-dashboard@...)
   - Click "Keys" tab
   - Click "Add Key" → "Create new key"
   - Select "JSON"
   - Click "Create"
   - A file will download (keep it safe!)

6. **Copy the service account email**:
   - You'll see an email like: `hayward-dashboard@hayward-hiring-dashboard.iam.gserviceaccount.com`
   - Copy this email address

### Part 2: Share Your Google Sheet

1. **Open your Google Sheet**:
   https://docs.google.com/spreadsheets/d/1aYIGNvU9p9PJBH7S8asro1_CMpL5kk0l/edit

2. **Click the "Share" button** (top right corner)

3. **Paste the service account email** you copied above

4. **Set permission to "Editor"**

5. **Uncheck "Notify people"**

6. **Click "Share"**

### Part 3: Install Credentials

1. **Locate the downloaded JSON file**:
   - It's in your Downloads folder
   - Name is something like: `hayward-hiring-dashboard-abc123.json`

2. **Rename it**:
   - Rename to: `google_credentials.json`

3. **Move it to the app folder**:
   ```bash
   mv ~/Downloads/google_credentials.json "/Users/osheen/Desktop/MSBA/3rd Term/Capstone /City of Hayward/fire-hiring-app/"
   ```

### Part 4: Configure Sheet Name

The app needs to know your sheet's exact name. Run this command:

```bash
cd "/Users/osheen/Desktop/MSBA/3rd Term/Capstone /City of Hayward/fire-hiring-app"
```

Then we need to update the app to use your sheet ID instead of name.

### Part 5: Test Connection

After completing the above:

1. **Restart the app** (I'll help with this)
2. **Open browser** to http://127.0.0.1:5000
3. **Check the indicator** at the top - should say "Google Sheets: Connected" in green
4. **Click "Refresh from Google Sheets"** button to test

---

## Troubleshooting

If "Google Sheets: Not Connected" appears:

1. Check `google_credentials.json` is in the app folder
2. Verify you shared the sheet with the service account email
3. Make sure both "Police" and "Fire" worksheets exist
4. Check column headers match exactly

---

## Your Sheet Structure

Make sure your sheet has these two tabs:

### Tab 1: "Police"
Columns: role, vacancies, job_class, total_ot_hrs, total_ot_pay, no_ot_employees, avg_salary_per_hr, ot_factor, overtime_pay_hr, work_hrs_35_weeks, pension_pct

### Tab 2: "Fire"
Columns: (same as above)

**Note**: Column names are case-sensitive and must match exactly!
