@echo off
echo Stopping Django Development Server...
REM Kill process running on port 8000
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do taskkill /PID %%a /F
echo Done.
pause
