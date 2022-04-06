import random
from random import choice


smalltalk=("jak jde tvoje nicotná existence?",
        "těšil ses na zprávu od tvé Paní?",
        "doufám, že na mě myslíš!",
        "pořád jseš takovej zoufalec?",
        "tak kolikrát jsi honil, co?")

uukoly=["Pošleš mi fotky tvýho minipéra.",
        "Zákaz masturbace do příštího mailu!",
        "Chci fotku něčeho velkýho v tvým zadku! Vyber si co chceš.",
        "Pošleš mi na účet 1000 Kč.",
        "Napíšeš esej o tom, proč jsi taková nula. Pět stran je minimum.",
        "Chci video jak honíš. A u toho budeš říkat moje jméno.",
        "Video, kde chodíš po čtyřech a chrochtáš.",
        "Vyholíš si nad péro moje jméno.",
        "Koupíš si tanga a budeš je nosit až do příštího mailu.",
        "Půjdeš do sprchy, zazpíváš něco od Queenů a pošleš mi video.",
        "Potřeš si péro a zadek chilli. Chci fotku nebo video.",
        "Strčíš péro do mísy s ledem. A natoč mi to.",
        "Chci následující video: batolíš se po pokoji a jako správný batole máš samozřejmě plenku a dudlík.",
        "Strčíš to svoje pérko do svěráku a budeš pořádně utahovat. Chci, aby tě to bolelo! Neznič si ho ale, ještě ho budeme potřebovat.",
        "Chci abys napsal básničku o tom, že jsi ubožák. Každý druhý verš bude znít 'jsem ubožák'. Takže to bude vypadat třeba takhle: Mám to prostě tak, jsem ubožák. Ale to ti už radím!",
        "Naučíme se pár základních psích povelů. Pro začátek mi ukážeš jak umíš sednout, lehnout a hrát mrtvýho psa. Všechno tak desetkrát.",
        "Pořídíš si psí misku a ukážeš mi na videu jak žereš konzervu. Můžeš si vybrat takovou, která ti bude nejvíc chutnat.",
        "Koupíš si kozačky a ty pro mě budeš líbat a olizovat. Představuj si, že je tvoje Paní u tebe.",
        "Omotáš si celý svoje minipérko lepící páskou. Pak mi natočíš jak to jde dolů.",
        "Tentokrát po tobě chci abys byl kreativní. Představuju si fotku, kde jsi na všech čtyřech a ze zadku ti trčí něco originálního. Překvap mě!",
        "Jednoduchá záležitost: budeš holka. To znamená paruku, vycpeš si prsa v šatech a budeš si to dělat. Samozřejmě mi pošleš video.",
        "Vezmeš toho svýho chcípáka a pořádně mu nafackuješ. Ať je červenej! Pošli video nebo fotku.",
        "Zatancuješ mi! Vyber si hudbu, kterou máš rád. Chci, aby to bavilo mě i tebe."]


varovani=("A pokud ne, tak si mě nepřej!",
          "A jestli nebudeš poslouchat, dostaneš, co si zasloužíš!",
          "A jestli se na to vykašleš, tak ti to spočítám, ty nulo!",
          "A zkus mi odmlouvat, prase!",
          "A je ti doufám jasný, co se stane když nebudeš hodnej.")

def generaator():
                mail=choice(["Čau ","Nazdar ","Ahoj "])+choice(["prase,","ubožáku,","zoufalče,", "nulo,", "otroku,"])+"\n\n"
                mail=mail+choice(smalltalk)
                mail=mail+choice([" Teď po tobě budu chtít tohleto...",
                        " Dneska jsem si pro tebe nachystala tohle:",
                        " Jsi zvědavej co pro tebe mám tentokrát?",
                        " Tentokrát pro mě uděláš následující...",
                        " Dnes po tobě budu chtít takovou drobnost:"])+"\n"
                mail=mail+choice(uukoly)+"\n"
                mail=mail+choice(varovani)
                mail=mail+"\n\ntvoje Paní Dagmar"
                print(mail)

generaator()
