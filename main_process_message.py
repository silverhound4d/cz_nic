from odeslat_sms.utils import get_data
from odeslat_sms.utils import read_args
from odeslat_sms.process_message import process_message

if __name__ == "__main__":
    args = read_args()
    for dic in get_data(args['file_path']):
        process_message(dic['phone_number'], dic['message'], False)