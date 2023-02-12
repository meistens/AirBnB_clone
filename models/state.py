#!/usr/bin/python3
"""Initializing modules that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class state that inherits from BaseModel"""
    name = ""
