@echo OFF
title DriverFinancer Installation

REM Création de l'environnement virtuel
python -m venv venv_project

REM Activation de l'environnement virtuel
call venv_project\Scripts\activate.bat

%VIRTUAL_ENV%\scripts\python.exe -m pip install --upgrade pip

REM Installation des dépendances
pip install -r requirements.txt

REM Installation du package
python main.py

PAUSE