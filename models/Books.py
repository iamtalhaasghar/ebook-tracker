from pydal import DAL, Field
import os

from dotenv import load_dotenv
if not load_dotenv():
    print('Can\'t find .env file. Exiting!')
    exit(0)
db = DAL(os.getenv('DB_STR'), migrate=True, folder=os.getenv('DB_DIR')) # connection string
db.define_table('books',
                Field('name', 'string'),
                Field('author', 'string'),
                Field('read_on', 'datetime')
                )