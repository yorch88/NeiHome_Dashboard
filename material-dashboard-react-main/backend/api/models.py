from django.db import models

# Create your models here.

# CLASS SUBDIVISION
class SubDivision(models.Model):
    typedivision = models.CharField(max_length=100)
    subdivision_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    representatives = models.TextField()
    cp = models.CharField(max_length=10)
    def __str__(self):
        return self.subdivision_name

# CLASS STREET
class Street(models.Model):
    name = models.CharField(max_length=200)
    id_subdivision = models.ForeignKey(SubDivision, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# CLASS NEIGBOR
class Neigbor(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    home_number = models.CharField(max_length=10)
    role = models.CharField(max_length=10)
    id_street = models.ForeignKey(Street, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    
# CLASS SUBDIVISIONUSERS
class SubdividionUsers(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=250)
    id_subdivision = models.ForeignKey(SubDivision, on_delete=models.CASCADE)
    id_neigbor = models.ForeignKey(Neigbor, on_delete=models.CASCADE)
    def __str__(self):
        return self.email

# CLASS ADMINS
class AdminUsers(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=200)
    id_subdivision = models.ForeignKey(SubDivision, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


# CLASS SUBDIVISIONS NUMBER DB
class SubdivisionNumberDB(models.Model):
    number = models.IntegerField()
    name_subdivision = models.CharField(max_length=250)
    def __str__(self):
        return self.number