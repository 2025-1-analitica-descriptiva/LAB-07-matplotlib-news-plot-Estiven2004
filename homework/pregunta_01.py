"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    
    # Create the plots directory if it doesn't exist
    os.makedirs("files/plots", exist_ok=True)
    
    # Read the CSV data
    df = pd.read_csv("files/input/news.csv", index_col=0)
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Plot each media type
    for column in df.columns:
        plt.plot(df.index, df[column], marker='o', linewidth=2, label=column)
    
    # Customize the plot
    plt.title("News Consumption by Media Type Over Time", fontsize=16, fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Consumption (%)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    
    # Set the y-axis to start from 0 for better visualization
    plt.ylim(0, None)
    
    # Format x-axis to show years properly
    plt.xticks(df.index[::2])  # Show every other year to avoid crowding
    
    # Tight layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the plot
    plt.savefig("files/plots/news.png", dpi=300, bbox_inches='tight')
    plt.close()
