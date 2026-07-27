@echo off
:: 自动切换到当前脚本所在目录（防止路径错位）
cd /d "%~dp0"
:: 启动django
python manage.py runserver
:: 运行结束不关闭窗口，方便看报错
pause