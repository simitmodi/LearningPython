# generate_university_sample_data.py

import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta


def generate_sample_data(num_rows=10000):
    """
    Generates a sample university DataFrame with 10,000 rows and 50 specific columns.
    """
    data = {}

    # 1. ID (Unique Identifier)
    data['Student_ID'] = [f"STU{str(i).zfill(5)}" for i in range(1, num_rows + 1)]

    # 2. Personal Info
    indian_first_names_male = [
        'Aarav', 'Arjun', 'Aditya', 'Advait', 'Ayaan', 'Ansh', 'Aniket', 'Anirudh', 'Aryan', 'Arnav',
        'Atharv', 'Ishaan', 'Ishan', 'Rohan', 'Kabir', 'Rahul', 'Rohit', 'Sachin', 'Vikram', 'Karan',
        'Nikhil', 'Amit', 'Raj', 'Suresh', 'Vivek', 'Anil', 'Sunil', 'Manoj', 'Ravi', 'Rakesh',
        'Ajay', 'Dhruv', 'Reyansh', 'Darsh', 'Om', 'Tejas', 'Kunal', 'Pranav', 'Manish', 'Hemant',
        'Harsh', 'Jay', 'Nirav', 'Meet', 'Parth', 'Chirag', 'Akshay', 'Mihir', 'Smit', 'Sahil',
        'Shaurya', 'Tanmay', 'Aaryan', 'Bhargav', 'Ronit', 'Gautam', 'Shubham', 'Pratik', 'Nishant', 'Vikash',
        'Aviral', 'Dinesh', 'Girish', 'Sourabh', 'Yash', 'Arvind', 'Kishore', 'Rajat', 'Irfan', 'Vishal'
    ]
    indian_first_names_female = [
        'Aadhya', 'Ananya', 'Aaradhya', 'Advika', 'Diya', 'Ira', 'Kiara', 'Kiya', 'Myra', 'Pari',
        'Priya', 'Sita', 'Geeta', 'Kavya', 'Neha', 'Pooja', 'Riya', 'Shreya', 'Tanya', 'Uma',
        'Anika', 'Aarohi', 'Anvi', 'Ahana', 'Aakriti', 'Anshika', 'Avni', 'Ayesha', 'Alisha', 'Anmol',
        'Aanya', 'Meera', 'Nisha', 'Ishita', 'Trisha', 'Mitali', 'Rupal', 'Disha', 'Mansi', 'Jiya',
        'Khushi', 'Charvi', 'Sharvi', 'Bansari', 'Hetvi', 'Krisha', 'Prisha', 'Nirali', 'Rachita', 'Drashti',
        'Sahana', 'Veda', 'Smriti', 'Shalini', 'Esha', 'Reema', 'Kiran', 'Samaira', 'Nandini', 'Saanvi',
        'Vrinda', 'Anushka', 'Tanvi', 'Purvi', 'Kritika', 'Divya', 'Sonal', 'Ritika'
    ]
    indian_last_names = [
        'Sharma', 'Verma', 'Gupta', 'Agarwal', 'Singh', 'Kumar', 'Joshi', 'Pandey', 'Shukla', 'Mehta',
        'Patel', 'Reddy', 'Nair', 'Iyer', 'Gandhi', 'Bose', 'Chatterjee', 'Das', 'Malhotra', 'Khanna',
        'Rao', 'Naik', 'Jain', 'Choudhary', 'Kapoor', 'Mishra', 'Yadav', 'Chauhan', 'Tomar', 'Solanki',
        'Shah', 'Desai', 'Trivedi', 'Bhatt', 'Vora', 'Gohil', 'Dave', 'Upadhyay', 'Saxena', 'Bansal',
        'Mittal', 'Goenka', 'Mahajan', 'Bhardwaj', 'Sinha', 'Prasad', 'Pillai', 'Menon', 'Shetty', 'Naidu',
        'Ranganathan', 'Fernandes', "D'Souza", 'Kulkarni', 'Banerjee', 'Mukherjee', 'Ganguly', 'Roy', 'Sengupta', 'Mitra',
        'Dutta', 'Nath', 'Chakraborty', 'Sood', 'Arora', 'Bhat', 'Bhattacharya', 'Chopra', 'Bedi', 'Ahuja',
        'Kohli', 'Grover', 'Lal', 'Singhal', 'Suri', 'Nathani', 'Rathi', 'Bajaj', 'Pradhan', 'Rai',
        'Khan', 'Ansari', 'Khanolkar', 'Saxena', 'Rawal', 'Panchal', 'Parikh', 'Modi', 'Pandya', 'Vaghela'
    ]

    # Generate full names
    full_names = []
    genders_for_generation = []
    for _ in range(num_rows):
        gender = random.choice(['Male', 'Female'])
        genders_for_generation.append(gender)
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
    data['Age'] = np.random.randint(17, 26, size=num_rows)  # Ages 17 to 25 (typical university age)
    # Calculate birth year from age
    current_year = datetime.now().year
    data['Birth_Year'] = current_year - data['Age']
    # Assign city based on a common list for Indian universities
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Pune', 'Jaipur',
              'Lucknow',
              'Indore', 'Patna', 'Vadodara', 'Nagpur', 'Kanpur', 'Gurgaon', 'Noida', 'Thane', 'Bhopal', 'Surat']
    data['City'] = [random.choice(cities) for _ in range(num_rows)]
    # Assign state based on city (simplified mapping)
    city_to_state = {
        'Mumbai': 'Maharashtra', 'Pune': 'Maharashtra', 'Nagpur': 'Maharashtra', 'Thane': 'Maharashtra',
        'Delhi': 'Delhi',
        'Bangalore': 'Karnataka', 'Mysore': 'Karnataka',
        'Hyderabad': 'Telangana',
        'Ahmedabad': 'Gujarat', 'Vadodara': 'Gujarat', 'Surat': 'Gujarat',
        'Chennai': 'Tamil Nadu',
        'Kolkata': 'West Bengal',
        'Jaipur': 'Rajasthan', 'Bhopal': 'Madhya Pradesh',
        'Lucknow': 'Uttar Pradesh', 'Kanpur': 'Uttar Pradesh',
        'Indore': 'Madhya Pradesh', 'Patna': 'Bihar', 'Gurgaon': 'Haryana', 'Noida': 'Uttar Pradesh'
    }
    data['State'] = [city_to_state.get(city, 'Other') for city in data['City']]

    # 4. Academic Details
    courses = ['B.Tech CSE', 'B.Tech ECE', 'B.Tech ME', 'B.Tech CE', 'BBA', 'BCA', 'B.Sc Physics', 'B.Sc Chemistry',
               'B.A. Economics', 'B.A. English']
    data['Course'] = [random.choice(courses) for _ in range(num_rows)]

    # Map course to potential specializations or departments
    course_to_dept = {
        'B.Tech CSE': 'Computer Science', 'B.Tech ECE': 'Electronics', 'B.Tech ME': 'Mechanical',
        'B.Tech CE': 'Civil', 'BBA': 'Business', 'BCA': 'Computer Applications',
        'B.Sc Physics': 'Physics', 'B.Sc Chemistry': 'Chemistry',
        'B.A. Economics': 'Economics', 'B.A. English': 'English'
    }
    data['Department'] = [course_to_dept[course] for course in data['Course']]

    # Academic Year: Assuming 4-year courses, years 1-4
    data['Academic_Year'] = [random.randint(1, 4) for _ in range(num_rows)]

    # Semester based on Academic Year (1-2 per year)
    data['Semester'] = [random.randint(1, 2) + 2 * (data['Academic_Year'][i] - 1) for i in range(num_rows)]

    # Enrollment Date: Random dates between 2020 and 2024
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    data['Enrollment_Date'] = [
        (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%Y-%m-%d')
        for _ in range(num_rows)
    ]

    # CGPA: Random float between 5.0 and 10.0
    data['CGPA'] = np.round(np.random.uniform(5.0, 10.0, size=num_rows), 2)

    # Credits Earned: Based on year and semester, average 20-25 per semester
    credits_per_sem = 22  # Average
    data['Credits_Earned'] = [(year - 1) * 2 * credits_per_sem + sem * credits_per_sem for year, sem in
                              zip(data['Academic_Year'], data['Semester'])]
    # Add some random variation
    data['Credits_Earned'] = [int(credits + random.randint(-5, 5)) for credits in data['Credits_Earned']]

    # 5. Performance & Activities
    # Attendance Percentage: Random float between 60 and 100
    data['Attendance_Percentage'] = np.round(np.random.uniform(60, 100, size=num_rows), 2)

    # Number of projects completed
    data['Projects_Completed'] = [random.randint(0, 10) for _ in range(num_rows)]

    # Number of extracurricular activities
    data['Extracurricular_Count'] = [random.randint(0, 5) for _ in range(num_rows)]

    # Scholarship Status
    data['Has_Scholarship'] = [random.choice([True, False]) for _ in range(num_rows)]

    # Library Books Borrowed
    data['Books_Borrowed_Last_Month'] = [random.randint(0, 8) for _ in range(num_rows)]

    # Lab Hours Per Week
    data['Lab_Hours_Per_Week'] = [random.randint(0, 20) for _ in range(num_rows)]

    # 6. Financial & Contact
    # Annual Fees: Based on course, with some variation
    course_fees = {
        'B.Tech CSE': 250000, 'B.Tech ECE': 240000, 'B.Tech ME': 220000, 'B.Tech CE': 210000,
        'BBA': 180000, 'BCA': 160000, 'B.Sc Physics': 140000, 'B.Sc Chemistry': 140000,
        'B.A. Economics': 130000, 'B.A. English': 120000
    }
    base_fees = [course_fees[course] for course in data['Course']]
    data['Annual_Fees'] = [int(fee * random.uniform(0.95, 1.05)) for fee in base_fees]  # Add 5% variation

    # Amount Paid: Some might have pending fees
    data['Fees_Paid'] = [int(fee * random.uniform(0.8, 1.0)) for fee in data['Annual_Fees']]

    # Phone Number (Simulated)
    data['Phone_Number'] = [''.join(random.choices(string.digits, k=10)) for _ in range(num_rows)]

    # Email (Simulated)
    data['Email'] = [f"{name.split()[0].lower()}.{name.split()[1].lower()}{i}@university.edu.in" for i, name in
                     enumerate(data['Full_Name'], start=1)]

    # 7. Additional Student Fields
    # Hostel Status
    data['Lives_In_Hostel'] = [random.choice([True, False]) for _ in range(num_rows)]

    # Hostel Room Number (if applicable)
    data['Hostel_Room_Number'] = [f"{random.choice(['A', 'B', 'C', 'D'])}{random.randint(100, 499)}" if status else None
                                  for status in data['Lives_In_Hostel']]

    # Transport Mode
    transport_modes = ['Bus', 'Metro', 'Car', 'Bike', 'Walk', 'Auto']
    data['Transport_Mode'] = [random.choice(transport_modes) for _ in range(num_rows)]

    # Distance From University (km)
    data['Distance_From_University_km'] = np.round(np.random.uniform(1, 50, size=num_rows), 2)

    # Parent/Guardian Name
    data['Parent_Guardian_Name'] = [
        f"Mr. {name.split()[1]}" if data['Gender'][i] == 'Male' else f"Mrs. {name.split()[1]}" for i, name in
        enumerate(data['Full_Name'])]

    # Parent/Guardian Occupation
    occupations = ['Engineer', 'Doctor', 'Teacher', 'Business', 'Farmer', 'Government Employee', 'Self-Employed',
                   'Retired']
    data['Parent_Guardian_Occupation'] = [random.choice(occupations) for _ in range(num_rows)]

    # Parent/Guardian Phone
    data['Parent_Guardian_Phone'] = [''.join(random.choices(string.digits, k=10)) for _ in range(num_rows)]

    # Blood Group
    data['Blood_Group'] = [random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']) for _ in range(num_rows)]

    # Medical Conditions (Yes/No)
    data['Has_Medical_Conditions'] = [random.choice([True, False]) for _ in range(num_rows)]

    # Sports Participation
    data['Participates_In_Sports'] = [random.choice([True, False]) for _ in range(num_rows)]

    # Technical Club Membership
    data['Technical_Club_Member'] = [random.choice([True, False]) for _ in range(num_rows)]

    # Cultural Club Membership
    data['Cultural_Club_Member'] = [random.choice([True, False]) for _ in range(num_rows)]

    # Internship Status
    data['Has_Internship'] = [random.choice([True, False]) for _ in range(num_rows)]

    # Expected Graduation Date (based on enrollment and course duration)
    enrollment_dates_as_datetime = pd.to_datetime(data['Enrollment_Date'])
    # Assuming 4-year course, add 4 years
    expected_graduation = enrollment_dates_as_datetime + pd.DateOffset(years=4)
    data['Expected_Graduation_Date'] = expected_graduation.strftime('%Y-%m-%d')

    # Status (Active, Graduated, Suspended, Transferred)
    status_weights = [0.85, 0.10, 0.03, 0.02]  # Active, Graduated, Suspended, Transferred
    data['Student_Status'] = random.choices(['Active', 'Graduated', 'Suspended', 'Transferred'], weights=status_weights,
                                            k=num_rows)

    # Advisor/Supervisor Name
    advisor_names = [f"Prof. {last}" for last in
                     random.choices(indian_last_names, k=20)]  # Generate 20 potential advisors
    data['Advisor_Name'] = [random.choice(advisor_names) for _ in range(num_rows)]

    # Major GPA (for specific major courses, if applicable)
    data['Major_GPA'] = np.round(np.random.uniform(5.0, 10.0, size=num_rows), 2)

    # Minor GPA (if applicable)
    data['Minor_GPA'] = np.round(np.random.uniform(5.0, 10.0, size=num_rows), 2)

    # SAT/Entrance Score (Simulated, if relevant)
    data['Entrance_Score'] = [random.randint(800, 1600) for _ in range(num_rows)]

    # Research Interest (if applicable)
    research_areas = ['AI', 'ML', 'Data Science', 'Robotics', 'Renewable Energy', 'Biotechnology', 'Finance',
                      'Literature']
    data['Research_Interest'] = [random.choice(research_areas) for _ in range(num_rows)]

    # Thesis Topic (if applicable)
    thesis_topics = ['Topic A', 'Topic B', 'Topic C', 'Topic D', 'Topic E', 'Topic F', 'Topic G', 'Topic H', 'Topic I',
                     'Topic J']
    data['Thesis_Topic'] = [random.choice(thesis_topics) for _ in range(num_rows)]

    # Laptop/PC Ownership
    data['Has_Laptop_PC'] = [random.choice([True, False]) for _ in range(num_rows)]

    # Internet Speed (Mbps)
    data['Internet_Speed_Mbps'] = [random.randint(10, 1000) for _ in range(num_rows)]

    # Sibling Count
    data['Number_of_Siblings'] = [random.randint(0, 4) for _ in range(num_rows)]

    # Family Income (Annual, in INR)
    data['Family_Annual_Income_INR'] = [random.randint(200000, 2000000) for _ in range(num_rows)]

    # Languages Spoken
    languages = ['Hindi', 'English', 'Tamil', 'Telugu', 'Marathi', 'Bengali', 'Gujarati', 'Punjabi', 'Malayalam',
                 'Kannada']
    data['Languages_Spoken'] = [', '.join(random.sample(languages, random.randint(1, 3))) for _ in range(num_rows)]

    # Last Login Date (to simulate activity)
    data['Last_Login_Date'] = [
        (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%Y-%m-%d')
        for _ in range(num_rows)
    ]

    # Notes
    sample_notes = [
        "Excellent academic performance.",
        "Needs improvement in attendance.",
        "Active in extracurriculars.",
        "Consistent performer.",
        "Outstanding project work.",
        "",
        "Reliable student.",
        "Good problem solver.",
        "Potential for research.",
        "Requires academic support."
    ]
    data['Notes'] = [random.choice(sample_notes) for _ in range(num_rows)]

    df = pd.DataFrame(data)

    # Introduce some random NaN values for demonstration (as per syllabus requirement for data cleaning)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for col in numeric_cols:
        # Randomly select indices to set as NaN (about 1-2% of the data)
        nan_indices = random.sample(range(num_rows), int(random.uniform(0.01, 0.02) * num_rows))
        df.loc[nan_indices, col] = np.nan

    # Introduce some random NaN values in categorical/text columns
    text_cols = df.select_dtypes(include=['object']).columns.tolist()
    # Avoid setting critical keys like Student_ID to NaN, focus on descriptive fields
    text_feature_cols = [col for col in text_cols if col not in ['Student_ID', 'Full_Name', 'Email', 'Phone_Number']]
    for col in text_feature_cols:
        nan_indices = random.sample(range(num_rows), int(random.uniform(0.005, 0.015) * num_rows))
        df.loc[nan_indices, col] = np.nan

    return df


if __name__ == "__main__":
    print("Generating sample university data with 10,000 rows and 50 columns...")
    df = generate_sample_data(10000)

    filename = "Student.csv"
    df.to_csv(filename, index=False)
    print(f"Sample university data saved to '{filename}'. Shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head().to_string())
    print("\nColumn Names:")
    print(df.columns.tolist())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())