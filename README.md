# cz_nic
Python version: 3.10.0


## Úloha Frontend manualní č. 1.1 – Registrační formulář
Viz [TS_001_Registration.xlsx](https://github.com/silverhound4d/cz_nic/blob/master/TS_001_Registration.xlsx)

Návrh testovacího scénáře vychází z předokladu, že i když pole "Jméno" je povinné, nejedná se o username, tedy unikátní hodnotu a může existovat více uživatelů se stejným jménem. V opačném případě by bylo potřeba napsat další testy a ověřit, zdali uživatel se stejným jménem již neexistuje.

Dokument uvedený výše neobsahuje žádné "Non-functional" testy.

### 1.2 Navrhněte odhad času na manuální otestování dialogu podle Vámi navrženého scénáře

TC_UserReg_001-012 = 2,5min/TC\
TC_UserReg_013-015 = 3min/TC\
Buffer = 10%\
Vzorec = (12 * 2,5 + 3 * 3) * 1.1\
Odhad = 43 minut


## 1.3 Představte si, že dialog dovolí registraci i bez vyplněného pole Jméno

Bohužel nerozumím přesně zadání. Jelikož se jedná o povinné pole, k takové situaci by dojít nemělo a uživatel by měl být upozorněn odpovídajícím upozorněním. Pokud by pole nebylo povinné a uživatel žádné nezadá, Jméno by mohlo být generováno automaticky...

## Úloha Dokumentace č. 1 – Uživatelská dokumentace
### Napište v češtině a angličtině uživatelský návod pro scénář "V systému 'VYHLEDÁVÁNÍ V REGISTRU (WHOIS)' na stránkách nic.cz stáhnout 'Ověřený výpis z registru' držitele domény 'tablexia.cz'"

#### CZ
1. Spusťte prohlížeč
2. Navštivte následující webovou adresu: https://www.nic.cz/whois/
3. Klikněte na vyhledávací pole uprostřed stránky s popiskem "Doména (bez www.) / identifikátor"
4. Do vyhledávacího pole zadejte "talbexia.cz"
5. Klikněte na tlačítko Hledat pod vyhledávacím polem
6. Klikněte na odkaz "Ověřený výpis z registru" ve spodní části stránky

#### EN
1. Launch your browser.
2. Go to the following URL: https://www.nic.cz/
3. On the navigation panel click on "Domains"
4. On the newly opened Domains sub menu, click on "WHOIS"
5. Click on the search field labeled as "Domain (without www. prefix) / Handle:"
6. Enter "tablexia.cz" into the search field
7. Hit the Search button below the search field
8. Click on the link "Verified record statement" in the lower part of the webpage

## Úloha Python č. 1.1 – Krmení geparda
### U následujícímu kódu popište, co to dělá. Je v kódu nějaká chyba?

Kód umožňuje vytvořit "Gepard" objekt, na který posléze můžeme použít 3 metody, přičemž každý nový gepard má právě 9 životů (což je zároveň maximální počet možných životů).

- je_zivy - Pokud má gepard nějaké životy, return True. Pokud gepard životy nemá, return False.
- uber_zivot - Pokud má gepard více než 0 životů (je naživu), metoda ubere gepardovy jeden život.
- snez - Metoda gepardovy život přidá, pokud není mrtvý nebo na maximálním počtu životů (9). Gepard si může životy obnovit pouze jezením ryb. Žádné jiné jídlo gepardovy životy nepřidá.

#### Chyby
- Chybí "self" v metodě "je_zivy"
- Nepřehledný formát kódu, bez místa mezi jednotlivými funkcemi
- I když metoda snez funguje, dle mého názoru by bylo čitelnější zbavit se prázného return statementu v 1. if bloku, a 2. if statement nahradit elif, viz níže:

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

### 1.2 Navrhněte metodu "napapej_se", která postupně po jedné rybě nakrmí geparda, až už se do něj další ryba nevejde.
Viz [gepard.py](https://github.com/silverhound4d/cz_nic/blob/master/gepard.py), případně níže.
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
Mimo jiné, v zadání jsou 2 funkce:
- send_sms
- process_message

V mnou vypracovaném řešení jsou názvy těchto dvou funkcí prohozeny, přijde mi to logičtější. Funkce send_sms se doopravdy stará o odeslání SMS zprávy, zatímco funkce "process_message" spojuje dohromady ostatní fuknce, které zajišťují verifikaci vstupů.

Viz [cz_nic/odeslat_sms/](https://github.com/silverhound4d/cz_nic/tree/master/odeslat_sms)

#### Kód je spustitelný skrz soubor main_process_message.py v kmenovém adresáři
```bash
python main_process_message.py <path to csv file>
```

### 2.2 Napište testovací třídu s využitím testovacího frameworku (unittest, nosetests, pytest), která pokryje metodu send_sms automatickými testy

Viz [odeslat_sms/tests](https://github.com/silverhound4d/cz_nic/tree/master/odeslat_sms/tests)

#### Příklad spuštění
```bash
python -m pytest odeslat_sms/tests
```

## Úloha Frontend automatický č. 1.1 – Selenium Webdriver
### Popište, co dělá následující kód

Viz komentáře v souboru [fronetend_uloha.py](https://github.com/silverhound4d/cz_nic/blob/master/frontend_uloha.py)

### 1.2 Jaké metody selenium nabízí pro lokalizaci elementů

Viz dokumentace: https://selenium-python.readthedocs.io/locating-elements.html

Kdykoliv to jde, používat "id" lokátor. Pokud nelze, relative xpath/css selectors. Případně jakýkoliv z jiných způsobů uvedených v dokumentaci (link_text, partial_link_text, class_name...).

### 1.3 Dokážete popsat rozdíl mezi Google Chrome a ChromeDriver?
- Google Chrome - Prohlížeč, interpretuje HTML kód.
- ChromeDriver - Software, který nám umožňuje automatizovat ovládání prohlížeče skrz nejrůznější bindings/API calls.


## Úloha Frontend automatický č. 2 – Selenium Webdriver
Viz [mojeid_registration](https://github.com/silverhound4d/cz_nic/tree/master/mojeid_registration)

#### Příklad spuštění
```bash
python -m pytest mojeid_registration/tests
```

## Úloha SQL č. 1 – object_registry
Bohužel mám momentálně omezenou zkušenost s NoSQL databázemi (MongoDB), ale SQL bohužel neovládám, velice rád se samozřejmě naučím.
