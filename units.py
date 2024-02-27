length_c_units = {
    'kilometer': 10**3,
    'hectometer': 10**2,
    'decameter': 10,
    'meter': 1,
    'decimeter': 10**-1,
    'centimeter': 10**-2,
    'millimeter': 10**-3,
    'micrometer': 10**-6,
    'nanometer': 10**-9,
    'picometer': 10**-12,
    'femtometer': 10**-15,
    'attometer': 10**-18,

    'feet': 0.3048
}

weight_c_units = {
    'gigaton': 10**15,
    'megaton': 10**12,
    'ton': 10**6,
    'kilogram': 10**3,
    'gram': 1,
    'milligram': 10**-3,
    'microgram': 10**-6,
    'nanogram': 10**-9,
    'picogram': 10**-12,
    'femtogram': 10**-15,
    'attogram': 10**-18
}

time_c_units = {
    'millisecond': 10**-3,
    'second': 1,
    'minute': 60,
    'hour': 3600,
    'day': 86400,
    'week': 604800
}

amperage_c_units = {
    'petaampere': 10**15,
    'teraampere': 10**12,
    'gigaampere': 10**9,
    'megaampere': 10**6,
    'kiloampere': 10**3,
    'hectoampere': 10**2,
    'decaampere': 10,
    'ampere': 1,
    'deciampere': 10**-1,
    'centiampere': 10**-2,
    'milliampere': 10**-3,
    'microampere': 10**-6,
    'nanoampere': 10**-9,
    'picoampere': 10**-12,
    'femtoampere': 10**-15
}

def get_all_units(sep: str = None) -> list:
    all_units = []
    
    all_units.extend(i for i in length_c_units.keys())
    if not sep is None:
        all_units.append(sep)

    all_units.extend(i for i in weight_c_units.keys())
    if not sep is None:
        all_units.append(sep)

    all_units.extend(i for i in time_c_units.keys())
    if not sep is None:
        all_units.append(sep)

    all_units.extend(i for i in amperage_c_units.keys())
    if not sep is None:
        all_units.append(sep)

    all_units.extend(('celsius', 'fahrenheit', 'kelvin'))

    return all_units
