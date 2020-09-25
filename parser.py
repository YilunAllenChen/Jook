st = '''Business & Sales
Engineering
Marketing
Operations'''

st = "'" + st.replace("\n", "','").replace(" ", "%20") + "'"


print(st)