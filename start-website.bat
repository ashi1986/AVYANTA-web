@echo off
title avyanta.ai - local clone
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 serve.py %*
    goto :eof
)

where python >nul 2>nul
if %errorlevel%==0 (
    python serve.py %*
    goto :eof
)

echo Python 3 was not found. Install it from https://python.org and run this file again.
pause
