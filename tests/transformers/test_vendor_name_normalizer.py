import pandas as pd
import pytest
from tribble.transformers import vendor_name_normalizer

@pytest.fixture
def template() -> typing.Dict:
    return {
        'contract_period_start': None,
        'contract_period_end': None,
        'delivery_date': None,
        'contract_date': None,
        'source_fiscal': datetime.date(2017, 1, 1),
    }

def test_apply() -> None:
    pass