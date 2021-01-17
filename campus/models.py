from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Chambre(models.Model):
    individuel = 'individuel'
    double = 'double'
    chambernumber = models.CharField(max_length=20)
    batnumber = models.CharField(max_length=10)
    TYPE_CHAMBRE = [
        (individuel, 'individuel'),
        (double, 'double'),
    ]
    typeChambre = models.CharField(max_length=20, choices=TYPE_CHAMBRE, default=individuel)

    def __str__(self):
        return self.chambernumber

class Etudiant(models.Model):
    boursierLoger = 'Boursier logé'
    boursierNonLoger = 'Boursier non logé'
    nonBoursier = 'Non Boursier'
    TYPE_ETUDIANT = [
        (boursierLoger, 'Boursier logé'),
        (boursierNonLoger, 'Boursier non logé'),
        (nonBoursier, 'Non Boursier'),
    ]
    matricule = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    birthday = models.DateField()
    image =  models.ImageField(upload_to='images/', blank=True, null=True)
    typeEtudiant = models.CharField(max_length=50, choices=TYPE_ETUDIANT, default=nonBoursier)
    bourse = models.CharField( max_length=20,blank=True, null=True)
    addresse = models.CharField(max_length=100,blank=True, null=True)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.matricule



