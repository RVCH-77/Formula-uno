import fastf1 
session = fastf1.get_session(2021, 7, 'Q')
session.load()  # Esto descargará los datos del GP de Francia 2021

# 'Qualifying'
print(session.name)
# 2021-06-19 13:00:00
print(session.date)
# Información general del GP de Francia 2021
print(session.event)