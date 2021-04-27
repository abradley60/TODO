import pytest
from todo import *


@pytest.mark.parametrize("description, expected", [("Walk the dog", True)])
def test_create(description, expected):
    id_, df = create(description, save=False)
    assert (id_ in df.index) == expected


@pytest.mark.parametrize("description, new_description", [("Walk the dog", "run the dog")])
def test_toggle(description, new_description):
    id_, df = create(description, save=False)
    assert df.loc[id_]["description"] == description
    df = toggle(id_, new_description, save=False, df=df)
    assert df.loc[id_]["description"] == new_description


@pytest.mark.parametrize("description, expected", [("Walk the dog", True)])
def test_update(description, expected):
    id_, df = create(description, save=False)
    assert df.loc[id_]["completed"] == False
    df = update(id_, df=df, save=False)
    assert df.loc[id_]["completed"] == expected


@pytest.mark.parametrize("description, expected", [("Walk the dog", True)])
def test_delete(description, expected):
    id_, df = create(description, save=False)
    assert df.loc[id_]["completed"] == False
    df = delete(id_, df=df, save=False)
    assert df.empty
