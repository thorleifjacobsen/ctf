import mido
for msg in mido.MidiFile('oilerstrack.mid'):
    if msg.is_meta:
        print("\n"+str(msg))
    if not msg.is_meta and msg.type == 'note_on':
        print(chr(msg.note), end = '')