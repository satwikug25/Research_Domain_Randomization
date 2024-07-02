from pydub import AudioSegment
import os

input_directory = "/Users/satwikm/Desktop/domain_randomization/Ambulance/"
output_directory = "/Users/satwikm/Desktop/domain_randomization/Output/"
background_sound_file = '/Users/satwikm/Desktop/domain_randomization/60570__robinhood76__00388-wet-traffic-1.wav'


background_sound = AudioSegment.from_file(background_sound_file, format='wav')

for filename in os.listdir(input_directory):
    print(filename)
    if filename.endswith(".WAV"):
        print(filename)
        # Load ambulance call recording
        call_audio = AudioSegment.from_file(os.path.join(input_directory, filename), format='wav')

        # Adjust volume levels or apply other effects if needed
        background_sound = background_sound - 10

        if len(call_audio) != len(background_sound):
    # Adjust audio2 to match length of audio1 (example: truncate or extend)
            background_sound = background_sound[:len(call_audio)]  # truncate or extend as needed

        # Overlay background sound onto call audio
        mixed_audio = call_audio.overlay(background_sound)

        # Export mixed audio to output directory
        output_filename = os.path.join(output_directory, filename)
        mixed_audio.export(output_filename, format='wav')

        print(f"Processed {filename}")

print("Batch processing complete.")