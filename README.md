# Police & Fire Department Hiring Scenarios - City of Hayward

An interactive web application for analyzing Police and Fire Department hiring scenarios, comparing costs between overtime (OT) and new hiring strategies.

## Features

- **Dual Department Support**: Switch between Police and Fire departments with one click
- **Google Sheets Integration**: Connect to Google Sheets for easy data management by City staff
- **Interactive Controls**: Adjust new hiring and overtime percentages with intuitive sliders
- **Preset Scenarios**: Quick access to 5 predefined hiring scenarios
- **Real-time Calculations**: Instant updates showing cost impacts
- **Visual Analytics**: Charts and tables displaying cost comparisons by role
- **Key Metrics Dashboard**: Summary cards showing total costs, savings, and net impact
- **Data Refresh**: Update dashboard instantly when Google Sheets data changes

## Application Structure

```
fire-hiring-app/
├── app.py                          # Flask backend with calculation logic
├── templates/
│   └── index.html                  # Frontend interface with charts and controls
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── GOOGLE_SHEETS_SETUP.md          # Google Sheets integration guide
├── QUICK_START.md                  # Quick start instructions
├── google_credentials.json         # (Optional) Google service account credentials
├── Procfile                        # For Heroku deployment
└── .gitignore                      # Git ignore rules
```

## Installation

1. **Navigate to the project directory**:
   ```bash
   cd "fire-hiring-app"
   ```

2. **Install dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

## Running Locally

1. **Start the Flask server**:
   ```bash
   python3 app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

The app will be running in debug mode on port 5000.

## How to Use

1. **Select Department**:
   - Click "Police Department" or "Fire Department" button to switch between departments

2. **Adjust Sliders**:
   - **New Hiring Percentage**: Percentage of OT to replace with new full-time employees (0-100%)
   - **Overtime Percentage**: Percentage of remaining OT budget to utilize (0-100%)

3. **Use Preset Buttons**:
   - **Scenario 1**: 100% Hiring (No OT)
   - **Scenario 2**: 75% Hiring / 25% OT
   - **Scenario 3**: 50% Hiring / 50% OT
   - **Scenario 4**: 25% Hiring / 75% OT
   - **Scenario 5**: 100% OT (No New Hiring)

4. **Review Results**:
   - Summary cards show key financial metrics
   - Bar chart compares costs across different roles
   - Detailed table provides breakdown by role

5. **Update Data** (if Google Sheets is connected):
   - Click "Refresh from Google Sheets" to load latest data
   - City staff can update the Google Sheet and changes appear instantly

## Google Sheets Integration

The app supports optional Google Sheets integration, allowing City of Hayward staff to update role data, salaries, and OT costs without touching the code.

**Quick Setup**:
1. Follow the detailed instructions in [GOOGLE_SHEETS_SETUP.md](GOOGLE_SHEETS_SETUP.md)
2. Place `google_credentials.json` in the app folder
3. Restart the app to enable Google Sheets connection

**Benefits**:
- Non-technical staff can update data easily
- Changes reflect immediately in the dashboard
- No need to redeploy the app
- Version history and audit trail via Google Sheets

**Note**: The app works perfectly without Google Sheets - it will use the default data from your Excel file.

## Deployment Options

### Option 1: Deploy to Heroku

1. **Create a Procfile**:
   ```bash
   echo "web: gunicorn app:app" > Procfile
   ```

2. **Initialize git repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

3. **Create and deploy to Heroku**:
   ```bash
   heroku create hayward-fire-hiring-app
   git push heroku main
   heroku open
   ```

### Option 2: Deploy to Render

1. **Create account** at [render.com](https://render.com)

2. **Create a new Web Service**:
   - Connect your GitHub repository
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Set environment to Python 3

3. **Deploy** and access your app at the provided URL

### Option 3: Deploy to PythonAnywhere

1. **Create account** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload files** via the Files tab

3. **Create a new web app**:
   - Select Flask
   - Point to your app.py file
   - Set working directory

4. **Install requirements**:
   ```bash
   pip3 install --user -r requirements.txt
   ```

5. **Reload** the web app

### Option 4: Deploy to Google Cloud Run

1. **Create a Dockerfile**:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
   ```

2. **Build and deploy**:
   ```bash
   gcloud run deploy hayward-fire-app --source . --platform managed --region us-central1 --allow-unauthenticated
   ```

### Option 5: Run on Local Network

To make the app accessible on your local network:

```bash
python3 -c "from app import app; app.run(host='0.0.0.0', port=5000)"
```

Then access from any device on the network using your computer's IP address (e.g., `http://192.168.1.100:5000`)

## API Endpoints

### POST `/api/calculate`
Calculate costs for a custom scenario.

**Request Body**:
```json
{
  "new_hire_pct": 60,
  "ot_pct": 40
}
```

**Response**:
```json
{
  "roles": [...],
  "totals": {
    "total_original_ot": 6083195.19,
    "total_new_hire_cost": 2761479.35,
    "total_new_hire_with_pension": 3215349.56,
    "total_salary_saving": 3649917.11,
    "total_extra_ot_cost": 2433271.29,
    "total_net_savings": -1998703.74
  }
}
```

### GET `/api/predefined-scenarios`
Get results for all 5 predefined scenarios.

## Data Source

The application uses Fire Department data including:
- 5 different roles (Apparatus Operator, Fire Captain, Firefighter, Battalion Chief, Staff Fire Captain)
- Current overtime hours and costs
- Salary information
- Pension percentages

## Calculations

The app calculates the following for each scenario:

1. **Employees Needed**: Based on OT hours to replace
2. **Cost of FT Employees**: Salary cost for new hires
3. **Cost with Pension**: Including pension benefits
4. **Salary Saving**: Reduction in OT costs
5. **Extra OT Cost**: Remaining OT budget utilization
6. **Net Savings**: Total financial impact (positive = savings, negative = additional cost)

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Charts**: Chart.js
- **Styling**: Custom CSS with gradient designs
- **Server**: Gunicorn (production)

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Support

For questions or issues, contact the City of Hayward IT Department.

## License

City of Hayward - Internal Use
