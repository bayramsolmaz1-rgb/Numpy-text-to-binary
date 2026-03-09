import numpy as np

class DinamikModel:
    def __init__(self):
        self.vocab = {}
        self.kelime_sayisi = 0
        
    def ogren_ve_cevir(self, cumle):
        kelimeler = cumle.lower().split()
        
        for kelime in kelimeler:
            if kelime not in self.vocab:
                self.vocab[kelime] = self.kelime_sayisi
                self.kelime_sayisi += 1
                
        vektor = np.zeros(self.kelime_sayisi)
        
        for kelime in kelimeler:
            indeks = self.vocab[kelime]
            vektor[indeks] = 1
            
        return vektor, self.vocab
    
model = DinamikModel()

print("çıkmak için 'q' diyin.")

while True:
    user_input = input("\nBir cümle gir: ")
    if user_input.lower() == "q":
        break
    
    vektor, guncel_sozluk = model.ogren_ve_cevir(user_input)
    
    print(f"Sözlük Durumu: {guncel_sozluk}")
    print(f"Oluşan Vektör: {vektor}")  
