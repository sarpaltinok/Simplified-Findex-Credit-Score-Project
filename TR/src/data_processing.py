import pandas as pd
from calculation import odeme_aliskanligi_puani, yeni_kredi_puani, borc_durumu_puani, kredi_kullanim_puani, kredi_notu_hesapla

columns_needed = [
    "Delay_from_due_date",           # Gecikme süresi (ödeme alışkanlığı)
    "Num_of_Delayed_Payment",        # Geciken ödeme sayısı
    "Outstanding_Debt",              # Kalan borç
    "Credit_Utilization_Ratio",      # Borç/limit oranı
    "Num_of_Loan",                   # Aktif kredi sayısı
    "Num_Credit_Card",               # Kredi kartı sayısı
    "Num_Bank_Accounts",             # Banka hesabı sayısı
    "Num_Credit_Inquiries"           # Son zamanlardaki kredi başvuruları
]

# Veriyi çek ve temizle
df = pd.read_csv("data_base/test.csv", usecols=columns_needed)
df = df.fillna(df.mean(numeric_only=True))

# Sayısal olması gereken kolonları dönüştür
df[columns_needed] = df[columns_needed].apply(pd.to_numeric, errors='coerce')

# Her satır için puanları hesapla ve kredi notunu ekle
df['Odeme_Aliskanligi_Puani'] = df.apply(odeme_aliskanligi_puani, axis=1)
df['Borc_Durumu_Puani'] = df.apply(borc_durumu_puani, axis=1)
df['Kredi_Kullanim_Puani'] = df.apply(kredi_kullanim_puani, axis=1)
df['Yeni_Kredi_Puani'] = df.apply(yeni_kredi_puani, axis=1)

df['Kredi_Notu'] = df.apply(
    lambda row: kredi_notu_hesapla(
        row['Odeme_Aliskanligi_Puani'],
        row['Borc_Durumu_Puani'],
        row['Kredi_Kullanim_Puani'],
        row['Yeni_Kredi_Puani']
    ),
    axis=1
)

# Sonuçları görter
print(df[['Kredi_Notu']].head(50))







