from google.cloud import texttospeech

def text_to_speech(text, filename='audio.mp3'):
    client = texttospeech.TextToSpeechClient()

    # Text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Select the language and voice
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Set the audio configuration
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    # Perform the synthesis
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # Save the audio to a file
    with open(filename, "wb") as out:
        out.write(response.audio_content)
    print(f"Audio saved as {filename}")

if __name__ == '__main__':
    # Example usage:
    text = "This is a test text to convert to speech."
    text_to_speech(text, 'audio.mp3')
