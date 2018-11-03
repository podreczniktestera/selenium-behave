# Przykład projektu Selenium - Behave [![Build Status](https://travis-ci.org/podreczniktestera/selenium-behave.svg?branch=master)](https://travis-ci.org/podreczniktestera/selenium-behave)

#### Ustawienie projektu

###### CMD \ Terminal
```bash
    git clone

    cd selenium-behave

    virtualenv venv --python=python

    venv\Scripts\activate.bat
      # lub na Linuxie
    source venv/bin/activate

    pip install -r requirements.txt
```
###### PyCharm CE
* Należy zmienić interpreter Python'a tak aby wskazywał na wirtualne środowisko
* Oraz dodać konfigurację do uruchamiania testów:
  * Script path - ścieżka do aplikacji `behave` z wirualnego środowiska
  * Parameters - ścieżka do katalogu `google_tests/tests`
