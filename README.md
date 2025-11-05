# Kokoro TTS API

This is a simple API for generating TTS audio using the Kokoro model.

## Installation

```bash
source ./install.sh
```

## Usage

```bash
source ./start.sh
```

## API

```bash
http://localhost:8000/tts
```

## Request

```bash
curl -X POST http://localhost:8000/tts -H "Content-Type: application/json" -d '{"text": "Hello, world!", "voice": "af_heart", "speed": 1}'
```

## Response

```bash
{
  "graphemes": "Hello, world!",
  "phonemes": "h e l l o ,   w o r l d !",
  "b64_audio": "data:audio/wav;base64,..."
}
```
