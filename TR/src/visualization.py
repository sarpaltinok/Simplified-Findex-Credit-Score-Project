import matplotlib.pyplot as plt
import data_processing
from calculation import kategorize_et

df = data_processing.df

def main():
    # Kredi Notu Dağılımı
    plt.hist(df['Kredi_Notu'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Kredi Notu Dağılımı')
    plt.xlabel('Kredi Notu')
    plt.ylabel('Kişi Sayısı')
    plt.show()

    # Kredi Notu Kategorilerine Göre Pasta Grafiği
    df['Kategori'] = df['Kredi_Notu'].apply(kategorize_et)
    category_counts = df['Kategori'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(
        category_counts,
        labels=category_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=['#ff9999','#ffcc99','#99ff99','#66b3ff','#c2c2f0']
    )
    plt.title('Kredi Notu Kategorilerine Göre Dağılım')
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()