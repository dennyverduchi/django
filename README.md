# Documentazione
    https://docs.djangoproject.com/en/5.1/

# Architettura
    Architettura MVC (Model View Controller)
    M: definisce quali dati contiene l'app
    V: descrive come mostrare i dati
    C: contiene la logica che aggiorna i modelli e/o le view in risposta all'input utente

    Django utilizza MTV (Model Template View) che è sostanzialmente un MVC
    M: "data access layer" definisce la struttura delle entità nel sito, tradotte poi in tabelle nel db
    T: "presentation layer" descrive come i dati vanno mostrati
    V: "business logic layer" gestisce req/res HTTP. Dispone della logica per sapere a quali dati accedere, tramite models, e delegare la formattazione ai templates

# Installazione venv django
    PS E:\dev\django> .\django_env\Scripts\Activate.ps1
    (django_env) PS E:\dev\django> pip install django

# Creazione progetto
    (django_env) PS E:\dev\django> django-admin startproject lab 
    (django_env) PS E:\dev\django> ls
    
        Directory: E:\dev\django
    
    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----        31/01/2025     14:30                django_env
    d-----        31/01/2025     14:33                lab
    -a----        31/01/2025     14:24            661 note.txt

manage.py:
- script da cui vengono lanciati comandi di tipo amministrativo come

        (django_env) PS E:\dev\django\lab> python .\manage.py runserver

# File di progetto
init.py:
- file vuoto che informa django di trattare la cartella in cui risiede come package

# Creazione di una app
    PS E:\dev\django\lab> python .\manage.py startapp test_app
    
apps.py:
- configurazioni specifiche per l'applicazione
  
models.py:
- contiene le classi dei modelli della applicazione

Quando creo una app è necessario inserirla dentro il file settings.py di progetto:
            
    INSTALLED_APPS = [
        ...
        'django.contrib.staticfiles',
    
        'test_app'
    ]

Tipicamente non vengono aggiunti gli url delle varie app direttamente nel file urls.py di progetto, ma viene creato un file urls.py per ogni app e successivamente importato il modulo nel file urls.py di progetto.
        
# Migrazioni
Gestisce la corrispondenza tra quanto scrivo in models.py ed il contenuto dentro al db

    (venv) PS E:\dev\django\dl_2\django_l2> python .\manage.py makemigrations
    Migrations for 'news':
    news\migrations\0001_initial.py
        + Create model Journalist
        + Create model Article



    (venv) PS E:\dev\django\dl_2\django_l2> python .\manage.py sqlmigrate news 0001
    BEGIN;
    --
    -- Create model Journalist
    --
    CREATE TABLE "news_journalist" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(20) NOT NULL, "last_name" varchar(20) NOT NULL);
    --
    -- Create model Article
    --
    CREATE TABLE "news_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(50) NOT NULL, "content" text NOT NULL, "journalist_id" bigint NOT NULL REFERENCES "news_journalist" ("id") DEFERRABLE INITIALLY DEFERRED);
    CREATE INDEX "news_article_journalist_id_97044b2f" ON "news_article" ("journalist_id");
    COMMIT;



    (venv) PS E:\dev\django\dl_2\django_l2> python .\manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, news, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK     
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying news.0001_initial... OK
    Applying sessions.0001_initial... OK