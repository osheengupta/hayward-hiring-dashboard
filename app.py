from flask import Flask, render_template, jsonify, request
import os
import json

# Try to import Google Sheets libraries (optional)
try:
    import gspread
    from google.oauth2.service_account import Credentials
    GSHEETS_AVAILABLE = True
except ImportError:
    GSHEETS_AVAILABLE = False

app = Flask(__name__)

# Default data - Police Department
POLICE_ROLES = [
    {
        'role': 'POLICE OFFICER',
        'vacancies': 30,
        'job_class': 'P200',
        'total_ot_hrs': 30770.75,
        'total_ot_pay': 2971659.17,
        'no_ot_employees': 122,
        'avg_salary_per_hr': 69.744,
        'ot_factor': 1.5,
        'overtime_pay_hr': 96.574,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.1877
    },
    {
        'role': 'POLICE SERGEANT',
        'vacancies': 2,
        'job_class': 'P210',
        'total_ot_hrs': 4249,
        'total_ot_pay': 526622.73,
        'no_ot_employees': 25,
        'avg_salary_per_hr': 90.57,
        'ot_factor': 1.5,
        'overtime_pay_hr': 123.940,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.1875
    },
    {
        'role': 'COMMUNICATIONS OPERATOR',
        'vacancies': 9,
        'job_class': 'C635',
        'total_ot_hrs': 4933.5,
        'total_ot_pay': 338117.48,
        'no_ot_employees': 21,
        'avg_salary_per_hr': 54.894,
        'ot_factor': 1.5,
        'overtime_pay_hr': 68.535,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.0562
    },
    {
        'role': 'COMMUNITY SERVICE OFFICER',
        'vacancies': 2,
        'job_class': 'C650',
        'total_ot_hrs': 4827.25,
        'total_ot_pay': 296691.43,
        'no_ot_employees': 21,
        'avg_salary_per_hr': 45.518,
        'ot_factor': 1.5,
        'overtime_pay_hr': 61.462,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.0571
    },
    {
        'role': 'POLICE LIEUTENANT',
        'vacancies': 1,
        'job_class': 'P215',
        'total_ot_hrs': 1530.8,
        'total_ot_pay': 197537.81,
        'no_ot_employees': 10,
        'avg_salary_per_hr': 104.3,
        'ot_factor': 1.5,
        'overtime_pay_hr': 129.042,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.1918
    },
    {
        'role': 'COMMUNICATIONS SUPERVISOR',
        'vacancies': 2,
        'job_class': 'C645',
        'total_ot_hrs': 2073.75,
        'total_ot_pay': 186329.18,
        'no_ot_employees': 5,
        'avg_salary_per_hr': 63.23,
        'ot_factor': 1.5,
        'overtime_pay_hr': 89.851,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.0571
    },
    {
        'role': 'CALL TAKER',
        'vacancies': 0,
        'job_class': 'C633',
        'total_ot_hrs': 2410.5,
        'total_ot_pay': 136266.21,
        'no_ot_employees': 9,
        'avg_salary_per_hr': 45.624,
        'ot_factor': 1.5,
        'overtime_pay_hr': 56.530,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.0562
    },
    {
        'role': 'JAIL SUPERVISOR',
        'vacancies': 0,
        'job_class': 'C660',
        'total_ot_hrs': 1363.25,
        'total_ot_pay': 110770.19,
        'no_ot_employees': 3,
        'avg_salary_per_hr': 52.064,
        'ot_factor': 1.5,
        'overtime_pay_hr': 81.254,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.0596
    },
    {
        'role': 'POLICE RECORDS CLERK II',
        'vacancies': 0,
        'job_class': 'C695',
        'total_ot_hrs': 2032.75,
        'total_ot_pay': 96268.8,
        'no_ot_employees': 15,
        'avg_salary_per_hr': 39.410,
        'ot_factor': 1.5,
        'overtime_pay_hr': 47.359,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.0566
    }
]

