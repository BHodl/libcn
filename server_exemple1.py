"""Exemple of handling callback from cyphernode"""
from libcn.libcn import CallbackFlaskServer
import json
from flask import request
def unconf():
    """Do stuff with unconfirmed paiment callbacks"
    fields = ['id', 'address', 'hash', 'vout_n', 'sent_amount', \
        'confirmations', 'received', 'size', \
        'vsize', 'fees', 'is_replaceable', 'pub32', \
            'pub32_label', 'pub32_derivation_path', 'eventMessage']"""
    #print(request.get_data().decode('utf-8'))
    if request:
        call = json.loads(request.get_data().decode('utf-8'))
        amount = call['sent_amount']
        amount = format(amount, '.8f')
        amount = '{} ₿'.format(amount)
        fees = call['fees']
        fees = format(fees, '.8f')
        fees = '{} ₿'.format(fees)
        #print('Paiment non confirmé = {}'.format(call))
        print('Unconfirmed of adresse \'{}\' received {} at {} and the transaction fees is {}'\
            .format(call['address'], amount, call['received'], fees))

def conf():
    """Do stuff with confirmed paiment callbacks"
    fields = ['id', 'address', 'hash', 'vout_n', 'sent_amount', \
        'confirmations', 'received', 'size', \
        'vsize', 'fees', 'is_replaceable', 'pub32', \
            'pub32_label', 'pub32_derivation_path', 'eventMessage']"""
    #print(request.get_data().decode('utf-8'))
    if request:
        call = json.loads(request.get_data().decode('utf-8'))
        amount = call['sent_amount']
        amount = format(amount, '.8f')
        amount = '{} ₿'.format(amount)
        fees = call['fees']
        fees = format(fees, '.8f')
        fees = '{} ₿'.format(fees)
        #print('Paiment non confirmé = {}'.format(call))
        print('Confirmation of adresse \'{}\' received {} at {} and the transaction fees is {}'\
            .format(call['address'], amount, call['received'], fees))

def txunconf():
    """Do stuff with unconfirmed transation callbacks
    fields = ['id', 'txid', 'confirmations']"""
    if request:
        call = json.loads(request.get_data().decode('utf-8'))
        print('Transaction non confirmé = {}'.format(call))

def txconf():
    """Do stuff with confirmed transaction callbacks"
    fields = ['id', 'txid', 'confirmations']"""
    if request:
        call = json.loads(request.get_data().decode('utf-8'))
        print('Transaction confirmé = {}'.format(call))

def ln_invoice():
    "Do stuff with lightning invoice callbacks"
    if request:
        call = json.loads(request.get_data().decode('utf-8'))
        print('Lightning invoice confirmé = {}'.format(call))

def ln_connect():
    "Do stuff with lightning connected node callbacks"
    if request:
        call = json.loads(request.get_data().decode('utf-8'))
        print('lightning connect confirmé = {}'.format(call))

def ots_stamp():
    "Do stuff with ots callbacks"
    print(request.remote_addr)
    if request:
        call = json.loads(request.get_data().decode('utf-8'))
        print('OTS stamp confirmé = {}'.format(call['result']))

a = CallbackFlaskServer('action', 2906)
a.add_endpoint(endpoint='/unconf', endpoint_name='unconf', handler=unconf)
a.add_endpoint(endpoint='/conf', endpoint_name='conf', handler=conf)
a.add_endpoint(endpoint='/txunconf', endpoint_name='txunconf', handler=txunconf)
a.add_endpoint(endpoint='/txconf', endpoint_name='txconf', handler=txconf)
a.add_endpoint(endpoint='/ln_invoice', endpoint_name='ln_invoice', handler=ln_invoice)
a.add_endpoint(endpoint='/ln_connect', endpoint_name='ln_connect', handler=ln_connect)
a.add_endpoint(endpoint='/ots_stamp', endpoint_name='ots_stamp', handler=ots_stamp)
a.run()
