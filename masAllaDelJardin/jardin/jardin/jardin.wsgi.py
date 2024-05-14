import os

from masAllaDelJardin.settings import *  # Reemplaza con la ruta a tu archivo settings.py
from jardin import application  # 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jardin.settings')

application = get_wsgi_application()
