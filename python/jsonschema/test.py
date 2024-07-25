#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Links:
* https://builtin.com/software-engineering-perspectives/python-json-schema

"""
from jsonschema import validate
import jsonschema
import unittest

# Simple Schema of type object
schemaOne = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "level": {"type": "string"}
    },
    "required": ["name", "age"],
    "additionalProperties": False
}

# Simple schema of type list (of objects).
schemaTwo = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "number"},
            "scores": {
                "type": "array", 
                "items": {"type": "number"},
                "minItems": 4
            }
        }
    }

}


class TestSchema(unittest.TestCase):
    def test_validOne(self):

        # Valid data. 
        data = {
            "name": "Joe",
            "age": 434,
            "level": "L4"
        }
        validate(schema=schemaOne, instance=data)

        # Valid data.
        data = {
            "name": "Joe",
            "age": 434.9
        }
        validate(schema=schemaOne, instance=data)

        # Invalid (address) is not part of schema and 
        # additionalProperties is set to False
        data = {                                                                      
            "name": "Behzad",                                                            
            "age": 47,                                                                   
            "address": "abcd"                                                            
        }     
        with self.assertRaises(jsonschema.exceptions.ValidationError) as context:
            validate(schema=schemaOne, instance=data)

        self.assertTrue("Additional properties are not allowed" in str(context.exception))

    def test_validateTwo(self):
        data = [
                {"name": "Behzad", "age": 40, "scores": [43, 44, 34, 53]}, 
                {"name": "Json", "age": 43, "scores": [43, 34, 23,34]}
        ]
        validate(schema=schemaTwo, instance=data)




