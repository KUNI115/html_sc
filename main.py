from bs4 import BeautifulSoup
import requests as res
import pprint
import pandas as pd
import re
from pydantic import BaseModel
class Modeldata(BaseModel):
    url:str
    titile:list
    
def selection(url,data):
    judge = re.compile(r'<.*?>')
    adjust = [ re.sub(judge,'',str(i)) for i in data]
   
    #com_list = Modeldata(url,adjust) 
    pprint.pprint(adjust)
    return adjust
def scr(name_url):
    get = res.get(name_url)
    soup = BeautifulSoup(get.text, 'html.parser')
    H = ["h1","h2","h3","h4","h5","h6"]
    Hs = [ 'None' if x == None else soup.findAll(x)   for x in H ]
    cleaned_Hs = selection(name_url,Hs)
    pf = pd.DataFrame(cleaned_Hs)
    pf.to_excel("scr_date.xlsx",index=False)
if __name__ == "__main__":
    url = input("//url setup//")
    scr(url)