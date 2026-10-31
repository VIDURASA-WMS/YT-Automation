# AI Agent Instructions – YT-Automation

## Project Goal
Build a free, AI-assisted automation system for creating 5–10 minute documentary-style YouTube videos.

## Project Structure
- scripts/: Python automation scripts.
- assets/images/: Documentary images.
- output/: Generated audio and videos.
- requirements.txt: Python dependencies.

## Current Features
- Piper TTS narration generation.
- FFmpeg video generation.
- 1080p video output.
- Smooth image crossfade transitions.

## Development Rules
1. Keep the system free or open-source wherever possible.
2. Use Python for automation.
3. Use FFmpeg for video processing.
4. Preserve existing working functionality.
5. Do not delete user assets or generated outputs.
6. Keep large media files and AI models out of Git.
7. Explain changes before modifying important scripts.
8. Test scripts after making changes.

## Environment
- Windows 10/11.
- Python.
- FFmpeg.
- Piper TTS.

## Execution
Generate narration:
python scripts/generate_voice.py

Generate video:
python scripts/create_video.py
