from Cinema import Cinema 

def getCinemaTable(c, cinema_id):
    query = """
            SELECT * FROM cinemas WHERE (((cinemas.cinema_id)="""+ str(cinema_id) + "));"
    c.execute(query)
    table = c.fetchone()
    return table

def getCinemaObject(c, cinema_id):
    cin_row = getCinemaTable(c, cinema_id)
    cin = Cinema(id=cin_row[0], morn_LH=cin_row[3], after_LH=cin_row[6], night_LH=cin_row[9])
    return cin
