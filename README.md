# STAJ22002
Sentiment Analysis ML Yaz Zorunlu Staj

:information_source: **Dersin Kodu:** [STAJ22002](https://ebp.klu.edu.tr/Ders/dersDetay/STAJ22002/716026/tr)  
:information_source: **Dersin Adı:** [MESLEK STAJI-II(20 İŞ GÜNÜ)](https://ebp.klu.edu.tr/Ders/dersDetay/STAJ22002/716026/tr)  
  
---

## Grup Bilgileri

| Öğrenci No  | Adı Soyadı                | Bölüm          		       | Grup Üyelerinin Github Profilleri              |
|------------ |---------------------------|------------------------- |------------------------------------------------|
| 1200505063  |  Halil Şafak Şimşek  			| Yazılım Mühendisliği     | [Github](https://github.com/Kerevizodunu2000)  |

---

## Proje Açıklaması

 Yaz zorunlu stajimda geliştirmiş olduğum makine öğrenmesi projesi. Cümle üzerinde duygu analizi yapılması amaçlanmaktadır. Proje kapsamında geliştirilen modellerin başarı oranları ve performans metrikleri detaylı bir şekilde değerlendirilecek, en etkili modelin belirlenmesi hedeflenmektedir. Kullanılan veri seti huggin face üzerinden elde edilmiştir 492.782 label hazırlanmış %10'u test için ayrılmıştır. Pozitif, negatif, nötr olmak üzere 3 farklı alanda labellama işlemi yapılmıştır. Bu veriseti , farklı kaynaklardan derlenmiş pozitif , negatif ve nötr sınıflardan örnekler içerir. Nötr cümleler wikipedia datasından alınmıştır. Ek olarak bazı rastgele inputlar nötr olarak eklenmiştir. Örneğin: "Lorem ipsum dolor sit amet.". [Hugging Face Sitesine Ulaşmak İçin Tıklayınız.](https://huggingface.co/datasets/winvoker/turkish-sentiment-analysis-dataset)
 
## Proje Dosya Yapısı

- **/Binovist  Sentiment Analysis**
  - **/src**
    - `LinearSVM_Pytorch.ipynb`
    - `LogicticRegresyon_Tam_Veri.ipynb`
    - `main.ipynb`
    - `CNN80_20.ipynb`
    - `MineModel_Pytorch.ipynb`
    - `Navie Bayes.ipynb`
    - `SVM.ipynb`
  - **/data**
    - `Beyaz Perde 10k data`
    - `Hepsiburada Dataset 492k(%10 test)`
    - `Magza Yorumları Analiz 11 k`
  - **/trstop-master**
  - **`README.md`**

## Kullanım

<ol style='list-style-type:number' >
  <li>Veriler Google Drive'a yüklenir (<a href='https://drive.google.com/drive/folders/1s9wX0R9lhYuWGbWR7t-2ZM8HHKQxZsKF?usp=drive_link'>Verileri indirmek için tıklayın</a>) </li>
  <li>Google Colab açılır</li>
  <li>ipynb dosyaları içeri aktarılır</li>
  <li>Adım adım kod satırları çalıştırılır</li>
</ol>



## İletişim

- Halil Şafak Şimşek         - halil_tafak@hotmail.com / 1200505063@ogr.klu.edu.tr

