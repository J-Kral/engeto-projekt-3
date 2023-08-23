# engeto-projekt-3
Můj Python projekt 3

"Elections Scraper"


    Popis projektu

Tento skript slouží k extrahování dat z webových stránek ČSU: "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ" (Volby do Poslanecké sněmovny Parlamentu České republiky konané ve dnech 20.10. – 21.10.2017).


    Instalace knihoven

Knihovny, které jsou použité v tomto skriptu jsou uložene v souboru requirements.txt . Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:

$ pip3 --version                    # overim verzi manazeru
$ pip3 install -r requirements.txt  # nainstalujeme knihovny


    Spuštění projektu

Spuštění souboru projekt_3.py v rámci přik. řádku požaduje dva povinné argumenty.

python projekt_3.py <odkaz-uzemniho-celku> <vysledny-soubor>

Následně se stáhnou data ze zadaného odkazu jako soubor s příponou .csv.


    Ukázka projektu

Výsledky hlasování pro okres Blansko:
1. argument: "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201"
2. argument: "vysledky_Blansko"

Spuštění programu:

python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201" "vysledky_Blansko"

Průběh programu:

STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201
UKLADAM DO SOUBORU vysledky_Blansko.csv
ZPRACOVANO %
100%
END 

Při otevírání CSV souboru je nutné nadefinovat následující pravidla pro import textu (OpenOffice.org Calc):
    Znaková sada (kódování) - UTF-8
    Oddělovací pole – tabulátor - ";"
    Oddělovač textu – ponechte výchozí nastavení

Částečný výstup:

code;location;registered;envelopes;valid;...
581291;Adamov;3668;2157;2138;208;3;5;222;0;76;241;37;18;28;1;7;208;5;63;565;5;14;117;2;10;3;6;278;15;1
581313;Bedřichov;205;155;153;16;0;2;10;0;3;4;0;3;8;0;0;13;0;6;51;0;1;17;0;0;1;0;18;0;0
581330;Benešov;538;382;382;28;0;0;43;0;9;45;4;5;6;0;0;24;0;11;92;0;0;74;0;2;0;1;36;2;0
...