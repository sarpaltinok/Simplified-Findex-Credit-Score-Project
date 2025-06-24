def kredi_notu_hesapla(
    odeme_aliskanligi_puani,  # 0-100 arası
    borc_durumu_puani,        # 0-100 arası
    kredi_kullanim_puani,     # 0-100 arası
    yeni_kredi_puani          # 0-100 arası
):
    # Her bileşenin yüzdesine göre ağırlıklı ortalama
    genel_puan = (
        odeme_aliskanligi_puani * 0.45 +
        borc_durumu_puani * 0.32 +
        kredi_kullanim_puani * 0.18 +
        yeni_kredi_puani * 0.05
    )
    
    # 0-100 ölçeğinden 0-1900 ölçeğine çevirme
    kredi_notu = int((genel_puan / 100) * 1900)
    return kredi_notu

    

def odeme_aliskanligi_puani(row):
    if row['Num_of_Delayed_Payment'] == 0:
        return 100
    elif row['Delay_from_due_date'] <= 2:
        return 70
    else:
        return 40

def borc_durumu_puani(row):
    ratio = row['Credit_Utilization_Ratio']
    if ratio < 0.3:
        return 100
    elif ratio < 0.7:
        return 70
    else:
        return 40

def kredi_kullanim_puani(row):
    if row['Num_of_Loan'] <= 1 and row['Num_Credit_Card'] <= 3:
        return 100
    elif row['Num_of_Loan'] <= 3:
        return 70
    else:
        return 40

def yeni_kredi_puani(row):
    if row['Num_Credit_Inquiries'] == 0:
        return 100
    elif row['Num_Credit_Inquiries'] <= 1:
        return 70
    else:
        return 40
    
def kategorize_et(kredi_notu):
    if not (1 <= kredi_notu <= 1900):
        raise ValueError("Kredi skoru 1 ile 1900 arasında olmalıdır.")
    
    if kredi_notu <= 699:
        return "Yüksek risk"
    elif kredi_notu <= 1099:
        return "Orta risk"
    elif kredi_notu <= 1499:
        return "Düşük risk"
    elif kredi_notu <= 1699:
        return "İyi"
    else:
        return "Çok iyi"

        
