import csv

# csv header
fieldnames = ['URL','name','target_price']

# csv data
rows = [
    {'URL': 'https://www.amazon.in/Samsung-Galaxy-Celestial-Black-Storage/dp/B085J1CPCW/ref=sr_1_1?crid=1CSB8OU6DI6BY&dchild=1&keywords=galaxy+m51&qid=1621779803&s=electronics&sprefix=galaxy%2Celectronics%2C565&sr=1-1',
        'name' : 'Samsung Galaxy M51',
        "target_price" : 21000 },
    {'URL': 'https://www.amazon.in/dp/B08VB2CMR3/ref=syn_sd_onsite_desktop_51?psc=1&uh_it=57ac9a7088255ba0e9535b5b4aa606ae_CT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWkpHNTZKWDhMOVlFJmVuY3J5cHRlZElkPUEwNDc1MTk5UlVKT0VHUlkwNzhVJmVuY3J5cHRlZEFkSWQ9QTAwODU0MzMzRE9TMTJYSzZOVUhHJndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl',
        'name' : 'OPPO A74 5G',
        "target_price" : 18000},
    {'URL': 'https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HGGYWL6/ref=sr_1_1?dchild=1&keywords=galaxy+m31&qid=1621781371&s=electronics&sr=1-1',
        'name' : 'Samsung Galaxy M31',
        "target_price" : 15000},
    {'URL': 'https://www.amazon.in/dp/B08WC387F8/ref=pc_mcnc_merchandised-search-12_?pf_rd_s=merchandised-search-12&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=F5QE7F1CRZX55D16MM08&pf_rd_p=e7024920-7ae9-40db-97a4-252e126f2590',
        'name' : 'Samsung Galaxy A12',
        "target_price" : 12000},
    {'URL': 'https://www.amazon.in/dp/B08VB6MV2Y/ref=pc_mcnc_merchandised-search-12_?pf_rd_s=merchandised-search-12&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=0VNQ8VAQ2B4J9PH1PMHE&pf_rd_p=e7024920-7ae9-40db-97a4-252e126f2590',
        'name' : 'Samsung A32',
        "target_price" : 20000}
]

with open('product_to_track.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


import pandas as pd

df = pd.read_csv('product_to_track.csv')
print(df)