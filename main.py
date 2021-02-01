import requests

# https://blockstream.info/block/000000000000000000015f56e397bb29e36b7958aa58eb81ba316464838a5970

# EXAMPLE: single input
address = '181nc7DbpcYjVrpKtUf3WvDmvusvhPuXV3'

# EXAMPLE: multiple inputs
# address = '3QdwsH5yVHATYsvvVqTx4A7jTtuGr9bUN5'

# EXAMPLE: single output, possibly an exchange deposit account
# address = '12cgpFdJViXbwHbhrA3TuW1EGnL25Zqc3P'

transactions = []
url = 'https://blockstream.info/api/address/' + address + '/txs'
response = requests.get(url)

for tx in response.json():
    for input in tx['vin']:
        for output in tx['vout']:
            simple_tx = {}
            simple_tx['from'] = input['prevout']['scriptpubkey_address']
            simple_tx['to'] = output['scriptpubkey_address']
            simple_tx['amount'] = output['value']
            simple_tx['txid'] = tx['txid']
            transactions.append(simple_tx)

print(transactions)
