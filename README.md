# 2024-dj4-medium-clone-turki-final
Github: https://github.com/gurnitha/2024-dj4-medium-clone-turki-final


## 1. SETUP


#### 1. Memodifikasi struktur awal file proyek

        modified:   README.md


#### 2. Membuat virtual environment (venv)

        λ REM: Membuat virtual environment (venv)

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final\src(main -> origin)
        λ cd ..

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final
        λ python --version
        Python 3.12.1

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final
        λ pip --version
        pip 24.1.2 from E:\_WORKSPACE\laragon\bin\python\python-3.12\Lib\site-packages\pip (python 3.12)

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final
        λ python -m venv venv312413 --promp medium-clone

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final
        λ ls
        src/  venv312413/


#### 3. Meng-aktifkan/deaktifkan virtual environment (venv312413)

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final
        λ REM: Meng-aktifkan virtual environment (venv312413)

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final
        λ venv312413\Scripts\activate.bat

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final
        (medium-clone) λ REM: Men-deaktifkan virtual environment (venv312413)

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final
        (medium-clone) λ deactivate


#### 4. Meng-instal Django versi 4.1.3 dan memeriksa hasil instalasi

        λ venv312413\Scripts\activate.bat

        (medium-clone) λ pip install django==4.1.3
        Collecting django==4.1.3
          ...
        Successfully installed asgiref-3.8.1 django-4.1.3 sqlparse-0.5.1 tzdata-2024.1

        [notice] A new release of pip is available: 23.2.1 -> 24.1.2
        [notice] To update, run: python.exe -m pip install --upgrade pip

        (medium-clone) λ python.exe -m pip install --upgrade pip
        ...
        Successfully installed pip-24.1.2

        (medium-clone) λ pip list
        Package  Version
        -------- -------
        asgiref  3.8.1
        Django   4.1.3
        pip      24.1.2
        sqlparse 0.5.1
        tzdata   2024.1


## 2. PROYEK DAN APLIKASI


#### 1. Meng-inisiasi proyek django dengan nama config

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2. Menjalankan development server

        (medium-clone) λ ls
        config/  manage.py*  README.md

        C:\Users\ING\Desktop\medium-clone\2024-dj4-medium-clone-turki-final\src(main -> origin)
        (medium-clone) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        July 25, 2024 - 11:39:45
        Django version 4.1.3, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


#### 3. Menlihat tampilan laman default django di browser

        http://127.0.0.1:8000/