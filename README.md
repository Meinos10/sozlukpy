# [sozlukpy](https://pypi.org/project/sozlukpy/)

A basic Turkish dictionary

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -U sozlukpy
```

## Usage

```python
from sozlukpy import Sozluk

sozluk = Sozluk()

kelime = "Bayrak"

# returns 'anlam'
sozluk.anlam(kelime)
"""
Bir milletin, belli bir topluluğun veya bir kuruluşun simgesi olarak kullanılan, renk ve biçimle özelleştirilmiş, genellikle dikdörtgen biçiminde kumaş, sancak
"""

# returns 'anlamlar'
sozluk.anlamlar(kelime)
"""
BAYRAK

1 - Bir milletin, belli bir topluluğun veya bir kuruluşun simgesi olarak kullanılan, renk ve biçimle özelleştirilmiş, genellikle dikdörtgen biçiminde kumaş, sancak
2 - Öncü
3 - Simge, sembol
4 - Baklagilllerde diğerlerinden daha üstte bulunan, daha büyük olan ve çoğunlukla başka bir renkte ve yuvarlakça olan taç yaprağı
5 - Atletizmdeki bayrak yarışında dört sporcunun elden ele geçirdiği kısa, yuvarlak sopa
6 - Gerektiğinde indirilip kaldırılan, açılıp kapatılan kol
"""

# returns 'ornekler'
sozluk.ornekler(kelime)
"""
BAYRAK

- Bayrakları bayrak yapan üstündeki kandır / Toprak eğer uğrunda ölen varsa vatandır | Mithat Cemal Kuntay
- Yeni bir sanat kuşağının bayrağıydı o. | Yusuf Ziya Ortaç
- Kız, Sinekli Bakkal'ın erkek dünyasına meydan okuyan bir bayrak gibiydi. | Halide Edip Adıvar
- Yoldan, bayrağı açık bir taksi çevirdiler. | Mahmut Yesari
"""

# returns 'atasozleri'
sozluk.atasozleri(kelime)
"""
BAYRAK

1 - bayrağı yarıya indirmek
2 - bayrak açmak
3 - bayrak çekmek (veya asmak)
4 - bayrak dikmek
5 - bayrak gibi
6 - bayrakları açmak
"""
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

[Telegram](https://t.me/ReWoxi) - [Github](https://github.com/Meinos10) - Discord: ```emree#0010```
