@echo off
echo Creating Python virtual environment...
python -m venv venv
echo.

echo Activating virtual environment...
call venv\Scripts\activate
echo.

echo Installing dependencies...
pip install -r requirements.txt
echo.

echo Environment setup complete!
echo To activate the environment, run: venv\Scripts\activate
