from django.db import models

# Define the Category model which will be used to categorize Articles
class Category(models.Model):
    # The name field will store the category name
    name = models.CharField(max_length=255)

    # The __str__ method provides a human-readable string representation of the Category object
    def __str__(self):
        return self.name

# Define the Type model which will be used to specify the type of an Article
class Type(models.Model):
    # The name field will store the type name
    name = models.CharField(max_length=255)

    # The __str__ method provides a human-readable string representation of the Type object
    def __str__(self):
        return self.name

# Define the Article model to represent individual articles
class Article(models.Model):
    # A ForeignKey field that links the Article to a specific Category
    # on_delete=models.CASCADE ensures that if the category is deleted, the articles belonging to it will be deleted as well
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # A ForeignKey field that links the Article to a specific Type
    # on_delete=models.CASCADE ensures that if the type is deleted, the articles belonging to it will be deleted as well
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    # The name field stores the title or name of the article
    name = models.CharField(max_length=255)

    # The born field stores the year the person (if relevant) was born
    born = models.IntegerField(null=True, blank=True)

    # The died field stores the year the person (if relevant) passed away
    died = models.IntegerField(null=True, blank=True)

    # The nationality field stores the nationality of the person (if relevant)
    nationality = models.CharField(max_length=255, null=True, blank=True)

    # The known_for field stores what the person (if relevant) is known for
    known_for = models.CharField(max_length=255, null=True, blank=True)

    # The notable_work field stores the notable work or achievement of the person (if relevant)
    notable_work = models.CharField(max_length=255, null=True, blank=True)

    # The about field stores additional information about the article or person (if relevant)
    about = models.TextField(null=True, blank=True)

    # The year field stores the year the article was created or published
    year = models.IntegerField(null=True, blank=True)

    # The medium field stores the medium used for the article or work (e.g., painting, sculpture, etc.)
    medium = models.CharField(max_length=255, null=True, blank=True)

    # The dimensions field stores the dimensions of the article or work (e.g., size for artworks)
    dimensions = models.CharField(max_length=255, null=True, blank=True)

    # The location field stores the location where the article or work is displayed or stored
    location = models.CharField(max_length=255, null=True, blank=True)

    # The designer_name field stores the name of the designer (if relevant)
    designer_name = models.CharField(max_length=255, null=True, blank=True)

    # The developer_name field stores the name of the developer (if relevant)
    developer_name = models.CharField(max_length=255, null=True, blank=True)

    # The __str__ method provides a human-readable string representation of the Article object, using its name
    def __str__(self):
        return self.name
