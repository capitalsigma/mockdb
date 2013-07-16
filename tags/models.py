from django.db import models

# Create your models here.

class TaggedResource(models.Model):
    """Every TaggedResource has exactly one:
         -- date_added: the date when it was first entered into the database
         -- date_modified: the date when it was last modified
         -- uploader: the MockDB user who uploaded the file
         -- Accessor: an object that wraps either a local resource URL or a 
                      a call to the Drive SDK
         -- PermissionsSet: an object that defines who has r/w access
       Every tagged resource has zero or more:
         -- Tag: 
    """
         
