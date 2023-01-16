
# ~~Not really an~~ auto attendance for ITB

Random shit I made.\
\
This stuff uses firefox gecko driver, so install firefox and gecko driver.\
\
Gecko driver can be downloaded [here](https://github.com/mozilla/geckodriver/releases).


## How to actually use it

Clone the project

```
  git clone https://github.com/KaonWry/Selenium-ITB-SIX-not-really-auto-attendance.git
```

Go to the project directory

```
  cd Selenium-ITB-SIX-not-really-auto-attendance
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Make auth.txt in the project root folder, put your NIM on the first line and password on the second line (I use nano here, but you can use anything similar like notepad or Vim if you're feeling masochistic)

````bash
  nano auth.txt
````

Hit the engine and let selenium do the rest

```bash
  python index.py
```

