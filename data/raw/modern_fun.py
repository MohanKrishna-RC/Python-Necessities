import pandas as pd
from decimal import Decimal
from typing import NewType

#ideal notation
def cheeseshop(kind: str, weight: int, region:str = None) ->Decimal:
    print("weeee")

""" # We could implement our own type of Decimal here """
Price = NewType('Price',Decimal)
def cheeseshop1(kind: str, weight: int, region:str = None) ->Price :
    print("Hii")
cheeseshop(1,1,1) 

from decimal import Decimal
from django.db import models
​
class Cheese(models.Model):
    # model snipped for brevity
    name = models.CharField(...)
​
def cheeseshop(
    kind: Cheese,
    weight: int,
    region=None: str,
) -> Decimal:

def cheeseshop(
    kind: int,
    weight: int,
    *,
    region: str=None,
) -> Price:
    print("dff")

""" Here the asterik "*" signifies the seperation between args and kwargs, and it actually enforces this. This meant region --if given, because it's still optional -- must provided as a __kwarg__ """