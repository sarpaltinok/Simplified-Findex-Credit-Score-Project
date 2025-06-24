import data_processing
import visualization

def main():
    # Veriler işlenir ve kredi notları hesaplanır (data_processing.py)
    df = data_processing.df

    # Grafikler oluşturulur (visualization.py)
    visualization.df = df  
    visualization.main()    

if __name__ == "__main__":
    main()