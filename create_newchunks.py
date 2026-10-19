import whisper
import json
import os

model = whisper.load_model("large-v2")

audio_folder = r"D:\2025 video\audios"
json_folder = r"D:\2025 video\jsons"

os.makedirs(json_folder, exist_ok=True)

audios = os.listdir(audio_folder)

for audio in audios:
    if audio.lower().endswith((".mp3", ".wav", ".m4a")):
        number = audio.split(" ")[0]
        title = os.path.splitext(audio)[0]

        print(number, title)

        result = model.transcribe(
            audio=os.path.join(audio_folder, audio),
            language="hi",
            task="translate",
            word_timestamps=False
        )

        chunks = []

        for segment in result["segments"]:
            chunks.append({
                "number": number,
                "title": title,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })
is farmer 
        chunks_with_metadata = {
            "chunks": chunks,
            "text": result["text"]
        }

        output_file = os.path.join(json_folder, f"{title}.json")

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(chunks_with_metadata, f, ensure_ascii=False, indent=4)

        print("Saved:", output_file)