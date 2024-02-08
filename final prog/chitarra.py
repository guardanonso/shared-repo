import matplotlib.pyplot as plt

def draw_guitar_fretboard():
    # Disegna il manico della chitarra
    plt.figure(figsize=(12, 2))
    plt.plot([0, 24], [0, 0], color='black', linewidth=5)  # Lunghezza del manico della chitarra

    # Disegna le linee verticali per rappresentare i tasti
    for i in range(24):
        plt.plot([i, i], [0, 1], color='black')

    # Etichette dei tasti
    for i in range(24):
        plt.text(i + 0.5, -0.2, str(i + 1), fontsize=10, ha='center')

    # Rimuovi assi
    plt.axis('off')

def draw_triad(root_note, triad_type):
    # Mappa delle note sulla tastiera della chitarra
    notes_mapping = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5,
        'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }

    # Triadi principali
    triad_intervals = {
        'major': [0, 4, 7],
        'minor': [0, 3, 7],
        'augmented': [0, 4, 8],
        'diminished': [0, 3, 6]
    }

    # Calcola le note della triade
    root_index = notes_mapping[root_note]
    triad_intervals = [root_index + interval for interval in triad_intervals[triad_type]]

    # Disegna i cerchi per rappresentare le note della triade sulla tastiera
    for note_index in triad_intervals:
        plt.scatter(note_index, 0, color='red', s=100)

# Esempio di utilizzo
draw_guitar_fretboard()
draw_triad('C', 'major')

plt.show()