"""Remote host configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

host = environ.get('REMOTE_HOST')
user = environ.get('REMOTE_USERNAME')
ssh_key_filepath = environ.get('SSH_KEY')
remote_path = environ.get('REMOTE_PATH')

local_file_directory = 'data'
