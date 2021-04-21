import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from application import create_app

app = create_app()
manager = Manager(app)

# Turn on debugger by default and reloader
