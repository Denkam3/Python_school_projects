"""
This module implements various functions for physical units conversion.
"""

import numbers


def convert_speed(value, actual_unit: str, target_unit: str):
    """
    Convert speed value from actual_unit to target_unit. Return converted value.
    :param value: numeric value to convert
    :param actual_unit: string actual physical unit (mph, kph)
    :param target_unit: string target physical unit (mph, kph)
    :return: converted value
    :raises ValueError: exception due to wrong value, actual_unit, target_unit value
    """
    # make sure it's in lower case
    actual_unit, target_unit = actual_unit.lower(), target_unit.lower()
    # test acceptable inputs
    if isinstance(value, numbers.Number) and \
            all(x in ["mph", "kph"] for x in [actual_unit, target_unit]):
        # check units equality
        if actual_unit == target_unit:
            return value
        # dictionary for conversion, key is target unit
        conversion = {"kph": lambda x: x * 1.60934,
                      "mph": lambda x: x * 0.621371192
                      }
        return conversion[target_unit](value)
    raise ValueError("value must be numeric,"
                     " actual_unit and target_unit accept only mph or kph values")

def convert_temp(value, actual_unit:str, target_unit:str):
    """
    Convert temperature from Celsius to Kelvin or vise versa
    :param value: numeric value to convert
    :param actual_unit: unit I want to convert (°C or K)
    :param target_unit: what I want to convert it into (°C or K)
    :return: converted value
    :raises ValueError: wrong value or units were entered, unable to convert
    """
    # make sure it's in upper case
    actual_unit, target_unit = actual_unit.upper(), target_unit.upper()
    if isinstance(value,numbers.Number) and \
           all(x in ["°C", "K"] for x in [actual_unit, target_unit]):
        if actual_unit == target_unit:
            return value
        conversion = {"°C": lambda x: x - 273.15,
                      "K": lambda x: x + 273.15
                      }
        return conversion[target_unit](value)
    raise ValueError("value must be numeric,"
                     " actual:unit and target_unit accept only °C or K values")
