import sys
import midi

def main(argv):
    file_name = argv[0]
    pattern = midi.read_midifile(file_name)
    midi_track = pattern[1]
    time = 0
    notes = []
    for event in midi_track:
        time += event.tick * (500.0/480.0)
        if isinstance(event, midi.events.NoteOnEvent):
            notes.append({'time': time, 'note': event.data[0]})
    phrases = []
    for n in range(len(notes) - 5):
        if notes[n]['note'] == 66 and notes[n+1]['note'] == 75 and notes[n+2]['note'] == 73 and notes[n+3]['note'] == 70 and notes[n+4]['note'] == 82 and notes[n+5]['note'] == 78:
            phrases.append(int(notes[n+5]['time'] - notes[n]['time']))
    print phrases

if __name__ == "__main__":
    main(sys.argv[1:])
