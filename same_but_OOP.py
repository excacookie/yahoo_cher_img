import os
import requests
from bs4 import BeautifulSoup as bs
#for jupyter notebook
from IPython.display import Image, display

class scrapyahooimg():
    def finalprompt(self):
        startp= "https://fr.images.search.yahoo.com/search/images;_ylt=?p="
        endp="&fr2=piv-web&fr=yfp-t"
        try:
            rech=input("le nom de l'image quont rechercher . ")
            rechplus = rech.replace(" ", "+")
            pfinal=startp+rechplus+endp
        except:
            print("apprend a écrire")
        return pfinal
    def request(self,prompt):
        request = requests.get(prompt)
        return request
    def soup(self,request):
        soup=bs(request.text,"html.parser")
        images = soup.find_all('img')
        return images
    def downloadimg(self,images):
        count=0
        for img in images:
            if img.get('src')==None:
                del(images[count])
            count=count+1
        max_images=int(input("nombre d'image que l'on veut télécharger : "))
        i=1
        for j in range(max_images):
            img_url = images[j].get('src')
            print(img_url)
            response = requests.get(img_url, stream=True)
            save_path=f"image{i}.png"
            i=i+1
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
        return i
    #for jupyter notebook
    def printimg(self,nimage):
        limgpath = []
        for k in range(1,nimage):
            limgpath.append(f'image{k}.png')
    
        for imgpath in limgpath:
            display(Image(filename=imgpath))

obj=scrapyahooimg()
prompt=obj.finalprompt()
request=obj.request(prompt)
soup=obj.soup(request)
nimage=obj.downloadimg(soup)
#for jupyter notebook
obj.printimg(nimage)
