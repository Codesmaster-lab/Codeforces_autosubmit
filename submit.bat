@ECHO OFF
set arg1=%1
set arg2=%2
cmd /k "cd /d E: & cd /d E:\Submit\venv\Scripts & activate & cd /d    E:\Submit & python submit.py  %1  %2 & cd /d E: & cd /d E:\Submit\venv\Scripts & deactivate &  cd /d E:\Submit"
