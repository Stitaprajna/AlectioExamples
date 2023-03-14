import hashlib
import json
import os

def generate_file_hash(file_path, hash_type='md5', blocksize=2**20):
    if hash_type == 'md5':
        m = hashlib.md5()
    elif hash_type == 'sha256':
        m = hashlib.sha256()

    if blocksize == -1:
        with open(file_path, "rb") as f:
            f_byte = f.read()
        m.update(f_byte)
        return m.hexdigest()
    else:
        with open(file_path, "rb" ) as f:
            while True:
                buf = f.read(blocksize)
                if not buf:
                    break
                m.update(buf)
        return m.hexdigest()

def generate_ann_hash(anns):
    m = hashlib.sha256()
    for ann in anns:
        ann = json.dumps(ann, sort_keys=True).encode()
        m.update(ann)
    return m.hexdigest()