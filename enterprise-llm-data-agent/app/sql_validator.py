import sqlglot

def validate_read_only(sql):
    tree=sqlglot.parse_one(sql)
    blocked={'INSERT','UPDATE','DELETE','DROP','ALTER','TRUNCATE','CREATE','MERGE'}
    if any(node.key.upper() in blocked for node in tree.walk()): raise ValueError('Only read-only SQL is allowed')
    return True
