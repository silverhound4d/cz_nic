# cz_nic
Job application submission


## Úloha Frontend manualní č. 1.1 – Registrační formulář
viz soubor TS_001_Registration.xlsx

Návrh testovacího scénáře vychází z předokladu, že i když pole "Jméno" je povinné, nejedná se o username, tedy unikátní hodnotu a může existovat více uživatelů se stejným jménem. V opačném případě by bylo potřeba napsat další testy a ověřit, zdali uživatel se stejným jménem již neexistuje.


## Úloha Frontend manualní č. 1.2 – Registrační formulář
### Navrhněte odhad času na manuální otestování dialogu podle Vámi navrženého scénáře

TC_UserReg_001-012 = 2,5min/TC <br>
TC_UserReg_013-015 = 3min/TC <br>
Buffer = 10% <br>
Vzorec = (12 * 2,5 + 3 * 3) * 1.1 <br>
Odhad = 43 minut <br>


## Úloha Frontend manualní č. 1.3 – Registrační formulář
### Představte si, že dialog dovolí registraci i bez vyplněného pole Jméno

Bohužel nerozumím přesně zadání. Jelikož se jedná o povinné pole, k takové situaci by dojít nemělo a uživatel by měl být upozorněn odpovídajícím upozorněním. Případně by mohlo být Jméno generováno automaticky...

## Úloha Dokumentace č. 1 – Uživatelská dokumentace


## Úloha Python č. 1.1 – Krmení geparda
### U následujícímu kódu popište, co to dělá. Je v kódu nějaká chyba?

Kód umožňuje vytvořit "Gepard" objekt, na který posléze můžeme použít 3 metody, přičemž každý nový gepard má právě 9 životů (což je i zároveň maximální počet možných životů).

- je_zivy - Pokud má gepard nějaké životy, return True. Pokud gepard životy nemá, return False.
- uber_zivot - Pokud má gepard více než 0 životů (je naživu), metoda ubere gepardovy jeden život.
- snez - Metoda gepardovy život přidá, pokud není mrtvý nebo na maximálním počtu životů (9). Gepard si může životy obnovit pouze jezením ryb. Žádné jiné jídlo gepardovy životy nepřidá.

#### Chyby
- Chybí "self" v metodě "je_zivy"
- Nepřehledný formát kódu (not PEP 8 compliant)
- I když metoda snez funguje, dle mého názoru by bylo čitelnější zbavit se return statementu v 1. if bloku, a 2. if statement nahradit elif, viz níže:</ul>

```python
    def snez(self, jidlo):
        if not self.je_zivy():
            print("Je zbytecne krmit mrtve zvire!")
        elif jidlo == "ryba" and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print("Gepard spapal rybu a obnovil se mu jeden zivot.")
        else:
            print("Gepard se krmi.")
```

### 1.2 Navrhněte metodu "napapej_se", která postupně po jedné rybě nakrmí geparda, až už se do něj dalšíryba nevejde.
Viz [gepard.py](gepard.py), případně níže.
```python
    def napapej_se(self):
        if not self.je_zivy():
            print("Je zbytecne krmit mrtve zvire!")
        elif self.pocet_zivotu == 9:
            print("Gepard se přejedl.")
        else:
            while self.pocet_zivotu < 9:
                self.snez("ryba")
                print(f"Současný počet životů {self.pocet_zivotu}")
```

## Úloha Python č. 2.1 – Odeslání SMS

Viz [main_process_message.py](main_process_message.py)

#### Příklad spuštění
```bash
python main_process_message.py <path to csv file>
```

## Úloha Python č. 2.2 – Odeslání SMS
### Napište testovací třídu s využitím testovacího frameworku (unittest, nosetests, pytest), která pokryje metodu send_sms automatickými testy

Viz [odeslat_sms/tests](www.seznam.cz)

#### Příklad spuštění
```bash
python -m pytest odeslat_sms/tests
```

## Úloha Frontend automatický č. 1 – Selenium Webdriver
### 1.1 Popište, co dělá následující kód

Viz komentáře v souboru [fronetend_uloha](fronetend_uloha)

### 1.2 Jaké metody selenium nabízí pro lokalizaci elementů

Viz dokumentace: https://selenium-python.readthedocs.io/locating-elements.html

Kdykoliv to jde, používat "id" lokátor. Pokud nelze, relative xpath/css selectors. Případně jakýkoliv z jiných způsobů uvedených v dokumentaci (link_text, partial_link_text, class_name...).

### 1.3 Dokážete popsat rozdíl mezi Google Chrome a ChromeDriver?
- Google Chrome - Prohlížeč, interpretuje HTML kód.
- ChromeDriver - Software, který nám umožňuje automatizovat ovládání prohlížeče skrz nejrůznější bindings/API calls.


## Úloha Frontend automatický č. 2 – Selenium Webdriver
Viz [mojeid_registration](www.seznam.cz)

#### Příklad spuštění
```bash
python -m pytest mojeid_registration/tests
```

## Úloha SQL č. 1 – object_registry
Bohužel mám momentálně omezenou zkušenost s NoSQL databázemi (MongoDB), ale SQL bohužel neovládám, velice rád se samozřejmě naučím.
