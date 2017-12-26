import pandas as pd

from tribble.transformers import vendor_name_normalizer


def test_upcase() -> None:
    data = pd.DataFrame([
        {'id': 1, 'vendor_name': 'IBM Canada'}
    ])
    output = vendor_name_normalizer.VendorNameNormalizer().apply(data)
    assert output.to_dict('records') == [{'id': 1, 'vendor_name': 'IBM CANADA'}]

def test_apply() -> None:
    pass