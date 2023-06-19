import requests
import bs4

results=requests.get("https://en.wikipedia.org/wiki/Monkey")
soup=bs4.BeautifulSoup(results.text, "lxml")


print(soup.select('.image-section')[0])
print("======determine the stirng to download=======================")
getSrc=soup.select('.image-section')[0]
print(getSrc)
print("Getting image from website +++++++++++++++++++++++++++++++++++")
imag=requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Bonnet_macaque_%28Macaca_radiata%29_Photograph_By_Shantanu_Kuveskar.jpg/220px-Bonnet_macaque_%28Macaca_radiata%29_Photograph_By_Shantanu_Kuveskar.jpg")

f=open('monkey.jpg','wb')
f.write(imag.content)
f.close
print("Saved+++++++++++++++++++++++++++++")