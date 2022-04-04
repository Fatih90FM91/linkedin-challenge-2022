#!c:\users\hunterman\desktop\linkedin_challenge_django\venv\scripts\python.exe
# When the django-admin.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admin.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admin instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admin.py is deprecated in favor of django-admin.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()
    


#     import re
# import sys

# from gunicorn.app.wsgiapp import run


# if __name__ == '__main__':
#         sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$','',sys.argv[0])
#         sys.exit(run())