import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))

CHROMEDRIVER_EXE = os.environ.get('CHROMEDRIVER_EXE')
GECKODRIVER_EXE = os.environ.get('GECKODRIVER_EXE')