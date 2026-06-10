### Turnajovy Management System

Jednoducha webova aplikace v Django pro spravu fotbalovych klubu, soupisek hracu a ligovych zápasu.

## Instalace

### Klonovani repozitare
```bash
git clone [https://github.com/Sacinskyy/Django-aplikace.git](https://github.com/Sacinskyy/Django-aplikace.git)

python -m venv venv

.venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations turnaj
python manage.py migrate

python manage.py napln_data

python manage.py runserver

Pristupove udaje do administrace
  Superuzivatel: admin
  Heslo: admin
