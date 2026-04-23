import pytest
import pandas as pd
import json

from src.validation.data_validations import validate_from_config


@pytest.fixture
def processed_df():
    return pd.read_csv("data/processed/processed_healthcare_data.csv")


@pytest.fixture
def config_data():
    with open("config/validation_config.json") as f:
        return json.load(f)


def test_config_driven_validation(processed_df, config_data):
    assert validate_from_config(processed_df, config_data) == True