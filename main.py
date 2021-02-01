import requests

address = '181nc7DbpcYjVrpKtUf3WvDmvusvhPuXV3'
transactions = []
url = 'https://blockstream.info/api/address/' + address + '/txs'
response = requests.get(url)

for tx in response.json():
    for output in tx['vout']:
        simple_tx = {}
        simple_tx['from'] = tx['vin'][0]['prevout']['scriptpubkey_address']
        simple_tx['to'] = output['scriptpubkey_address']
        simple_tx['amount'] = output['value']
        transactions.append(simple_tx)
    print(transactions)
