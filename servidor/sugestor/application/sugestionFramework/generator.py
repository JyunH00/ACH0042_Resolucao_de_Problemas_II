#!/usr/bin/python
# This class handles the generation of a new song given a markov chain
# containing the note transitions and their frequencies.

from ctypes import LittleEndianStructure
from .markov_chain import MarkovChain

import random
import mido

class Generator:

    def __init__(self, markov_chain):
        self.markov_chain = markov_chain
        self.all_sugestions = []
        self.notes_used = []
        self.track = None
        self.last_note = None
        self.sugestions = []
        self.new_note = None
        self.midi = None

    @staticmethod
    def load(markov_chain):
        assert isinstance(markov_chain, MarkovChain)
        return Generator(markov_chain)

    def _note_to_messages(self, note):
        return [
            mido.Message('note_on', note=note.note, velocity=127,
                         time=0),
            mido.Message('note_off', note=note.note, velocity=0,
                         time=note.duration)
        ]

    def generate(self, filename):
        with mido.midifiles.MidiFile() as midi:
            notes_used = []
            track = mido.MidiTrack()
            last_note = None
            # Generate a sequence of 100 notes
            for i in range(100):
                new_note = self.markov_chain.get_next(last_note)
                notes_used.append(new_note)
                track.extend(self._note_to_messages(new_note))
            midi.tracks.append(track)
            midi.save(filename)
            print(notes_used)
    
    def generate_paused(self, filename):
        with mido.midifiles.MidiFile() as self.midi:
            all_sugestions = []
            notes_used = []
            track = mido.MidiTrack()
            last_note = None

            get_choice = 0;
            # Generate a sequence of 30 notes
            while get_choice < 10:
                if last_note is not None:
                    print("last note : "+str(last_note))

                sugestions = []
                
                for _ in range(3):
                    new_note = self.markov_chain.get_next(last_note)
                    sugestions.append(new_note)

                print(sugestions)
                
                sugestion_to_use = int(input("select the suggestion "))
                all_sugestions.append(sugestions)
                
                new_note = sugestions[sugestion_to_use]

                last_note = new_note
                notes_used.append(last_note)
                track.extend(self._note_to_messages(last_note))
                get_choice += 1

            self.midi.tracks.append(track)
            self.midi.save(filename)

            print("-----------------------------------------------")
            #print suggestions created
            print("all the suggestions given ")
            for i in range(len(all_sugestions)):
                for j in range(3):
                    print(all_sugestions[i][j])
                print()
            
            print("-----------------------------------------------")
            print("all the notes used ")
            for i in range(len(notes_used)):
                print(notes_used[i])

    def generate_paused_test(self, filename):
        
            
        self.startToGenerate()

        get_choice = 0

        while get_choice < 5:

            self.getNextSugestions(None)

            get_choice += 1


        self.saveMidi(filename)

    def startToGenerate(self):
        with mido.midifiles.MidiFile() as self.midi:
            print("Starting to generate")
            
            self.all_sugestions = []
            self.notes_used = []
            self.track = mido.MidiTrack()
            self.last_note = None

    def setSugestionToUse(self, index):
        
        sugestion_to_use = int(index)

        self.all_sugestions.append(self.sugestions)
        
        if index != "-1":
            new_note = self.sugestions[sugestion_to_use]
        else:
            new_note = self.sugestions[0]

        self.last_note = new_note
        self.notes_used.append(self.last_note)
        self.track.extend(self._note_to_messages(self.last_note))

    
    def getNextSugestions(self, last_note_used = None):

        if last_note_used == None:
            self.last_note = last_note_used
        
        if self.last_note is not None:
            print("last note : "+str(self.last_note))
        
        self.sugestions = []

        for _ in range(3):
            new_note = self.markov_chain.get_next(self.last_note)
            self.sugestions.append(new_note)
        
        return self.sugestions

        

        
    
    def saveMidi(self,filename):
        self.midi.tracks.append(self.track)
        self.midi.save(filename)
    
    def getUsedNotes(self):
        return self.notes_used

if __name__ == "__main__":
    ...
