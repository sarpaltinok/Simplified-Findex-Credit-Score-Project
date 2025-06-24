import matplotlib.pyplot as plt
import data_processing
from calculation import categorize

df = data_processing.df

def main():
    # Credit Score Distribution
    plt.hist(df['Credit_Score'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Credit Score Distribution')
    plt.xlabel('Credit Score')
    plt.ylabel('Number of People')
    plt.show()

    # Pie Chart by Credit Score Categories
    df['Category'] = df['Credit_Score'].apply(categorize)
    category_counts = df['Category'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(
        category_counts,
        labels=category_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=['#ff9999','#ffcc99','#99ff99','#66b3ff','#c2c2f0']
    )
    plt.title('Distribution by Credit Score Categories')
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()