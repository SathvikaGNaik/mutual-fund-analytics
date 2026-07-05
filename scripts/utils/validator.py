"""
Validation functions
"""


def validate_positive(series):
    """Count values <= 0"""
    return (series <= 0).sum()


def validate_duplicates(df):
    """Count duplicate rows"""
    return df.duplicated().sum()


def validate_range(series, minimum, maximum):
    """Count values outside a range"""
    return (~series.between(minimum, maximum)).sum()