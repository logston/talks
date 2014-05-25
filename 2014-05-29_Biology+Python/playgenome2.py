import random
from time import sleep

import pygame
import pygame.midi

from genomereader import genome_line_generator

GRAND_PIANO = 0


def get_note(char):
    if char == 'A':
        return 81
    elif char == 'C':
        return 72
    elif char == 'G':
        return 79
    elif char == 'T':
        return random.choice((74, 76, 77, 83))
    else:
        return random.choice((74, 76, 77, 83))


def play_chord(midi, chord, on):
    midi.set_instrument(2, 1)
    if on:
        for char in chord:
            midi.note_on(get_note(char) - 24, 100)
    else:
        for char in chord:
            midi.note_off(get_note(char) - 24, 100)


def get_duration(char):
    if char == 'A':
        return 0.25
    elif char == 'C':
        return 0.5
    elif char == 'G':
        return 0.25
    else:
        return random.choice((0.25, 0.5))    


def play_genome():
    # start pygame.midi
    pygame.midi.init()

    # Get port to send midi instructions to.
    port = pygame.midi.get_default_output_id()
    midi_out = pygame.midi.Output(port)
    try:
        
        for line in genome_line_generator:
            if line[0] == 'N':
                continue
            
            for n in range(0, 70, 7):
                chord = line[n+3:n+6]
                duration = get_duration(line[6])
                
                play_chord(midi_out, chord, True)
                for char in line[n:n+3]: 
                    midi_out.set_instrument(GRAND_PIANO, 0)
                    midi_out.note_on(get_note(char)- 12, 127)
                    sleep(duration)
                    midi_out.note_off(get_note(char) - 12, 127)
                play_chord(midi_out, chord, False)

    finally:
        del midi_out
        pygame.midi.quit()

play_genome()
