### Turnajovy Management System

Jednoducha webova aplikace v Django pro spravu fotbalovych klubu, soupisek hracu a ligovych zápasu.

## Instalace

### Klonovani repozitare
```bash
git clone [https://github.com/Sacinskyy/Django-aplikace.git](https://github.com/Sacinskyy/Django-aplikace.git)
```
Vytvoreni virtualniho prostredi do slozky .venv
```bash
python -m venv venv
```
Aktivace virtualniho prostredi
```bash
.venv\Scripts\activate
```
Instalace requirements.txt
```bash
pip install -r requirements.txt
```
Inicializace databaze a migrace
```bash
python manage.py makemigrations turnaj
python manage.py migrate
```
Inicializace databaze a migrace
```bash
python manage.py napln_data
```
Spusteni aplikace
```bash
python manage.py runserver
```

Pristupove udaje do administrace
  Superuzivatel: admin
  Heslo: admin
