from datetime import datetime, timedelta
import re
import time
import pytz

# 1. Age Calculator
def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    if age_days < 0:
        age_months -= 1
        age_days += (today.replace(year=today.year - 1) - birthdate).days

    if age_months < 0:
        age_years -= 1
        age_months += 12

    print(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")

# 2. Days Until Next Birthday
def days_until_birthday(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    current_year_birthday = birthdate.replace(year=today.year)

    if today > current_year_birthday:
        current_year_birthday = current_year_birthday.replace(year=today.year + 1)

    days_left = (current_year_birthday - today).days
    print(f"Days until your next birthday: {days_left} days.")

# 3. Meeting Scheduler
def schedule_meeting(current_time, duration):
    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
    duration = timedelta(hours=int(duration.split(":")[0]), minutes=int(duration.split(":")[1]))
    end_time = current_time + duration
    print(f"The meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")

# 4. Timezone Converter
def convert_timezone(date_time_str, from_tz, to_tz):
    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    
    local_time = from_timezone.localize(date_time)
    converted_time = local_time.astimezone(to_timezone)
    print(f"Converted time: {converted_time.strftime('%Y-%m-%d %H:%M')}")

# 5. Countdown Timer
def countdown_timer(target_date_str):
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d %H:%M")
    while True:
        remaining_time = target_date - datetime.now()
        if remaining_time.total_seconds() <= 0:
            print("Time's up!")
            break
        print(f"Time remaining: {remaining_time}")
        time.sleep(1)

# 6. Email Validator
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

# 7. Phone Number Formatter
def format_phone_number(phone_number):
    pattern = r'(\d{3})(\d{3})(\d{4})'
    formatted_number = re.sub(pattern, r'(\1) \2-\3', phone_number)
    print(f"Formatted phone number: {formatted_number}")

# 8. Password Strength Checker
def check_password_strength(password):
    if len(password) < 8:
        print("Password is too short. It should be at least 8 characters long.")
    elif not re.search(r'[A-Z]', password):
        print("Password should contain at least one uppercase letter.")
    elif not re.search(r'[a-z]', password):
        print("Password should contain at least one lowercase letter.")
    elif not re.search(r'[0-9]', password):
        print("Password should contain at least one digit.")
    else:
        print("Password is strong.")

# 9. Word Finder
def find_word(text, word):
    pattern = r'\b' + re.escape(word) + r'\b'
    occurrences = re.findall(pattern, text)
    print(f"The word '{word}' occurred {len(occurrences)} times.")

# 10. Date Extractor
def extract_dates(text):
    pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    dates = re.findall(pattern, text)
    if dates:
        print("Extracted dates: ")
        for date in dates:
            print(date)
    else:
        print("No dates found.")
