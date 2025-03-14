# Fényképalbum Alkalmazás

Ez egy Django alapú fényképalbum alkalmazás, amely lehetővé teszi a felhasználók számára képek feltöltését, megtekintését és kezelését.

## Funkciók

- Felhasználói regisztráció és bejelentkezés
- Képek feltöltése (minimum 40 karakteres névvel)
- Képek listázása (név vagy dátum szerint rendezve)
- Képek részletes nézete
- Saját képek törlése
- Reszponzív felület Bootstrap segítségével

## Telepítés és futtatás lokálisan

1. **Klónozzuk a repositoryt**

```bash
git clone https://github.com/felhasznalonev/photoalbum.git
cd photoalbum
```

2. **Virtuális környezet létrehozása és aktiválása**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Függőségek telepítése**

```bash
pip install -r requirements.txt
```

4. **Adatbázis migrációk futtatása**

```bash
python manage.py migrate
```

5. **Admin felhasználó létrehozása**

```bash
python manage.py createsuperuser
```

6. **Alkalmazás indítása**

```bash
python manage.py runserver
```

Ezután az alkalmazás elérhető a http://127.0.0.1:8000/ címen.

## Környezeti változók

A `.env` fájl létrehozásával felülírhatjuk az alapértelmezett beállításokat:

```
SECRET_KEY=sajat-titkos-kulcs
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://user:password@localhost:5432/photoalbum
```

## PaaS telepítés

### OpenShift telepítés előkészítése

1. **Regisztráljunk az OpenShift Developer Sandbox-ra**
2. **Töltsük fel a kódot GitHub-ra**
3. **Konfiguráljuk a szükséges környezeti változókat a PaaS platformon**
4. **Hozzunk létre PostgreSQL adatbázist**
5. **Végezzük el a szükséges beállításokat**

## Projekt struktúra

- **photoalbum/** - Django projekt főkönyvtár
  - **settings.py** - Projekt beállítások
  - **urls.py** - Fő URL-ek
- **photos/** - Fényképkezelő alkalmazás
  - **models.py** - Adatbázis modellek
  - **views.py** - Nézetek
  - **urls.py** - App URL-ek
- **templates/** - HTML sablonok
- **static/** - Statikus fájlok (CSS, JS)
- **media/** - Feltöltött fájlok tárolása

## Technológiák

- Django 4.2
- Bootstrap 5
- PostgreSQL (production)
- SQLite (fejlesztés)

## Licenc

MIT