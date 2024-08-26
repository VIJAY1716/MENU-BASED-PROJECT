import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Set voice (0 for male, 1 for female)
engine.setProperty('voice', voices[1].id)

# Set speech rate
engine.setProperty('rate', 150)

# Text to be spoken
text = "Hello, this is a text-to-speech conversion using Python."

# Print the text
print(text)

# Use the TTS engine to speak the text
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