# Default data - Fire Department
FIRE_ROLES = [
    {
        'role': 'APPARATUS OPRTR-56HR',
        'vacancies': 2,
        'job_class': 'F210',
        'total_ot_hrs': 29446.5,
        'total_ot_pay': 2102404.99,
        'no_ot_employees': 43,
        'avg_salary_per_hr': 55.518,
        'ot_factor': 1.5,
        'overtime_pay_hr': 71.397,
        'work_hrs_35_weeks': 1960,
        'pension_pct': 0.1625
    },
    {
        'role': 'FIRE CAPTAIN (56 HR)',
        'vacancies': 0,
        'job_class': 'F245',
        'total_ot_hrs': 20660.25,
        'total_ot_pay': 1919697.26,
        'no_ot_employees': 41,
        'avg_salary_per_hr': 65.81,
        'ot_factor': 1.5,
        'overtime_pay_hr': 92.917,
        'work_hrs_35_weeks': 1960,
        'pension_pct': 0.171
    },
    {
        'role': 'FIREFIGHTER (56 HR)',
        'vacancies': 0,
        'job_class': 'F200',
        'total_ot_hrs': 21963.25,
        'total_ot_pay': 1399009.35,
        'no_ot_employees': 69,
        'avg_salary_per_hr': 52.328,
        'ot_factor': 1.5,
        'overtime_pay_hr': 63.698,
        'work_hrs_35_weeks': 1960,
        'pension_pct': 0.1549
    },
    {
        'role': 'BATTALION CHIEF (56 HR)',
        'vacancies': 0,
        'job_class': 'F410',
        'total_ot_hrs': 4720.5,
        'total_ot_pay': 546427.04,
        'no_ot_employees': 6,
        'avg_salary_per_hr': 79.082,
        'ot_factor': 1.5,
        'overtime_pay_hr': 115.756,
        'work_hrs_35_weeks': 1960,
        'pension_pct': 0.1756
    },
    {
        'role': 'STAFF FIRE CAPT-40HR',
        'vacancies': 1,
        'job_class': 'F240',
        'total_ot_hrs': 842.5,
        'total_ot_pay': 115656.55,
        'no_ot_employees': 5,
        'avg_salary_per_hr': 101.37,
        'ot_factor': 1.5,
        'overtime_pay_hr': 137.278,
        'work_hrs_35_weeks': 1400,
        'pension_pct': 0.1723
    }
]

def load_from_google_sheets():
    """Load data from Google Sheets if configured"""
    if not GSHEETS_AVAILABLE:
        return None, None

    try:
        # Define the scope
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']

        # Load credentials - try environment variable first, then file
        google_creds_json = os.getenv('GOOGLE_CREDENTIALS_JSON')

        if google_creds_json:
            # Load from environment variable (for deployment)
            creds_dict = json.loads(google_creds_json)
            creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
        else:
            # Load from file (for local development)
            creds_file = os.path.join(os.path.dirname(__file__), 'google_credentials.json')
            if not os.path.exists(creds_file):
                return None, None
            creds = Credentials.from_service_account_file(creds_file, scopes=scope)

        client = gspread.authorize(creds)

        # Get the spreadsheet by ID or name
        sheet_id = os.getenv('GOOGLE_SHEET_ID', '1AQ_4tBGLDyMaMjQOyLlWEreE5Ux46_MvU7oMINA52-I')
        sheet_name = os.getenv('GOOGLE_SHEET_NAME', '')

        # Try to open by ID first (more reliable), then by name
        if sheet_id:
            spreadsheet = client.open_by_key(sheet_id)
        else:
            spreadsheet = client.open(sheet_name)

        # Load Police data from 'Police' worksheet
        police_sheet = spreadsheet.worksheet('Police')
        police_data_raw = police_sheet.get_all_records()

        # Load Fire data from 'Fire' worksheet
        fire_sheet = spreadsheet.worksheet('Fire')
        fire_data_raw = fire_sheet.get_all_records()

        # Convert string values to numbers
        def convert_types(data):
            converted = []
            for row in data:
                converted_row = {}
                for key, value in row.items():
                    if key in ['role', 'job_class']:
                        converted_row[key] = str(value)
                    else:
                        try:
                            # Try to convert to float
                            converted_row[key] = float(value) if value != '' else 0
                        except (ValueError, TypeError):
                            converted_row[key] = value
                converted.append(converted_row)
            return converted

        police_data = convert_types(police_data_raw)
        fire_data = convert_types(fire_data_raw)

        return police_data, fire_data
    except Exception as e:
        print(f"Error loading from Google Sheets: {e}")
        return None, None

def get_department_data(department):
    """Get data for a specific department, trying Google Sheets first"""
    police_data, fire_data = load_from_google_sheets()

    if department.lower() == 'police':
        return police_data if police_data else POLICE_ROLES
    elif department.lower() == 'fire':
        return fire_data if fire_data else FIRE_ROLES
    else:
        return []

