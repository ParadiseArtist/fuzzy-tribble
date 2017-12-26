import pandas as pd
import string
from tribble.transformers import base

class VendorNameNormalizer(base.BaseTransform):
    """Normalizes all Vendor names by converting to uppercase characters, removing punctuation and organization identifiers such as inc, or llc."""

    @staticmethod
    def _uppercase(vendor_name: str) -> str:
        vendor_name = vendor_name.upper()
        return vendor_name

    _TRANSLATOR = str.maketrans('', '', string.punctuation)


    @staticmethod
    def _remove_punctuation_from_vendor_name(row: pd.Series) -> pd.Series:
        if row['vendor_name'] is not None:
            row['vendor_name'] = row['vendor_name'].translate(_TRANSLATOR)
        return row

    @staticmethod
    def _organization_identifiers(row: pd.Series) -> pd.Series:
        pass

    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
        data['vendor_name'] = data['vendor_name'].apply(self._uppercase)
        return data
