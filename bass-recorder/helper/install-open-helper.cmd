@echo off
rem Registers the bassrec-open: link so Bass Recorder can open folders. Current user only, no admin needed.
set "D=%LOCALAPPDATA%\BassRecorder"
if not exist "%D%" mkdir "%D%"
copy /Y "%~dp0bassrec-open.ps1" "%D%\bassrec-open.ps1" >nul || (echo bassrec-open.ps1 mora biti v isti mapi kot ta datoteka. & pause & exit /b 1)
reg add "HKCU\Software\Classes\bassrec-open" /ve /d "URL:Bass Recorder open folder" /f >nul
reg add "HKCU\Software\Classes\bassrec-open" /v "URL Protocol" /d "" /f >nul
reg add "HKCU\Software\Classes\bassrec-open\shell\open\command" /ve /d "powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File \"%D%\bassrec-open.ps1\" \"%%1\"" /f >nul
echo Namesceno v %D%
pause
