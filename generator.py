#!/usr/bin/python
# This class handles the generation of a new song given a markov chain
# containing the note transitions and their frequencies.

from ctypes import LittleEndianStructure
from markov_chain import MarkovChain


import random
import mido

class Generator:

    def __init__(self, markov_chain):
        self.markov_chain = markov_chain

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
        with mido.midifiles.MidiFile() as midi:
            all_sugestions = []
            notes_used = []
            track = mido.MidiTrack()
            last_note = None

            get_choice = 0;
            # Generate a sequence of 30 notes
            while get_choice < 50:
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

            midi.tracks.append(track)
            midi.save(filename)

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

if __name__ == "__main__":
    ...
