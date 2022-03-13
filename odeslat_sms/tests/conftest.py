import pytest
from odeslat_sms.utils import get_data


@pytest.fixture
def get_messages():
    path = 'odeslat_sms\data.csv'
    messages = [dic['message'] for dic in get_data(path)]
    return messages