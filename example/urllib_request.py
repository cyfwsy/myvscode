import urllib.request
with urllib.request.urlopen(\
    'https://www.jd.com/?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=106807362512_0_3eb1026604ce44a99f099d024eda1439') as f:
     print(f.read(300).decode('utf-8'))