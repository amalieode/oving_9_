# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:37:15 2021

@author: amali
"""

class Flervalgssporsmaal():
    
    def __init__(self, sporsmaalstekst, svaralternativer):
        self.sporsmaal=sporsmaalstekst
        self.alternativer=svaralternativer
        
        self.korrekt_svar=self.sjekk_svar()
        
        
    def __str__(self):
        return(self.__sporsmaal__(), self.svaralternativer())
    
    def sjekk_svar(self):
        self.svar=int(input("Skriv inn riktig svaralternativer her:"))
        if self.svar==1:
            print("Du har svart riktig")
        else: 
                        print("Du har svart feil")

if __name__=="__main__":
    svaralternativer=list()
    svaralternativer.append("Alternativ 1: ja")
    svaralternativer.append("Alternativ 2: nei ")
    svaralternativer.append("Alternativ 3: vet ikke ")
    
Flervalgssporsmaal("Har du med id?", svaralternativer)
