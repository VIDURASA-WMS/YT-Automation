# YT-Automation

A free Python-based documentary video automation project.

## Features
- AI voice generation using Piper TTS
- Image-based documentary scenes
- Automatic video creation using FFmpeg
- Smooth crossfade transitions
- 1080p video output

## Requirements
- Python 3.10+
- FFmpeg
- Piper TTS

## Setup

Install dependencies:

    pip install -r requirements.txt

Download a Piper voice model and update its path in scripts/generate_voice.py.

## Usage

Generate narration:

    python scripts/generate_voice.py

Create video:

    python scripts/create_video.py

Generated files are saved in the output folder.

## Project Structure

    YT-Automation/
    +-- scripts/
    +-- assets/
    ¦   +-- images/
    +-- output/
    +-- requirements.txt
    +-- README.md
    +-- .gitignore
