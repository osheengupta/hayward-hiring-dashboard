# Google Sheets Integration Setup Guide

This guide will help you connect the app to Google Sheets so City of Hayward can update the data dynamically.

## Overview

With Google Sheets integration, City of Hayward staff can:
- Update role data, salaries, and OT costs directly in Google Sheets
- Changes automatically reflect in the dashboard
- No need to redeploy the app or modify code
- Easy data management for non-technical users

---

## Step 1: Create Google Sheets Document

1. **Go to Google Sheets**: https://sheets.google.com

2. **Create a new spreadsheet** named: `City of Hayward - Police and Fire Hiring`

3. **Create two worksheets**:
   - Sheet 1: "Police"
   - Sheet 2: "Fire"

4. **Add column headers** (same for both sheets):
   ```
   | role | vacancies | job_class | total_ot_hrs | total_ot_pay | no_ot_employees | avg_salary_per_hr | ot_factor | overtime_pay_hr | work_hrs_35_weeks | pension_pct |
   ```

5. **Enter your data** following the format:
   - Each row represents one role
   - Use decimal numbers for salaries and percentages
   - pension_pct should be decimal (e.g., 0.1877 for 18.77%)

### Example Police Sheet:
```
role                        | vacancies | job_class | total_ot_hrs | total_ot_pay | no_ot_employees | avg_salary_per_hr | ot_factor | overtime_pay_hr | work_hrs_35_weeks | pension_pct
POLICE OFFICER              | 30        | P200      | 30770.75     | 2971659.17   | 122             | 69.744            | 1.5       | 96.574          | 1400              | 0.1877
POLICE SERGEANT             | 2         | P210      | 4249         | 526622.73    | 25              | 90.57             | 1.5       | 123.940         | 1400              | 0.1875
```

---

## Step 2: Create Google Cloud Project & Enable APIs

1. **Go to Google Cloud Console**: https://console.cloud.google.com

2. **Create a new project**:
   - Click "Select a project" → "New Project"
   - Name: "City of Hayward Hiring Dashboard"
   - Click "Create"

3. **Enable Google Sheets API**:
   - Go to "APIs & Services" → "Library"
   - Search for "Google Sheets API"
   - Click on it and press "Enable"

4. **Enable Google Drive API**:
   - Search for "Google Drive API"
   - Click on it and press "Enable"

---

## Step 3: Create Service Account

1. **Go to "IAM & Admin" → "Service Accounts"**

2. **Click "Create Service Account"**:
   - Service account name: `hayward-hiring-dashboard`
   - Description: "Service account for hiring scenarios dashboard"
   - Click "Create and Continue"

3. **Grant permissions** (optional, can skip):
   - Click "Continue" → "Done"

4. **Create a key**:
   - Click on the service account you just created
   - Go to "Keys" tab
   - Click "Add Key" → "Create new key"
   - Choose "JSON" format
   - Click "Create"
   - A JSON file will download automatically

5. **Rename the downloaded file**:
   - Rename it to: `google_credentials.json`

---

## Step 4: Share Google Sheet with Service Account

1. **Copy the service account email**:
   - It looks like: `hayward-hiring-dashboard@your-project-id.iam.gserviceaccount.com`
   - Find it in the JSON file under `"client_email"`

2. **Open your Google Sheet**

3. **Click "Share" button** (top right)

4. **Add the service account email**:
   - Paste the service account email
   - Give it "Editor" permission
   - Uncheck "Notify people"
   - Click "Share"

---

## Step 5: Install the App with Google Sheets Support

1. **Place the credentials file**:
   ```bash
   # Move the downloaded google_credentials.json to your app folder
   mv ~/Downloads/google_credentials.json "/Users/osheen/Desktop/MSBA/3rd Term/Capstone /City of Hayward/fire-hiring-app/"
   ```

2. **Install Google Sheets dependencies**:
   ```bash
   cd "/Users/osheen/Desktop/MSBA/3rd Term/Capstone /City of Hayward/fire-hiring-app"
   pip3 install -r requirements.txt
   ```

3. **Update the sheet name in app** (if different):
   - Open `app.py`
   - Find line with: `sheet_name = os.getenv('GOOGLE_SHEET_NAME', 'City of Hayward - Police and Fire Hiring')`
   - Update the sheet name if you used a different name

