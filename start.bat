@echo off
echo Starting Django Development Server...
REM Activate virtual environment
call win_env\Scripts\activate

REM Run server with HTTP (default)
python manage.py runserver

REM Or run with HTTPS (uncomment next line if needed)
:: python manage.py runserver_plus --cert-file cert.pem

pause
