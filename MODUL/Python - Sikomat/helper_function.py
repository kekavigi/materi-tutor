import matplotlib.pyplot as plt


class Bab2:
    def __init__(self):
        pass
    
    def anjing(self, A, B):
        return A+B
    
    def Plot(self, PopulasiA, PopulasiB):
        '''Plot yang digunakan untuk menampilkan perbandingan
        pertumbuhan populasi dengan metode analitik dan beda hingga'''

        # selisih solusi setiap iterasi
        Selisih = [a-b for a,b in zip(PopulasiA, PopulasiB)]

        plt.figure(figsize=(15, 6))

        # Plot grafik pertumbuhan
        plt.subplot(1,2,1)
        plt.title('Grafik Pertumbuhan')
        plt.plot(PopulasiA, label='analitik')
        plt.plot(PopulasiB, label='beda hingga')
        plt.xlabel('Hari')
        plt.ylabel('Besar Populasi')
        plt.legend()

        # Plot selisih solusi
        plt.subplot(1,2,2)
        plt.title('Grafik Selisih Solusi Pertumbuhan')
        plt.plot(Selisih, label='analitik')
        plt.xlabel('Hari')
        plt.ylabel('Besar Populasi')

        plt.show()
