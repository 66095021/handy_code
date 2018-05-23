#!/bin/env python
#openssl genrsa -out key.pem 1024
#openssl rsa -in key.pem -pubout -out pubkey.pem

#!/bin/env python
import M2Crypto
import json
import base64
from M2Crypto import RSA, BIO

__author__ = "chengbo"


def pub_encrypt(msg, file_name):
    rsa_pri = M2Crypto.RSA.load_pub_key(file_name)
    output = ""
    while msg:
        input = msg[:117]
        msg = msg[117:]
        ctxt_pri = rsa_pri.public_encrypt(input, M2Crypto.RSA.pkcs1_padding)
        output = output + ctxt_pri
    ctxt64_pri = base64.b64encode(output)
    print ('enc:%s' % ctxt64_pri, type(ctxt64_pri))
    return ctxt64_pri


def pri_decrypt(encrypted, file_name):
    output = ""
    priv_key = RSA.load_key(file_name)
    encrypted = base64.b64decode(encrypted)

    while encrypted:
        input = encrypted[:128]
        encrypted = encrypted[128:]
        out = priv_key.private_decrypt(input, RSA.pkcs1_padding)
        output = output + out
    return output


pubkey_file = 'pubkey.pem'
prikey_name = "key.pem"
f = open("/tmp/test")
c = f.read()
e = pub_encrypt(c, pubkey_file)
print e
print pri_decrypt(e, prikey_name)
