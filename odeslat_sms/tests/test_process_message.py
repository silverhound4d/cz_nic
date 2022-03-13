import pytest
import re
from odeslat_sms import process_message as pm
from odeslat_sms.utils import get_data

class Test_002_ProcessMessage:
    @pytest.mark.parametrize(
        'number, expected',[
            ('+420.123456789', True),
            ('(420)123-456-748', True),
            ('4201234544546', False),
            ('123456789', False),
            ('+425123', False),
            ('+ABC123456789', False),
            ('+/*/ sqw24', False)
        ]
    )
    def test_validate_number(self, number, expected):
        assert pm.validate_number(number) == expected
    
    def test_validate_message(self, get_messages):
        for msg in get_messages:
            if len(msg) == 0:
                assert pm.validate_message(msg) is False
            elif len(msg) > 255:
                assert pm.validate_message(msg) is False
            elif len(msg) <= 255:
                assert pm.validate_message(msg) is True
    
    def test_format_phone_num(self):
        phone_nums = ["+421123456789", "+420.123567111", "(455)564-741-612"]
        pattern = re.compile("^\+\d{12}$")
        for num in phone_nums:
            formatted_num = pm.format_phone_number(num)
            assert re.match(pattern, formatted_num) is not None

    def test_process_msg(self):
        data = get_data(R'odeslat_sms\test_data\test_data.csv')
        expected = [int(data['expected']) for data in data]
        actual = []
        for dic in data:
            actual.append(pm.process_message(dic['phone_number'], dic['message'], False))
        assert expected == actual