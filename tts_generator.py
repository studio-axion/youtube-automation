from gtts import gTTS
from pathlib import Path

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

text = "Hello. This is a GitHub Actions TTS test."

tts = gTTS(text=text, lang="en")
output_path = output_dir / "test.mp3"
tts.save(str(output_path))

print(f"Generated: {output_path}")
