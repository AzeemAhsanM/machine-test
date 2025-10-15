from django.db import models

# Create your models here.

class Airport(models.Model):
    # The unique code for the airport, e.g., 'A', 'B'.
    code = models.CharField(max_length=1, unique=True, help_text="Unique 1-letter airport code")

    # Self-referential foreign key to represent the parent airport.
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # The direction from the parent, 'left' or 'right'.
    position = models.CharField(max_length=5 ,choices=[('left', 'Left'), ('right', 'Right')] ,null=True ,blank=True)

    # The duration/distance in km from the parent.
    duration = models.PositiveIntegerField(null=True ,blank=True ,help_text="Distance in km from the parent airport.")

    def __str__(self):
        # Check if the airport has a parent.
        if self.parent:
            # If it's a child node, return a descriptive string.
            return f"{self.code} ({self.duration}km {self.position} of {self.parent.code})"
        # If it has no parent, it's a root node.
        return f"Airport {self.code} (Root)"