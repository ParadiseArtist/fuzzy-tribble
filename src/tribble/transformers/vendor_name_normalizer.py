import pandas as pd
import re, string
from tribble.transformers import base

class VendorNameNormalizer(base.BaseTransform):
    """Normalizes all Vendor names by converting to uppercase characters, removing punctuation and organization identifiers such as inc, or llc."""

    @staticmethod
    def _uppercase_vendor_name(row: pd.Series) -> pd.Series:
        if row['vendor_name'] is not None:
            row['vendor_name'] = row['vendor_name'].upper()
        return row

    @staticmethod
    def _remove_punctuation_from_vendor_name(row: pd.Series) -> pd.Series:
        if row['vendor_name'] is not None:
            translator = str.maketrans('', '', string.punctuation)
            row['vendor_name'] = row['vendor_name'].translate(translator)
        return row

    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
