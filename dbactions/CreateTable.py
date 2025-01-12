import dbactions
from sqlalchemy import text
def create_table():
    dbactions.conn.execute(text("""
                           create table if not exists test (id numeric)
                           """))
    data = get_table_data()
    print("###########################")
    print(data)
    return {
        "status": str(data),
        "status1": str(get_table_data_using_session())
    }

def get_table_data():
    result = dbactions.conn.execute(text("select * from test"))
    return result.all()

def get_table_data_using_session():
    return dbactions.session.execute(text("select * from test")).all()
