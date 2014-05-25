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


def play_genome():
    # start pygame.midi
    pygame.midi.init()

    # Get port to send midi instructions to.
    port = pygame.midi.get_default_output_id()
    midi_out = pygame.midi.Output(port, 0)
    print ("using output_id :%s:" % port) 
    print ("Output is %s" % midi_out)
    try:
        midi_out.set_instrument(GRAND_PIANO)
        
        for line in genome_line_generator:
            if line[0] == 'N':
                continue
            for char in line:
                if char == '-':
                    continue
                note = get_note(char)
                midi_out.note_on(note, 127)
                sleep(0.5)
                midi_out.note_off(note, 127)

    finally:
        del midi_out
        pygame.midi.quit()

play_genome()
