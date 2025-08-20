@echo off
REM run_example.cmd - quick wrappers for AUD parser

set PY=D:\apps\python\64\3.11.6\python.exe

%PY% ice_status_aud.py --date today --slot 10:00 --verbose
%PY% ice_status_aud.py --date today --slot 16:00
%PY% ice_status_aud.py --date today --slot 16:15
%PY% ice_status_aud.py --date today --slot 16:30 --verbose
