import pandas as pd
import string, re
from tribble.transformers import base

class VendorNameNormalizer(base.BaseTransform):
    """Normalizes all Vendor names by converting to uppercase characters, removing punctuation and organization identifiers such as inc, or llc."""

    @staticmethod
    def _uppercase(vendor_name: str) -> str:
        vendor_name = vendor_name.upper()
        return vendor_name

    @staticmethod
    def _remove_punctuation(vendor_name: str) -> str:
        vendor_name = vendor_name.translate(str.maketrans('', '', string.punctuation))
        return vendor_name

    @staticmethod
    def _organization_identifiers(vendor_name: str) -> str:
        org_idents = ['LLC', 'LTD', 'INC', 'CPA', 'LLP', 'ULC', 'CORP']
        for ident in org_idents:
            regex = '\s+{}\W*'.format(ident)
            vendor_name = re.sub(regex, '', vendor_name)
        return vendor_name

    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
        data['vendor_name'] = data['vendor_name'].apply(self._uppercase)
        data['vendor_name'] = data['vendor_name'].apply(self._remove_punctuation)
        data['vendor_name'] = data['vendor_name'].apply(self._organization_identifiers)
        return data
