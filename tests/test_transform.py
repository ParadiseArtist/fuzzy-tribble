import datetime
import typing
import pandas
from tribble import transform


def data_template(overrides: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
    data = {
        "uuid": "tbs-0000000000",
        "vendorName": "ABC Company",
        "referenceNumber": "0000000000",
        "contractDate": "2012â03â31",
        "description": "499 OTHER PROFESSIONAL SERVICES NOT ELSEWHERE SPECIFIED",
        "extraDescription": "Big Contract #1",
        "objectCode": "0499",
        "contractPeriodStart": "2012-04-01",
        "contractPeriodEnd": "2018-03-31",
        "startYear": "2012",
        "endYear": "2018",
        "deliveryDate": "",
        "originalValue": 6000.0,
        "contractValue": 6000,
        "comments": "This contract includes one or more amendments.This contract was competitively sourced." +
                    "This contract is a multi-year contract.",
        "ownerAcronym": "tbs",
        "sourceYear": 2012,
        "sourceQuarter": 1,
        "sourceFiscal": "201213-Q4",
        "sourceFilename": r"tbs\/5ae78038dd512ae3f7e8a91349f443cb.html",
        "sourceURL": r"http:\/\/www.tbs-sct.gc.ca\/scripts\/contracts-contrats\/reports-rapports-eng.asp" +
                     "?r=c&refNum=0000000000&q=4&yr=2012&d=",
        "amendedValues": [],
        "contractPeriodRange": "2012-04-01 to 2018-03-31",
        "yearsDuration": 6,
        "valuePerYear": 1000.0,
        "vendorClean": "Big Contract #1"
    }
    data.update(overrides)
    return data


def output_template(overrides: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
    data = {
        "uuid": "tbs-0000000000",
        "vendor_name": "ABC Company",
        "reference_number": "0000000000",
        "contract_date": datetime.date(2012, 3, 31),
        "contract_period_start": datetime.date(2012, 4, 1),
        "contract_period_end": datetime.date(2018, 3, 31),
        "reporting_period_start": datetime.date(2012, 4, 1),
        "reporting_period_end": datetime.date(2018, 3, 31),
        "contract_value": 6000,
        "department": "tbs",
        "source_fiscal": datetime.date(2013, 1, 1),
        "object_code": "0499"
    }
    data.update(overrides)
    return data


def test_transform() -> None:
    data = pandas.DataFrame([data_template({})])
    output = transform.transform(data).to_dict('records')

    assert output == [output_template({})]


def test_bad_contract_dates() -> None:
    data = data_template({
        'contractDate': '2012-10-10',
        'contractPeriodStart': '0001-01-01',
        'contractPeriodEnd': '1899-12-31',
    })
    df = pandas.DataFrame([data])

    expected = output_template({
        'contract_date': datetime.date(2012, 10, 10),
        'contract_period_start': datetime.date(2012, 10, 10),
        'contract_period_end': datetime.date(2012, 10, 10),
        'reporting_period_start': datetime.date(2012, 10, 10),
        'reporting_period_end': datetime.date(2012, 10, 10),
    })
    assert transform.transform(df).to_dict('records') == [expected]
