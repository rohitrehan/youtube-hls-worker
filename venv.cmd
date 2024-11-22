@echo off

rm -rf .venv
py -3.13 -m venv .venv

IF %ERRORLEVEL% NEQ 0 EXIT /B

call .venv\Scripts\activate.bat

python --version

python -m pip install pip-tools
python -m pip install -r requirements.txt
