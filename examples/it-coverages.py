from wtss import *

service = wtss('http://www.esensing.dpi.inpe.br')

for cv in service:
    print(cv)