import yaml

from conftest import BASE_DIR


def build_address_finc():
    with open(BASE_DIR + '/data/address_data.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        data_list = list()
        for i in data:
            data_list.append((i.get('name'), i.get('phone')))
        print(data_list)
        return data_list
