from django.db import models
from django.core.validators import MinValueValidator

class Tym(models.Model):
    jmeno_tymu = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.jmeno_tymu

class Hrac(models.Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    id_tym = models.ForeignKey(Tym, on_delete=models.CASCADE, related_name='hraci')

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} ({self.id_tym.jmeno_tymu})"

class Zapas(models.Model):
    id_domaci_tym = models.ForeignKey(Tym, on_delete=models.CASCADE, related_name='zapas_domaci')
    id_hostujici_tym = models.ForeignKey(Tym, on_delete=models.CASCADE, related_name='zapas_hoste')
    datum_zapasu = models.DateField()
    domaci_goly = models.IntegerField(default=-1, validators=[MinValueValidator(-1)])
    hostujici_goly = models.IntegerField(default=-1, validators=[MinValueValidator(-1)])

    def __str__(self):
        return f"{self.id_domaci_tym} vs. {self.id_hostujici_tym} ({self.datum_zapasu})"

class Střelec(models.Model):
    id_zapas = models.ForeignKey(Zapas, on_delete=models.CASCADE, related_name='strelci')
    id_hrac = models.ForeignKey(Hrac, on_delete=models.CASCADE, related_name='goly_v_zapasech')
    pocet_golu = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id_hrac.prijmeni} - {self.pocet_golu}x v zápase {self.id_zapas}"