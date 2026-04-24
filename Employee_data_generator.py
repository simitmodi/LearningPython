# generate_corporate_sample_data.py

import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta


def generate_sample_data(num_rows=10000):
    """
    Generates a sample corporate DataFrame with 10,000 rows and 50 specific columns.
    """
    data = {}

    # 1. ID (Unique Identifier)
    data['Employee_ID'] = [f"EMP{str(i).zfill(5)}" for i in range(1, num_rows + 1)]

    # 2. Personal Info
    indian_first_names_male = [
        'Aarav', 'Arjun', 'Kabir', 'Krishna', 'Rahul', 'Rohit', 'Sachin', 'Vikram', 'Karan', 'Nikhil',
        'Amit', 'Raj', 'Suresh', 'Vivek', 'Anil', 'Sunil', 'Manoj', 'Ravi', 'Rakesh', 'Ajay'
    ]
    indian_first_names_female = [
        'Aadhya', 'Ananya', 'Aaradhya', 'Advika', 'Diya', 'Ira', 'Kiara', 'Kiya', 'Myra', 'Pari',
        'Priya', 'Sita', 'Geeta', 'Kavya', 'Neha', 'Pooja', 'Riya', 'Shreya', 'Tanya', 'Uma'
    ]
    indian_last_names = [
        'Sharma', 'Verma', 'Gupta', 'Agarwal', 'Singh', 'Kumar', 'Joshi', 'Pandey', 'Shukla', 'Mehta',
        'Patel', 'Reddy', 'Nair', 'Iyer', 'Gandhi', 'Bose', 'Chatterjee', 'Das', 'Malhotra', 'Khanna'
    ]

    # Generate full names
    full_names = []
    for _ in range(num_rows):
        gender = random.choice(['Male', 'Female'])
        if gender == 'Male':
            first_name = random.choice(indian_first_names_male)
        else:
            first_name = random.choice(indian_first_names_female)
        last_name = random.choice(indian_last_names)
        full_names.append(f"{first_name} {last_name}")
    data['Full_Name'] = full_names
    # Correct gender assignment based on the actual first name generated
    data['Gender'] = ['Male' if name.split()[0] in indian_first_names_male else 'Female' for name in data['Full_Name']]

    # 3. Demographics
    data['Age'] = np.random.randint(22, 66, size=num_rows)  # Ages 22 to 65
    # Calculate birth year from age
    current_year = datetime.now().year
    data['Birth_Year'] = current_year - data['Age']
    # Assign city based on a common list for Indian corporates
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Pune', 'Jaipur',
              'Lucknow']
    data['City'] = [random.choice(cities) for _ in range(num_rows)]
    # Assign state based on city (simplified mapping)
    city_to_state = {
        'Mumbai': 'Maharashtra', 'Pune': 'Maharashtra',
        'Delhi': 'Delhi',
        'Bangalore': 'Karnataka', 'Hyderabad': 'Telangana',
        'Ahmedabad': 'Gujarat', 'Jaipur': 'Rajasthan',
        'Chennai': 'Tamil Nadu', 'Kolkata': 'West Bengal', 'Lucknow': 'Uttar Pradesh'
    }
    data['State'] = [city_to_state[city] for city in data['City']]

    # 4. Employment Details
    departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance', 'IT', 'Operations', 'Legal', 'R&D', 'Support']
    data['Department'] = [random.choice(departments) for _ in range(num_rows)]

    roles_engineering = ['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Principal Engineer',
                         'Engineering Manager']
    roles_sales = ['Sales Executive', 'Sales Manager', 'Regional Sales Manager', 'Sales Director', 'VP Sales']
    roles_other = ['Analyst', 'Senior Analyst', 'Manager', 'Senior Manager', 'Director', 'VP', 'Head']

    role_mapping = {
        'Engineering': roles_engineering,
        'Sales': roles_sales,
        'Marketing': roles_other,
        'HR': roles_other,
        'Finance': roles_other,
        'IT': roles_other,
        'Operations': roles_other,
        'Legal': roles_other,
        'R&D': roles_other,
        'Support': roles_other
    }
    data['Job_Role'] = [random.choice(role_mapping[dept]) for dept in data['Department']]

    levels = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7']
    data['Job_Level'] = [random.choice(levels) for _ in range(num_rows)]

    # Hire Date: Random dates between 2010 and 2024
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2024, 12, 31)
    data['Hire_Date'] = [
        (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%Y-%m-%d')
        for _ in range(num_rows)
    ]
    # Calculate Years of Experience based on hire date
    data['Years_Experience_At_Hire'] = [random.randint(0, 15) for _ in range(num_rows)]
    # Calculate current years of experience
    hire_dates_as_datetime = pd.to_datetime(data['Hire_Date'])
    today = pd.Timestamp.now()
    # --- ALTERNATIVE CORRECTED LINE: Use .days attribute directly ---
    time_diff = (today - hire_dates_as_datetime)
    data['Current_Years_Experience'] = (time_diff.days / 365.25).astype(int) + data['Years_Experience_At_Hire']

    employment_types = ['Full-time', 'Part-time', 'Contract', 'Intern']
    data['Employment_Type'] = [random.choice(employment_types) for _ in range(num_rows)]

    reporting_managers = [f"Manager_{i}" for i in range(1, 51)]  # Generate 50 potential managers
    data['Reporting_Manager'] = [random.choice(reporting_managers) for _ in range(num_rows)]

    # 5. Compensation & Benefits
    # Base salary depends on department, level, and experience
    base_salary_map = {'L1': 400000, 'L2': 600000, 'L3': 900000, 'L4': 1300000, 'L5': 1800000, 'L6': 2500000,
                       'L7': 3500000}
    data['Base_Salary'] = []
    for level, exp in zip(data['Job_Level'], data['Current_Years_Experience']):
        base = base_salary_map.get(level, 400000)
        # Add variation based on experience and department
        dept_multiplier = {'Engineering': 1.2, 'Sales': 1.1, 'R&D': 1.15}.get(
            data['Department'][len(data['Base_Salary'])], 1.0)
        exp_bonus = exp * 10000
        salary = base * dept_multiplier + exp_bonus
        # Add some random noise
        salary = int(salary * random.uniform(0.9, 1.1))
        data['Base_Salary'].append(salary)

    data['Bonus_Percentage'] = [random.uniform(0, 0.3) for _ in range(num_rows)]  # 0% to 30%
    data['Bonus_Amount'] = (np.array(data['Base_Salary']) * np.array(data['Bonus_Percentage'])).astype(int)
    data['Total_Compensation'] = np.array(data['Base_Salary']) + np.array(data['Bonus_Amount'])

    # 6. Performance & Skills
    data['Performance_Score'] = np.round(np.random.normal(loc=7.5, scale=1.5, size=num_rows),
                                         2)  # Mean ~7.5, scale ~1.5
    # Ensure scores are within a plausible range (e.g., 1-10)
    data['Performance_Score'] = np.clip(data['Performance_Score'], 1.0, 10.0)

    data['Last_Performance_Review_Date'] = [
        (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%Y-%m-%d')
        for _ in range(num_rows)
    ]

    tech_skills_pool = ['Python', 'Java', 'JavaScript', 'SQL', 'React', 'Node.js', 'AWS', 'Docker', 'Kubernetes',
                        'Machine Learning']
    data['Technical_Skills'] = [', '.join(random.sample(tech_skills_pool, random.randint(1, 4))) for _ in
                                range(num_rows)]

    # 7. Work & Engagement
    data['Satisfaction_Rating'] = np.random.randint(1, 11, size=num_rows)  # 1-10 scale
    data['Engagement_Score'] = np.round(np.random.normal(loc=7.0, scale=1.8, size=num_rows), 2)  # Mean ~7.0, scale ~1.8
    data['Engagement_Score'] = np.clip(data['Engagement_Score'], 1.0, 10.0)

    work_modes = ['On-site', 'Hybrid', 'Remote']
    data['Work_Mode'] = [random.choice(work_modes) for _ in range(num_rows)]

    data['Overtime_Hours_Last_Month'] = np.random.poisson(lam=8, size=num_rows)  # Avg 8 hours overtime

    # 8. Additional Corporate Fields
    education_levels = ['Bachelor', 'Master', 'PhD', 'Diploma']
    data['Education_Level'] = [random.choice(education_levels) for _ in range(num_rows)]

    data['Marital_Status'] = [random.choice(['Single', 'Married', 'Divorced']) for _ in range(num_rows)]

    data['Number_of_Dependents'] = np.random.poisson(lam=1.5, size=num_rows)  # Avg 1.5 dependents

    data['Has_Company_Car'] = [random.choice([True, False]) for _ in range(num_rows)]

    data['Has_Health_Insurance'] = [True for _ in range(num_rows)]  # Assume yes for corporates

    data['Training_Hours_Last_Year'] = np.random.poisson(lam=20, size=num_rows)  # Avg 20 hours

    project_counts = [0, 1, 2, 3, 4, 5]
    data['Number_of_Projects_Last_Year'] = [random.choice(project_counts) for _ in range(num_rows)]

    data['Leaves_Taken_Last_Year'] = np.random.poisson(lam=5, size=num_rows)  # Avg 5 days

    # 9. Status & Notes
    # Bias 'Active' heavily
    status_weights = [0.85, 0.05, 0.05, 0.05]  # Active, On Leave, Resigned, Terminated
    data['Employee_Status'] = random.choices(['Active', 'On Leave', 'Resigned', 'Terminated'], weights=status_weights,
                                             k=num_rows)

    sample_notes = [
        "High performer, recommended for promotion.",
        "Needs improvement in project delivery.",
        "Excellent team collaboration skills.",
        "Met all KPIs for the quarter.",
        "Outstanding innovation award winner.",
        "",
        "Reliable and punctual employee.",
        "Strong technical problem solver.",
        "Potential leadership candidate.",
        "Requires mentoring for soft skills."
    ]
    data['Notes'] = [random.choice(sample_notes) for _ in range(num_rows)]

    # --- Generate remaining columns to reach 50 ---
    # Example: Additional metrics, IDs, flags
    data['Employee_Category'] = [random.choice(['Regular', 'Probation', 'Contractor']) for _ in range(num_rows)]
    data['Shift_Type'] = [random.choice(['Day', 'Night', 'Rotational']) for _ in range(num_rows)]
    data['Has_Stock_Options'] = [random.choice([True, False]) for _ in range(num_rows)]
    data['Access_Level'] = [random.choice(['Basic', 'Standard', 'Advanced', 'Admin']) for _ in range(num_rows)]
    data['Last_Login_Date'] = [
        (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%Y-%m-%d')
        for _ in range(num_rows)
    ]
    # --- ALTERNATIVE CORRECTED LINE: Apply same method for Years_At_Company ---
    time_diff_company = (pd.Timestamp.now() - pd.to_datetime(data['Hire_Date']))
    data['Years_At_Company'] = (time_diff_company.days / 365.25).astype(int)
    data['Absence_Rate_Percent'] = np.round(np.random.uniform(0, 10, size=num_rows), 2)
    data['Client_Feedback_Score'] = np.round(np.random.normal(loc=4.0, scale=0.8, size=num_rows), 2)
    data['Client_Feedback_Score'] = np.clip(data['Client_Feedback_Score'], 1.0, 5.0)
    data['Internal_Training_Completed'] = [random.randint(0, 10) for _ in range(num_rows)]
    data['Certifications_Count'] = [random.randint(0, 5) for _ in range(num_rows)]
    data['Preferred_Language'] = [random.choice(['English', 'Hindi', 'English/Hindi']) for _ in range(num_rows)]
    data['Emergency_Contact_Relationship'] = [random.choice(['Spouse', 'Parent', 'Sibling', 'Friend']) for _ in
                                              range(num_rows)]
    data['Blood_Group'] = [random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']) for _ in range(num_rows)]
    data['Has_Dental_Insurance'] = [random.choice([True, False]) for _ in range(num_rows)]
    data['Has_Life_Insurance'] = [random.choice([True, False]) for _ in range(num_rows)]
    data['Commute_Method'] = [random.choice(['Car', 'Public Transport', 'Bike', 'Walk']) for _ in range(num_rows)]
    data['Distance_From_Office_km'] = np.round(np.random.uniform(1, 50, size=num_rows), 2)
    data['Team_Size_Under_Management'] = [random.randint(0, 15) for _ in range(num_rows)]  # 0 if not a manager
    for i, role in enumerate(data['Job_Role']):
        if 'Manager' not in role and 'Director' not in role and 'VP' not in role and 'Head' not in role:
            data['Team_Size_Under_Management'][i] = 0  # Non-managers manage 0
    data['Innovation_Ideas_Submitted'] = [random.randint(0, 12) for _ in range(num_rows)]  # Per year
    data['Patents_Held'] = [random.randint(0, 3) for _ in range(num_rows)]
    data['Mentorship_Hours_Provided'] = np.random.poisson(lam=5, size=num_rows)  # Avg 5 hours
    data['Volunteer_Hours_Last_Year'] = np.random.poisson(lam=10, size=num_rows)  # Avg 10 hours
    data['Expense_Claims_Last_Month'] = np.random.poisson(lam=2, size=num_rows)  # Avg 2 claims
    data['Average_Weekly_Hours_Worked'] = np.round(np.random.normal(loc=45, scale=5, size=num_rows), 2)
    data['Average_Weekly_Hours_Worked'] = np.clip(data['Average_Weekly_Hours_Worked'], 30.0, 70.0)
    data['Has_Mentor'] = [random.choice([True, False]) for _ in range(num_rows)]
    data['Career_Goal_Achievement_Percent'] = np.round(np.random.uniform(0, 100, size=num_rows), 2)
    data['Last_Salary_Hike_Percent'] = np.round(np.random.uniform(5, 25, size=num_rows), 2)
    data['Previous_Company_Tenure_Years'] = [random.randint(0, 10) for _ in range(num_rows)]
    data['Referral_Source'] = [random.choice(['Employee Referral', 'Job Portal', 'Campus', 'Consultant', 'Direct']) for
                               _ in range(num_rows)]
    data['Background_Check_Status'] = [random.choice(['Cleared', 'Pending', 'Failed']) for _ in range(num_rows)]
    data['Background_Check_Status'] = ['Cleared' if x == 'Cleared' else random.choice(['Pending', 'Cleared']) for x in
                                       data['Background_Check_Status']]  # Bias cleared
    data['Onboarding_Completion_Status'] = [random.choice(['Completed', 'In Progress', 'Not Started']) for _ in
                                            range(num_rows)]
    data['Onboarding_Completion_Status'] = [
        'Completed' if x == 'Completed' else random.choice(['In Progress', 'Completed']) for x in
        data['Onboarding_Completion_Status']]  # Bias completed
    data['IT_Equipment_Assigned'] = [random.choice(['Laptop', 'Desktop', 'Laptop + Monitor', 'Desktop + Monitor']) for _
                                     in range(num_rows)]
    data['IT_Equipment_Value_USD'] = [random.randint(500, 2500) for _ in range(num_rows)]
    data['Assigned_Parking_Slot'] = [random.choice(['Yes', 'No', 'Waitlist']) for _ in range(num_rows)]
    data['Assigned_Parking_Slot'] = ['Yes' if x == 'Yes' else random.choice(['No', 'Yes']) for x in
                                     data['Assigned_Parking_Slot']]  # Bias yes
    data['Cafeteria_Subscription'] = [random.choice([True, False]) for _ in range(num_rows)]
    data['Gym_Membership'] = [random.choice([True, False]) for _ in range(num_rows)]
    data['Company_Store_Discount_Level'] = [random.choice(['Standard', 'Premium', 'VIP']) for _ in range(num_rows)]
    data['Assigned_Office_Location'] = [f"Floor_{random.randint(1, 20)}-{random.choice(['A', 'B', 'C'])}" for _ in
                                        range(num_rows)]

    df = pd.DataFrame(data)

    # Introduce some random NaN values for demonstration (as per syllabus requirement for data cleaning)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for col in numeric_cols:
        # Randomly select indices to set as NaN (about 1-2% of the data)
        nan_indices = random.sample(range(num_rows), int(random.uniform(0.01, 0.02) * num_rows))
        df.loc[nan_indices, col] = np.nan

    # Introduce some random NaN values in categorical/text columns
    text_cols = df.select_dtypes(include=['object']).columns.tolist()
    # Avoid setting critical keys like Employee_ID to NaN, focus on descriptive fields
    text_feature_cols = [col for col in text_cols if col not in ['Employee_ID', 'Full_Name']]
    for col in text_feature_cols:
        nan_indices = random.sample(range(num_rows), int(random.uniform(0.005, 0.015) * num_rows))
        df.loc[nan_indices, col] = np.nan

    return df


if __name__ == "__main__":
    print("Generating sample corporate data with 10,000 rows and 50 columns...")
    df = generate_sample_data(10000)

    filename = "Employee.csv"
    df.to_csv(filename, index=False)
    print(f"Sample corporate data saved to '{filename}'. Shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head().to_string())
    print("\nColumn Names:")
    print(df.columns.tolist())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())
