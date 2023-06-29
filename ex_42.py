# Read the note from the user
note = input("Enter the note name (e.g., C4): ")

# Extract the letter and octave from the note
letter = note[0]
octave = int(note[1])

# Define the frequency for note C in octave 4
c4_frequency = 261.63

# Calculate the frequency based on the octave using if statements
if letter == "C":
    frequency = c4_frequency / (2 ** (4 - octave))
elif letter == "D":
    frequency = c4_frequency * (2 ** (1 / 12)) / (2 ** (4 - octave))
elif letter == "E":
    frequency = c4_frequency * (2 ** (2 / 12)) / (2 ** (4 - octave))
elif letter == "F":
    frequency = c4_frequency * (2 ** (3 / 12)) / (2 ** (4 - octave))
elif letter == "G":
    frequency = c4_frequency * (2 ** (5 / 12)) / (2 ** (4 - octave))
elif letter == "A":
    frequency = c4_frequency * (2 ** (7 / 12)) / (2 ** (4 - octave))
elif letter == "B":
    frequency = c4_frequency * (2 ** (9 / 12)) / (2 ** (4 - octave))

# Display the frequency
print("The frequency of", note, "is", frequency, "Hz.")
