from datetime import date
from typing import List, Dict, Any
from functools import reduce

def calculate_age(birth_date: str) -> int:
    year, month, day = birth_date.split('-')
    today = date.today()
    age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
    return age

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    adults = [user for user in users if calculate_age(user['birth_date']) >= 18]
    return adults

def generate_username(first_name: str, last_name: str) -> str:
    username = f"{first_name[0].lower()}.{last_name.lower()}"
    return username

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    full_names = list(map(lambda user: f"{user['first_name']} {user['last_name']}", users))
    return full_names

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    emails1 = set(map(lambda user: user['email'], users1))
    emails2 = set(map(lambda user: user['email'], users2))
    matching_emails = emails1.intersection(emails2)
    return matching_emails

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    keys = users[0].keys()
    combined_data = dict(zip(keys, zip(*[user.values() for user in users])))
    return combined_data

users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
             {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
             {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'}]


users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'}]


print(convert_to_full_name(users_data))