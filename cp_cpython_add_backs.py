

def delattr(target,name):
    exec('del str_target.'+name, {'str_target':target})