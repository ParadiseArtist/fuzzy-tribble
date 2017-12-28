import re
import pandas as pd
from tribble.transformers import base

class VendorNameNormalizer(base.BaseTransform):
    """Normalizes all Vendor names by converting to uppercase characters,
    removing punctuation and organization identifiers such as inc, or llc."""

    @staticmethod
    def _uppercase(vendor_name: str) -> str:
        vendor_name = vendor_name.upper()
        return vendor_name

    @staticmethod
    def _remove_punctuation(vendor_name: str) -> str:
        vendor_name = vendor_name.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
        return vendor_name

    @staticmethod
    def _organization_identifiers(vendor_name: str) -> str:
        org_idents = ['LLC', 'LTD', 'INC', 'CPA', 'LLP', 'ULC', 'CORP']
        for ident in org_idents:
            regex = r'\s+{}\W*$'.format(ident)
            vendor_name = re.sub(regex, '', vendor_name)
        return vendor_name

    @staticmethod
    def _whitespace_clean_up(vendor_name: str) -> str:
        vendor_name = vendor_name.strip()
        vendor_name = re.sub(r'\s{2,}', ' ', vendor_name)
        return vendor_name

    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
        data['vendor_name'] = data['vendor_name'].apply(self._uppercase)
        data['vendor_name'] = data['vendor_name'].apply(self._remove_punctuation)
        data['vendor_name'] = data['vendor_name'].apply(self._organization_identifiers)
        data['vendor_name'] = data['vendor_name'].apply(self._whitespace_clean_up)
        return data
