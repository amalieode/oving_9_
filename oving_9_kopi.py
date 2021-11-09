# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:57:53 2021

@author: amali
"""

import random 
from oving8bb import Flervalgssporsmaal

def finn_sporsmaal(file):
    sporsmaal = []
    for line in file: 
        line.strip()
        sporsmaal_idx = line.find(":")
        korrekt_idx = line.find(":", sporsmaal_idx + 1)
        
        sporsmaal = line[0 : sporsmaal_idx]
        korrekt = line[sporsmaal_idx + 1: korrekt_idx]
        alternativer = line[korrekt_idx + 1: -1]
        alternativer = alternativer.strip (" ")
        
        alternativer = alternativer.strip("[")
        alternativer = alternativer.strip("]")
        
        alternativer = alternativer.split(",")
        
        sporsmaal.append(Flervalgssporsmaal(sporsmaal, alternativer, int(korrekt)))
    return sporsmaal 

class Player(): 
    def __init__(self, name):
        self.name = name 
        self.points = 0
        
    def increase_points(self):
        self.points += 1
        
    def __str__(self):
        return self.name + "-> score: " + str(self.points)
    
if __name__=='__main__':
    f = open("sporsmaalsfil.txt")
    questions = finn.sporsmaal(f)
    
    num_players = int(input("Antall spillere: "))
    players = []
    for i in range(num_players):
        players.append(Player(input("Navn spiller " + str(i + 1) + ": ")))
        
    current_player = random.randint(0, num_players - 1)
    
    for question in questions: 
        if (current_player >= len(players)):
            current_player = 0
        
        player = players[current_player]
        
        print(player)
        print(question)
        
        svar = int(input("Skriv inn svar: "))
        if (question.sjekk_svar(svar)):
            print("Riktig")
            player.increase_points()
        else:
            print("feil")
            print("Korrekt svar: ", (quesion.riktig_svar()))
            
        current_player += 1 
        
    print("Resultater:\n")
    for player in players: 
        print(player)
        