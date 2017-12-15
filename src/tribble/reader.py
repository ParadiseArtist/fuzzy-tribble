import itertools
import json
import os
import typing
import pandas as pd
from tqdm import tqdm


T = typing.TypeVar('T')


def _json_blobs(input_dir: str) -> typing.Iterator[typing.Dict[str, typing.Any]]:
    input_filenames = [os.path.join(input_dir, dir_name) for dir_name in os.listdir(input_dir)]

    print("Reading " + str(len(input_filenames)) + " files:")
    for filename in tqdm(input_filenames):
        with open(filename) as input_file:
            yield json.loads(input_file.read())


def _grouper(iterable: typing.Iterable[T], group_length: int) -> typing.Iterable[T]:
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * group_length
    return itertools.zip_longest(*args, fillvalue=None)


def read_dir(input_dir: str, grouping_length: int = 100) -> pd.DataFrame:
    df: typing.Optional[pd.DataFrame] = None

    blobs = _json_blobs(input_dir)
    for group in _grouper(blobs, grouping_length):
        chunk = [x for x in group if x]
        df = pd.DataFrame(chunk) if df is None else df.append(chunk)

    return df if df is not None else pd.DataFrame()
