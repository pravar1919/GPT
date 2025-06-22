import os
from datetime import datetime
import random
import string
from chardet.universaldetector import UniversalDetector


async def upload_file(file, file_path):
    path = os.path.join(file_path, f"{file.filename}")
    with open(path, "wb") as f:
        f.write(await file.read())
    return path

def get_random_string(value = 6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(value))

def create_new_directory(dir_name):
    os.makedirs(dir_name, exist_ok=True)

def get_today_parts():
    now = datetime.now()
    return now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")

def create_job_description_dir():
    year, month, date = get_today_parts()
    # TODO: upload this to s3
    dir_name = f"uploads/jds/{year}/{month}/{date}"
    create_new_directory(dir_name)
    return dir_name

def create_resume_dir():
    # TODO: upload this to s3
    year, month, date = get_today_parts()
    dir_name = f"uploads/resumes/{year}/{month}/{date}"
    create_new_directory(dir_name)
    return dir_name

def detect_encoding(file_path):
    detector = UniversalDetector()
    with open(file_path, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result['encoding']
