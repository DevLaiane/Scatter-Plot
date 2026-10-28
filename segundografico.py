import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


caminho_csv = "/home/laiane/Documentos/SegundoG/opt-clsc-th-data.csv"
pdf_saida = "/home/laiane/Documentos/SegundoG/graficos_scatter.pdf"

data = pd.read_csv(caminho_csv)

data['ΔET[%]'] = data['ΔET[%]'].str.replace('%', '').astype(float)
data['ΔPSNR [db]'] = data['ΔPSNR [db]'].astype(float)


with PdfPages(pdf_saida) as pdf:
  
    configs = data['Config'].unique()
    qps = data['QP'].unique()
    
    for config in configs:
        for qp in qps:
          
            subset = data[(data['Config'] == config) & (data['QP'] == qp)]
            
           
            plt.figure(figsize=(8, 6))
            plt.scatter(subset['ΔET[%]'], subset['ΔPSNR [db]'], color='blue', label='Dados')
            
       
            plt.xticks(ticks=[-75.0, -50.0, -25.0], labels=['-75.0%', '-50.0%', '-25.0%'])
            plt.yticks(ticks=[0.0, 2.0, 4.0, 6.0], labels=['0.0000', '2.0000', '4.0000', '6.0000'])
            plt.xlim(-80, -20) 
            plt.ylim(-1, 7)    
            
            
            plt.title(f"Config: {config}, QP: {qp}")
            plt.xlabel("ΔET [%]")
            plt.ylabel("ΔPSNR [dB]")
            plt.grid(True)
            plt.legend()
            
           
            pdf.savefig()  
            plt.close()