def calculate_scenario(roles, new_hire_pct, ot_pct):
    """
    Calculate costs for a hiring scenario
    new_hire_pct: percentage of OT to replace with new hires (0-100)
    ot_pct: percentage of OT to keep (0-100)
    """
    results = []
    total_ot_pay = 0
    total_new_hire_cost = 0
    total_new_hire_with_pension = 0
    total_salary_saving = 0
    total_extra_ot_cost = 0
    total_net_savings = 0

    for role in roles:
        # Calculate OT hours to be replaced by new hires based on scenario percentage
        ot_hrs_to_replace = role['total_ot_hrs'] * (new_hire_pct / 100)

        # Calculate employees needed = OT hours to replace / work hours per employee
        employees_needed_decimal = ot_hrs_to_replace / role['work_hrs_35_weeks']

        # Round for display purposes
        employees_needed_rounded = round(employees_needed_decimal)

        # Cost of hiring new employees = decimal employees * avg_salary_per_hr * work_hrs_35_weeks
        # NOTE: Use decimal value for calculations, not rounded value
        cost_ft_employees = employees_needed_decimal * role['avg_salary_per_hr'] * role['work_hrs_35_weeks']

        # Total pension cost = pension_pct * Cost of hiring new employees
        pension_cost = cost_ft_employees * role['pension_pct']

        # Total cost with pension = Cost of hiring new employees + total pension cost
        cost_with_pension = cost_ft_employees + pension_cost

        # Extra OT cost = Scenario based % of Total OT pay
        extra_ot_cost = role['total_ot_pay'] * (ot_pct / 100)

        # Savings = total_ot_pay - Total Cost with pension
        salary_saving = role['total_ot_pay'] - cost_with_pension

        # Net Savings = Savings - Extra OT cost
        net_savings = salary_saving - extra_ot_cost

        # Calculate OT hours remaining based on scenario
        ot_hrs_remaining = role['total_ot_hrs'] * (ot_pct / 100)

        # OT hours and pay per employee
        if role['no_ot_employees'] > 0:
            ot_hrs_per_employee = ot_hrs_remaining / role['no_ot_employees']
            ot_pay_per_employee = extra_ot_cost / role['no_ot_employees']
        else:
            ot_hrs_per_employee = 0
            ot_pay_per_employee = 0

        total_ot_pay += role['total_ot_pay']
        total_new_hire_cost += cost_ft_employees
        total_new_hire_with_pension += cost_with_pension
        total_salary_saving += salary_saving
        total_extra_ot_cost += extra_ot_cost
        total_net_savings += net_savings

        results.append({
            'role': role['role'],
            'vacancies': int(role.get('vacancies', 0)),
            'employees_needed': employees_needed_rounded,
            'cost_ft_employees': round(cost_ft_employees, 2),
            'cost_with_pension': round(cost_with_pension, 2),
            'salary_saving': round(salary_saving, 2),
            'extra_ot_cost': round(extra_ot_cost, 2),
            'net_savings': round(net_savings, 2),
            'ot_hrs_per_employee': round(ot_hrs_per_employee, 2),
            'ot_pay_per_employee': round(ot_pay_per_employee, 2),
            'original_ot_pay': round(role['total_ot_pay'], 2)
        })

    return {
        'roles': results,
        'totals': {
            'total_original_ot': round(total_ot_pay, 2),
            'total_new_hire_cost': round(total_new_hire_cost, 2),
            'total_new_hire_with_pension': round(total_new_hire_with_pension, 2),
            'total_salary_saving': round(total_salary_saving, 2),
            'total_extra_ot_cost': round(total_extra_ot_cost, 2),
            'total_net_savings': round(total_net_savings, 2)
        }
    }

@app.route('/')
def index():
    return render_template('index.html', gsheets_enabled=GSHEETS_AVAILABLE)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    new_hire_pct = float(data.get('new_hire_pct', 0))
    ot_pct = float(data.get('ot_pct', 0))
    department = data.get('department', 'fire')

    if department == 'both':
        # Combine both departments
        police_roles = get_department_data('police')
        fire_roles = get_department_data('fire')
        roles = police_roles + fire_roles
    else:
        roles = get_department_data(department)

    results = calculate_scenario(roles, new_hire_pct, ot_pct)
    return jsonify(results)

@app.route('/api/departments')
def departments():
    """Return list of available departments"""
    return jsonify({
        'departments': ['police', 'fire'],
        'gsheets_enabled': GSHEETS_AVAILABLE
    })

@app.route('/api/refresh-data', methods=['POST'])
def refresh_data():
    """Force refresh data from Google Sheets"""
    police_data, fire_data = load_from_google_sheets()
    if police_data is not None or fire_data is not None:
        return jsonify({'status': 'success', 'message': 'Data refreshed from Google Sheets'})
    else:
        return jsonify({'status': 'error', 'message': 'Could not load data from Google Sheets'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
