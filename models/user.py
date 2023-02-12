#!/usr/bin/python3
"""Initializing modules which inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for the interpreter that"\
    "inherits from the BaseModel(see UML.md)"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
