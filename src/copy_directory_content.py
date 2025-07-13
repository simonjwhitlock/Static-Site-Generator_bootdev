import os
import shutil

def dir_copy_all(source,dest):
    if not os.path.exists(source):
        raise Exception(f"directory {source} does not exist")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    source_list = os.listdir(source)
    os.mkdir(dest)
    if os.path.isfile(source):
        shutil.copy(source,dest)
    else:
        for item in source_list:
            item_source = os.path.join(source,item)
            item_dest = os.path.join(dest, item)
            if os.path.isfile(item_source):
                shutil.copy(item_source,item_dest)
            if os.path.isdir(item_source):
                dir_copy_all(item_source, item_dest)