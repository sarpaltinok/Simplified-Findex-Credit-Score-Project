# Basitleştirilmiş Findeks Kredi Notu Projesi

Bu proje, örnek finansal verilere dayalı olarak kredi notlarını hesaplayan ve görselleştiren, Findeks Kredi Notu sisteminin basitleştirilmiş bir simülasyonudur. Python ile yazılmıştır ve veri işleme için pandas, görselleştirme için matplotlib kullanır.
## Özellikler

- **Veri İşleme:** Finansal verileri bir CSV dosyasından okur ve temizler.
- **Kredi Notu Hesaplama**  Her birey için ödeme alışkanlıkları, borç durumu, kredi kullanımı ve yeni kredi hareketlerine göre kredi notu hesaplar.
- **Göreselleştirme:** Kredi notu dağılımı ve risk kategorileri için histogram ve pasta grafik görselleri sunar.
## Proje yapısı

```
src/
├── main.py              # Projenin başlangıç noktası
├── data_processing.py   # Veri yükleme, temizleme ve not hesaplama işlemleri
├── calculation.py       # Notlandırma mantığı ve risk kategorilendirmesi
├── visualization.py     # Sonuçlar için görselleştirme
data_base/
└── test.csv             # Örnek veri dosyası (dahil değildir)
```

## Başlarken

### Gereksinimler

- Python 3.8+
- pandas
- matplotlib

Bağımlılıkları yüklemek için:

```bash
pip install pandas matplotlib
```

### Kullanım

1. Gerekli sütunlara sahip veri dosyanızı "test.csv" olarak yerleştirin:

    - `Delay_from_due_date`
    - `Num_of_Delayed_Payment`
    - `Outstanding_Debt`
    - `Credit_Utilization_Ratio`
    - `Num_of_Loan`
    - `Num_Credit_Card`
    - `Num_Bank_Accounts`
    - `Num_Credit_Inquiries`

2. Projeyi çalıştırın:

```bash
python src/main.py
```

3. Hesaplanan kredi notlarını ve oluşturulan görselleri görüntüleyin.

## Kredi Notu Hesaplama

Kredi notu, dört bileşenin ağırlıklı toplamı olarak hesaplanır:

- **Ödeme Alışkanlığı Puanı** (45%)
- **Borç Durumu Puanı** (32%)
- **Kredi Kullanım Puanı** (18%)
- **Yeni Kredi Puanı** (5%)

Her bileşen 0 ile 100 arasında puanlanır ve nihai not 0–1900 aralığına ölçeklenir.

## Lisans

Bu proje eğitim amaçlıdır.

---

**Not:** Bu model basitleştirilmiştir ve gerçek finansal kararlar için kullanılmamalıdır.
