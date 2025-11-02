# Deployment Guide

This guide will help you deploy the City of Hayward Police and Fire Hiring Scenarios Dashboard to Render (a free hosting platform).

## Prerequisites

1. A GitHub account (free)
2. A Render account (free) - sign up at https://render.com
3. Your Google Service Account credentials JSON file

## Step 1: Push to GitHub

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name it: `hayward-hiring-dashboard`
   - Make it Public or Private (your choice)
   - Do NOT initialize with README (we already have one)
   - Click "Create repository"

2. Push your local code to GitHub:
   ```bash
   cd "/Users/osheen/Desktop/MSBA/3rd Term/Capstone /City of Hayward/fire-hiring-app"
   git remote add origin https://github.com/YOUR_USERNAME/hayward-hiring-dashboard.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy to Render

1. Go to https://render.com and sign up/login

2. Click "New +" and select "Web Service"

3. Connect your GitHub repository:
   - Click "Connect account" to connect GitHub
   - Find and select your `hayward-hiring-dashboard` repository

4. Configure the web service:
   - **Name**: `hayward-hiring-dashboard` (or any name you prefer)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

5. Add Environment Variables:
   Click "Advanced" and add these environment variables:

   - **GOOGLE_CREDENTIALS_JSON**:
     - Open your `google_credentials.json` file
     - Copy the entire JSON content
     - Paste it as the value (it should be the entire JSON object)

   - **GOOGLE_SHEET_ID**: `1AQ_4tBGLDyMaMjQOyLlWEreE5Ux46_MvU7oMINA52-I`

6. Click "Create Web Service"

7. Wait for deployment (usually takes 2-3 minutes)

## Step 3: Access Your Deployed App

Once deployment is complete, Render will provide you with a URL like:
```
https://hayward-hiring-dashboard.onrender.com
```

Your app is now live and accessible to anyone with the link!

## Important Notes

### Free Tier Limitations
- The app may spin down after 15 minutes of inactivity
- First load after inactivity may take 30-60 seconds
- This is normal for free tier

### Updating the App
To update the deployed app after making changes:
```bash
git add .
git commit -m "Description of changes"
git push origin main
```
Render will automatically redeploy.

### Updating Google Sheets Data
- The app pulls data from Google Sheets in real-time
- City of Hayward can update the Google Sheet directly
- Changes will reflect immediately (click "Refresh from Google Sheets" button)

## Troubleshooting

### If deployment fails:
1. Check the Render logs for error messages
2. Verify that all environment variables are set correctly
3. Ensure the Google Credentials JSON is valid

### If Google Sheets connection fails:
1. Verify the Service Account email has access to the sheet
2. Check that the GOOGLE_SHEET_ID is correct
3. Ensure the sheet has "Police" and "Fire" worksheets with correct column names

## Alternative: Deploy to Heroku

If you prefer Heroku instead of Render:

1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Login: `heroku login`
3. Create app: `heroku create hayward-hiring-dashboard`
4. Set environment variables:
   ```bash
   heroku config:set GOOGLE_CREDENTIALS_JSON="$(cat google_credentials.json)"
   heroku config:set GOOGLE_SHEET_ID="1AQ_4tBGLDyMaMjQOyLlWEreE5Ux46_MvU7oMINA52-I"
   ```
5. Deploy: `git push heroku main`

## Support

For issues or questions, contact the development team or refer to:
- Render documentation: https://render.com/docs
- Flask documentation: https://flask.palletsprojects.com/
