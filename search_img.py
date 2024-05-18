import os
import requests
from bs4 import BeautifulSoup as bs
from IPython.display import Image, display

startp= "https://fr.images.search.yahoo.com/search/images;_ylt=?p="
endp="&fr2=piv-web&fr=yfp-t"
rech=input("le nom de l'image quont rechercher . ")
rechplus = rech.replace(" ", "+")
pfinal=startp+rechplus+endp

request = requests.get(pfinal)
soup=bs(request.text,"html.parser")
images = soup.find_all('img')
for img in images:
    if img==None:
        del(images[img])
max_images=int(input("nombre d'image que l'on veut télécharger : "))
i=1
for j,img in enumerate(images[:max_images]):
        img_url = img.get('src')
        if img_url!=None:
            print(img_url)
            response = requests.get(img_url, stream=True)
            save_path=f"image{i}.png"
            i=i+1
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):  
                    file.write(chunk)
      
