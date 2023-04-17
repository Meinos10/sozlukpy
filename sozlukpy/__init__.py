# Coder ReWoxi

# https://github.com/Meinos10/sozlukpy


import requests as req

class Sozluk:
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url = "https://sozluk.gov.tr/gts?ara="


    def anlam(self, kelime: str):
        header = self.header
        url = self.url
        anlam = req.get(url+str(kelime.lower()), headers=header).json()
        if anlam == {"error":"Sonuç bulunamadı"}:
            return anlam["error"]
        return anlam[0]["anlamlarListe"][0]["anlam"]

    def anlamlar(self, kelime: str, limit: int=100):
        header = self.header
        url = self.url
        anlamlar = req.get(url+str(kelime.lower()), headers=header).json()
        if anlamlar == {"error":"Sonuç bulunamadı"}:
            return anlamlar["error"]
        text = {}
        n = 1
        for t in anlamlar[0]["anlamlarListe"]:
            if n <= limit:
                text[str(n)] = t["anlam"]
                n += 1
        return text

    def ornekler(self, kelime: str, limit: int=100):
        header = self.header
        url = self.url
        ornekler = req.get(url+str(kelime.lower()), headers=header).json()
        if ornekler == {"error":"Sonuç bulunamadı"}:
            return ornekler["error"]
        text = {}
        n = 1
        for t in ornekler[0]["anlamlarListe"]:
            try:
                for o in t["orneklerListe"]:
                    if n <= limit:
                        text[str(n)] = o["ornek"]
                        n+=1
            except KeyError:
                pass
        return text
    
    def atasozleri(self, kelime: str, limit: int=100):
        header = self.header
        url = self.url
        ornekler = req.get(url+str(kelime.lower()), headers=header).json()
        if ornekler == {"error":"Sonuç bulunamadı"}:
            return ornekler["error"]
        text = {}
        n = 1
        for t in ornekler[0]["atasozu"]:
            if n <= limit:
                text[str(n)] = t["madde"]
                n+=1
        return text