4. **Start the app**:
   ```bash
   python3 app.py
   ```

5. **Check the indicator**:
   - Open browser to http://127.0.0.1:5000
   - Look for "Google Sheets: Connected" in green at the top
   - If it shows "Not Connected", check the troubleshooting section below

---

## Step 6: Using the App with Google Sheets

### For Dashboard Users:
1. App automatically loads data from Google Sheets on startup
2. Click "Refresh from Google Sheets" button to reload latest data
3. Switch between Police and Fire departments using the buttons

### For City of Hayward Staff (Data Updates):
1. Open the Google Sheet
2. Update any values (salaries, OT hours, pension percentages, etc.)
3. Save changes (automatically saved in Google Sheets)
4. In the dashboard, click "Refresh from Google Sheets" button
5. Changes appear immediately!

---

## Data Format Guidelines

### Required Columns:
- **role**: Role name (text)
- **vacancies**: Number of vacant positions (number)
- **job_class**: Job classification code (text)
- **total_ot_hrs**: Total overtime hours (number)
- **total_ot_pay**: Total overtime pay in dollars (number)
- **no_ot_employees**: Number of employees working OT (number)
- **avg_salary_per_hr**: Average salary per hour (number)
- **ot_factor**: Overtime multiplier, usually 1.5 (number)
- **overtime_pay_hr**: Overtime pay per hour (number)
- **work_hrs_35_weeks**: Work hours in 35 weeks period (number)
- **pension_pct**: Pension percentage as decimal (e.g., 0.1877 = 18.77%)

### Important Notes:
- Do NOT change column headers
- Use numbers only (no $ or % symbols)
- Pension percentage must be decimal (18.77% = 0.1877)
- Empty cells will be treated as 0
- Keep both "Police" and "Fire" worksheet names exact

---

## Troubleshooting

### "Google Sheets: Not Connected" appears

**Check these:**
1. Is `google_credentials.json` in the app folder?
2. Is the Google Sheet shared with the service account email?
3. Is the sheet name exactly: `City of Hayward - Police and Fire Hiring`?
4. Are both worksheets named exactly "Police" and "Fire"?
5. Run: `pip3 install gspread google-auth`

**View detailed error**:
- Check the terminal where you ran `python3 app.py`
- Look for error messages starting with "Error loading from Google Sheets"

### Permission Errors

**Problem**: "Access denied" or "Forbidden"
**Solution**:
- Make sure you shared the Google Sheet with the service account
- Give "Editor" permission (not just "Viewer")

### Wrong Data Appears

**Problem**: App shows old data after updating Google Sheet
**Solution**:
- Click "Refresh from Google Sheets" button in the app
- If that doesn't work, restart the server

### Can't Find Service Account Email

**Problem**: Don't know what email to share sheet with
**Solution**:
- Open `google_credentials.json`
- Look for `"client_email":` field
- Copy the email address there

---

## Deployment with Google Sheets

When deploying to a cloud service (Heroku, Render, etc.):

1. **Upload credentials as environment variable**:
   ```bash
   # For Heroku:
   heroku config:set GOOGLE_CREDENTIALS="$(cat google_credentials.json)"
   ```

2. **Update app.py** to read from environment variable (code already included)

3. **Set sheet name**:
   ```bash
   heroku config:set GOOGLE_SHEET_NAME="City of Hayward - Police and Fire Hiring"
   ```

---

## Security Best Practices

1. **Never commit `google_credentials.json` to Git**:
   - Already included in `.gitignore`

2. **Limit service account permissions**:
   - Only share the specific sheet, not entire Drive

3. **Use separate service accounts** for production/development

4. **Regularly rotate credentials**:
   - Create new keys every 90 days
   - Delete old keys

5. **Monitor access**:
   - Check Google Sheet's activity log for unauthorized changes

---

## Benefits of Google Sheets Integration

For City of Hayward:
- **Easy Updates**: No technical knowledge required
- **Real-time**: Changes appear immediately after refresh
- **Audit Trail**: Google Sheets tracks all changes
- **Collaboration**: Multiple people can update data
- **Backup**: Google Sheets automatically saves version history
- **Access Control**: Manage who can view/edit via Google permissions

---

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review server logs in terminal
3. Verify Google Sheet format matches examples
4. Ensure all APIs are enabled in Google Cloud Console

For additional help, contact the development team.
