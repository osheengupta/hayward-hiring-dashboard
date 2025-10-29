# Quick Start Guide

## Running the App (3 Easy Steps)

**New Features**:
- Both Police and Fire departments supported!
- Optional Google Sheets integration for easy data updates

### Step 1: Open Terminal
Navigate to the app directory:
```bash
cd "/Users/osheen/Desktop/MSBA/3rd Term/Capstone /City of Hayward/fire-hiring-app"
```

### Step 2: Run the App
```bash
./run.sh
```

Or manually:
```bash
python3 app.py
```

### Step 3: Open Browser
Go to: **http://127.0.0.1:5000**

---

## Using the App

### Main Features

1. **Department Selector**: Switch between Police and Fire departments
   - Click the buttons at the top to view different departments
   - Each department has its own roles, salaries, and OT data

2. **Sliders**: Adjust hiring vs. overtime percentages
   - New Hiring %: How much OT to replace with new hires (0-100%)
   - Overtime %: How much remaining OT budget to use (0-100%)

3. **Preset Buttons**: Click for quick scenario analysis
   - Scenario 1: 100% New Hiring (No OT)
   - Scenario 2: 75% New Hiring / 25% OT
   - Scenario 3: 50/50 Split
   - Scenario 4: 25% New Hiring / 75% OT
   - Scenario 5: 100% OT (No New Hiring)

3. **Results Dashboard**:
   - Summary cards showing key financial metrics
   - Bar chart comparing costs by role
   - Detailed table with breakdowns

### Understanding the Results

**Green (Positive) = Savings**
**Red (Negative) = Additional Cost**

Key Metrics:
- **Original OT Cost**: Current overtime spending
- **New Hire Cost**: Cost of hiring full-time employees (with pension)
- **Salary Savings**: Money saved from reduced OT
- **Extra OT Cost**: Remaining overtime costs
- **Net Savings**: Final financial impact

---

## Sharing the App

### On Local Network
1. Find your computer's IP address:
   ```bash
   ipconfig getifaddr en0  # Mac
   ```

2. Run with network access:
   ```bash
   python3 -c "from app import app; app.run(host='0.0.0.0', port=5000)"
   ```

3. Share URL: `http://YOUR-IP:5000` (e.g., `http://192.168.1.100:5000`)

### Deploy Online
See README.md for deployment options to:
- Heroku (Free tier available)
- Render (Free tier available)
- PythonAnywhere (Free tier available)
- Google Cloud Run

---

## Troubleshooting

**Port already in use?**
```bash
lsof -ti:5000 | xargs kill -9  # Kill process on port 5000
```

**Dependencies not installed?**
```bash
pip3 install -r requirements.txt
```

**Can't find Python?**
Make sure Python 3 is installed:
```bash
python3 --version
```

---

## Support

For questions, contact the project team or refer to the full README.md
