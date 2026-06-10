import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.db import transaction
from turnaj.models import Tym, Hrac, Zapas, Střelec

class Command(BaseCommand):
    help = 'Bezpečně naplní databázi testovacími daty včetně hráčů a střelců zápasů'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                self.stdout.write('Provádím bezpečné promazání starých dat...')
                Střelec.objects.all().delete()
                Zapas.objects.all().delete()
                Hrac.objects.all().delete()
                Tym.objects.all().delete()

                jmena = ['Jan', 'Petr', 'Tomáš', 'Martin', 'Jiří', 'Jakub', 'Michal', 'David', 'Ondřej', 'Filip']
                prijmeni = ['Novák', 'Svoboda', 'Novotný', 'Dvořák', 'Černý', 'Procházka', 'Kučera', 'Veselý', 'Horák', 'Němec']

                realne_tymy = [
                    'AC Sparta Praha', 'SK Slavia Praha', 'FC Viktoria Plzeň', 
                    'SFC Opava', 'FC Slovan Liberec', 'SK Sigma Olomouc', 'FK Mladá Boleslav'
                ]
                
                tymy_objekty = []
                for nazev in realne_tymy:
                    tym = Tym.objects.create(jmeno_tymu=nazev)
                    tymy_objekty.append(tym)
                    
                    for _ in range(11):
                        Hrac.objects.create(
                            jmeno=random.choice(jmena),
                            prijmeni=random.choice(prijmeni),
                            id_tym=tym
                        )

                self.stdout.write('Generuji unikátní harmonogram zápasů a střelců...')
                
                vsechny_mozne_dvojice = []
                for i in range(len(tymy_objekty)):
                    for j in range(len(tymy_objekty)):
                        if i != j:
                            vsechny_mozne_dvojice.append((tymy_objekty[i], tymy_objekty[j]))
                
                random.shuffle(vsechny_mozne_dvojice)
                
                aktualni_datum = date(2026, 6, 1)
                posledni_tym_domaci = None
                posledni_tym_hoste = None
                odehrane_dvojice = set()
                
                pocet_zapasu = 0
                while pocet_zapasu < 15 and vsechny_mozne_dvojice:
                    domaci, hoste = vsechny_mozne_dvojice.pop(0)
                    
                    if domaci == posledni_tym_domaci or domaci == posledni_tym_hoste or hoste == posledni_tym_domaci or hoste == posledni_tym_hoste:
                        vsechny_mozne_dvojice.append((domaci, hoste))
                        continue
                        
                    zapas = Zapas(
                        id_domaci_tym=domaci,
                        id_hostujici_tym=hoste,
                        datum_zapasu=aktualni_datum
                    )
                    
                    rozhodne_datum = date(2026, 6, 20)
                    if aktualni_datum < rozhodne_datum:
                        zapas.domaci_goly = random.randint(0, 3)
                        zapas.hostujici_goly = random.randint(0, 3)
                        zapas.save()
                        
                        hraci_domaci = list(domaci.hraci.all())
                        for _ in range(zapas.domaci_goly):
                            hrac = random.choice(hraci_domaci)
                            Střelec.objects.create(id_zapas=zapas, id_hrac=hrac, pocet_golu=1)
                            
                        hraci_hoste = list(hoste.hraci.all())
                        for _ in range(zapas.hostujici_goly):
                            hrac = random.choice(hraci_hoste)
                            Střelec.objects.create(id_zapas=zapas, id_hrac=hrac, pocet_golu=1)
                    else:
                        zapas.domaci_goly = -1
                        zapas.hostujici_goly = -1
                        zapas.save()
                        
                    posledni_tym_domaci = domaci
                    posledni_tym_hoste = hoste
                    aktualni_datum += timedelta(days=random.randint(1, 2))
                    pocet_zapasu += 1

                self.stdout.write(self.style.SUCCESS('Úspěch! Všechna data bezpečně zapsána.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Chyba: {str(e)}'))