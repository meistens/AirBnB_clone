#!/usr/bin/python3
"""Initializing modules"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class city that shows cities, inherited from BaseModel"""
    state_id = ""
    name = ""
