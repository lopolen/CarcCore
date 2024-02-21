import units


def convert(value: float, unit: str, convert_to: str) -> tuple[float, str]:
    if (unit in units.length_c_units.keys()) and (convert_to in units.length_c_units.keys()):
        multiplier = units.length_c_units[unit] / units.length_c_units[convert_to]

    elif (unit in units.weight_c_units.keys()) and (convert_to in units.weight_c_units[convert_to]):
        multiplier = units.weight_c_units[unit] / units.weight_c_units[convert_to]

    elif (unit in units.time_c_units.keys()) and (convert_to in units.time_c_units.keys()):
        multiplier = units.time_c_units[unit] / units.time_c_units[convert_to]

    elif (unit in units.amperage_c_units.keys()) and (convert_to in units.amperage_c_units.keys()):
        multiplier = units.amperage_c_units[unit] / units.amperage_c_units[convert_to]

    # Temperature
    elif unit == 'fahrenheit' and convert_to == 'celsius':
        return 5 / 9 * (value - 32), convert_to

    elif unit == 'celsius' and convert_to == 'fahrenheit':
        return 9 / 5 * value + 32, convert_to

    elif unit == 'celsius' and convert_to == 'kelvin':
        return value + 273.15, convert_to

    elif unit == 'kelvin':
        value -= 273.15
        if convert_to == 'fahrenheit':
            return 9 / 5 * value + 32, convert_to
        else:
            return value, convert_to

    else:
        raise ValueError

    return value * multiplier, convert_to
