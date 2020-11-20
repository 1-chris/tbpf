import sqlite3

conn = sqlite3.connect('tbpf-fs.db')

c = conn.cursor()

c.execute('''CREATE TABLE filetree (index integer, path text, iscontainer bool, origin text, baselocationid ''')
c.execute('''CREATE TABLE tags (tagid integer, name text, taggroupid, integer)''')
c.execute('''CREATE TABLE taggroups (taggroupid integer, name text)''')
c.execute('''CREATE TABLE baselocations (baselocationid integer, basepath text)''')
