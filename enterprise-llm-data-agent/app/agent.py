from .sql_validator import validate_read_only

def analyst_plan(question):
    return {'question':question,'steps':['retrieve business definitions','generate SQL','validate SQL','execute read-only query','explain results with evidence']}

def run_sql(sql,execute):
    validate_read_only(sql); return execute(sql)
