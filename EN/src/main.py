import data_processing
import visualization

def main():
    # Process data and calculate credit scores (data_processing.py)
    df = data_processing.df

    # Generate visualizations (visualization.py)
    visualization.df = df  
    visualization.main()    

if __name__ == "__main__":
    main()