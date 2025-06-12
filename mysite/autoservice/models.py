from django.db import models

class Automobilio_modelis(models.Model):
    marke = models.CharField(max_length=100)
    modelis = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.marke} {self.modelis}"

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobilio Modeliai"

class Automobilis(models.Model):
    valstybinis_nr = models.CharField(max_length=6, unique=True)
    automobilio_modelis = models.ForeignKey("Automobilio_modelis", on_delete=models.SET_NULL, null=True)
    vin_kodas = models.CharField(max_length=17, unique=True)
    klientas = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.automobilio_modelis.marke} {self.automobilio_modelis.modelis}"

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "automobiliai"

class Paslauga(models.Model):
    pavadinimas = models.CharField(max_length=40)
    kaina = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.pavadinimas} - {self.kaina}"

class Uzsakymas(models.Model):
    data = models.DateTimeField
    automobilis = models.ForeignKey("Automobilis", on_delete=models.SET_NULL, null=True)
    suma = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.data} {self.automobilis} {self.suma}"

class Uzsakymo_eilute(models.Model):
    paslauga = models.ForeignKey("Paslauga", on_delete=models.SET_NULL, null=True)
    uzsakymas = models.ForeignKey("Uzsakymas", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField(max_digits=6, decimal_places=1)
    kaina = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.uzsakymas} {self.paslauga} {self.kiekis} {self.kaina}"