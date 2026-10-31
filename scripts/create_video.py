
import subprocess

# Get narration duration
result = subprocess.run([
    "ffprobe", "-v", "error",
    "-show_entries", "format=duration",
    "-of", "default=noprint_wrappers=1:nokey=1",
    "output/voice.wav"
], capture_output=True, text=True, check=True)

audio_duration = float(result.stdout.strip())

transition = 0.5
image_duration = (audio_duration + 4 * transition) / 5

command = ["ffmpeg", "-y"]

for i in range(1, 6):
    command += [
        "-loop", "1",
        "-t", str(image_duration),
        "-i", f"assets/images/scene{i}.jpg"
    ]

command += ["-i", "output/voice.wav"]

filters = []

for i in range(5):
    filters.append(
        f"[{i}:v]scale=1920:1080:"
        f"force_original_aspect_ratio=decrease,"
        f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
        f"fps=30,setsar=1,format=yuv420p,settb=AVTB[v{i}]"
    )

previous = "[v0]"

for i in range(1, 5):
    output = f"[x{i}]"
    offset = i * (image_duration - transition)

    filters.append(
        f"{previous}[v{i}]"
        f"xfade=transition=fade:duration={transition}:"
        f"offset={offset}{output}"
    )

    previous = output

subprocess.run([
    *command,
    "-filter_complex", ";".join(filters),
    "-map", previous,
    "-map", "5:a",
    "-c:v", "libx264",
    "-c:a", "aac",
    "-pix_fmt", "yuv420p",
    "-shortest",
    "output/test_video.mp4"
], check=True)

print("Crossfade documentary video created!")
