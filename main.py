import requests

# https://blockstream.info/block/000000000000000000015f56e397bb29e36b7958aa58eb81ba316464838a5970

# EXAMPLE: single input
address = '181nc7DbpcYjVrpKtUf3WvDmvusvhPuXV3'

# EXAMPLE: multiple inputs
# address = '3QdwsH5yVHATYsvvVqTx4A7jTtuGr9bUN5'

# EXAMPLE: single output, possibly an exchange deposit account
# address = '12cgpFdJViXbwHbhrA3TuW1EGnL25Zqc3P'

links = []
points = {}
url = 'https://blockstream.info/api/address/' + address + '/txs'
response = requests.get(url)

for tx in response.json():
    for tx_input in tx['vin']:
        link = {
            'source': tx_input['prevout']['scriptpubkey_address'],
            'target': tx['txid'],
            'value': tx_input['prevout']['value']
        }
        links.append(link)
        points[link['source']] = {
            'id': link['source'],
            'type': 'address'
        }
        points[link['target']] = {
            'id': link['target'],
            'type': 'transaction'
        }

    for tx_output in tx['vout']:
        link = {
            'source': tx['txid'],
            'target': tx_output['scriptpubkey_address'],
            'value': tx_output['value']
        }
        links.append(link)
        points[link['source']] = {
            'id': link['source'],
            'type': 'transaction'
        }
        points[link['target']] = {
            'id': link['target'],
            'type': 'address'
        }

print(links)
print('--------')
print(list(points.values()))
