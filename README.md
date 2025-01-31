Documentazione:
    https://docs.djangoproject.com/en/5.1/

Architettura:
    Architettura MVC (Model View Controller)
    M: definisce quali dati contiene l'app
    V: descrive come mostrare i dati
    C: contiene la logica che aggiorna i modelli e/o le view in risposta all'input utente

    Django utilizza MTV (Model Template View) che è sostanzialmente un MVC
    M: "data access layer" definisce la struttura delle entità nel sito, tradotte poi in tabelle nel db
    T: "presentation layer" descrive come i dati vanno mostrati
    V: "business logic layer" gestisce req/res HTTP. Dispone della logica per sapere a quali dati accedere, tramite models, e delegare la formattazione ai templates

Installazione venv django:
'''
    PS E:\dev\django> powershell -ep bypass
    Windows PowerShell
    Copyright (C) Microsoft Corporation. Tutti i diritti riservati.

    Prova la nuova PowerShell multipiattaforma https://aka.ms/pscore6

    PS E:\dev\django> .\django_env\Scripts\Activate.ps1
    (django_env) PS E:\dev\django> pip install django
'''
Creazione progetto:
'''
    (django_env) PS E:\dev\django> django-admin startproject lab 
    (django_env) PS E:\dev\django> ls

        Directory: E:\dev\django

    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----        31/01/2025     14:30                django_env
    d-----        31/01/2025     14:33                lab
    -a----        31/01/2025     14:24            661 note.txt
'''
    manage.py:
        script da cui vengono lanciati comandi di tipo amministrativo come
'''
        (django_env) PS E:\dev\django\lab> python .\manage.py runserver
'''
File di progetto:
    init.py:
        file vuoto che informa django di trattare la cartella in cui risiede come package

    Creazione di una app:
        '''
        PS E:\dev\django\lab> python .\manage.py startapp test_app
        '''
        apps.py:
            configurazioni specifiche per l'applicazione
        models.py:
            contiene le classi dei modelli della applicazione

        Quando creo una app è necessario inserirla dentro il file settings.py di progetto:
            INSTALLED_APPS = [
                ...
                'django.contrib.staticfiles',

                'test_app'
            ]

        Tipicamente non vengono aggiunti gli url delle varie app direttamente nel file urls.py di progetto,
        ma viene creato un file urls.py per ogni app e successivamente importato il modulo nel file urls.py di progetto.
        