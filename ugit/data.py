import os
#import hashing functions like sha1sum
import hashlib

GIT_DIR = '.ugit'

def init():
    #make dir .git
    os.makedirs(GIT_DIR)
    #make dir /.git/objects
    os.makedirs(f'{GIT_DIR}/objects')


def hash_object(data, type_ ='blob'):

    # add type of content on starting with null value as partition
    obj = type_.encode() + b'\x00' + data
    #make hash of data and then use it as id to store data in  that file
    oid = hashlib.sha1(obj).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}','wb') as out:
        out.write(obj)
    return oid

def get_object(oid, expected = 'blob'):
    with open(f'{GIT_DIR}/objects/{oid}','rb') as f:
        obj = f.read()

    # partition them as type_, null, data
    type_,_,content = obj.partition(b'\x00')
    type_ = type_.decode()
    # verify if given type matched expected type
    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content
