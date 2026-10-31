import subprocess
from pathlib import Path

script = """
Welcome to our documentary channel.
Today, we explore something extraordinary.
"""

output = Path("output/voice.wav")
output.parent.mkdir(exist_ok=True)

subprocess.run(
    [
        "piper",
        "--model", r"C:\Users\sunet\en_US-lessac-medium.onnx",
        "--output_file", str(output)
    ],
    input=script,
    text=True,
    check=True
)

print(f"Voice generated: {output}")