# ai-voice-assistant

A minimal voice-controlled AI assistant built with LiveKit that can answer questions and check temperature readings across different rooms/zones.

## Features

- **Voice-to-Voice Communication**: Complete speech-to-text and text-to-speech pipeline
- **Natural Conversation**: Designed for natural voice interactions with minimal latency
- **Temperature Monitoring**: Check temperature readings across 5 different zones
- **Real-time Processing**: Built on LiveKit's real-time communication platform

## Project Structure

```
ai-voice-assistant/
├── ai/                 # Virtual environment
├── main.py            # Main application entry point
├── api.py             # Temperature control functions and agent tools
├── .env               # Environment variables
└── README.md          # This file
```

## Prerequisites

- Python
- LiveKit account and API credentials
- OpenAI API key

## Setup

### 1. Clone and Navigate
```bash
git clone <repository-url>
cd ai-voice-assistant
```

### 2. Activate Virtual Environment
```bash
source ai/bin/activate  # On macOS/Linux
# or
ai\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install livekit-agents
pip install livekit-plugins-openai
pip install livekit-plugins-silero
pip install python-dotenv
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=your_livekit_server_url
OPENAI_API_KEY=your_openai_api_key
```

## Usage

### Starting the Assistant
```bash
python main.py
```

The assistant will:
1. Connect to your LiveKit room
2. Initialize speech processing components
3. Greet you as "Navi" and wait for voice commands

### Available Commands

**Temperature Queries:**
- "What's the temperature in the living room?"
- "Check bedroom temperature"
- "How warm is the kitchen?"
- "Tell me the office temperature"
- "What's the bathroom temperature?"

**Supported Zones:**
- Living Room (25°C)
- Bedroom (22°C)  
- Kitchen (20°C)
- Bathroom (30°C)
- Office (21°C)

## Architecture

### Core Components

**main.py** - Application entry point
- Handles LiveKit connection and room management
- Configures the AI agent with personality and instructions
- Manages the complete voice processing pipeline

**api.py** - Function tools and business logic
- `TemperatureZone` enum defining available rooms
- `AssistantAgentFunction` class with temperature checking capabilities
- Function decorators for LiveKit agent integration

### Voice Processing Pipeline

1. **Speech-to-Text (STT)**: OpenAI Whisper converts voice to text
2. **Language Model (LLM)**: OpenAI GPT processes and generates responses
3. **Text-to-Speech (TTS)**: OpenAI TTS converts responses back to speech
4. **Voice Activity Detection (VAD)**: Silero VAD detects when users are speaking

## Configuration

### Agent Personality
The assistant is configured as "Clare" (though introduces itself as "Navi") with these characteristics:
- Minimal and concise responses
- Voice-optimized communication
- Natural conversation flow
- Specialized in temperature monitoring

### Audio Settings
- Audio-only connection (no video)
- Interruption support for natural conversation
- Real-time voice activity detection

## Development

### Adding New Functions
To add new capabilities:

1. Create a new method in `AssistantAgentFunction`
2. Use the `@function_tool()` decorator
3. Include proper type hints and docstrings
4. Handle speech responses with `await context.session.say()`

### Extending Temperature Zones
Modify the `_temperature_zones` dictionary in `api.py`:
```python
self._temperature_zones = {
    TemperatureZone.LIVING_ROOM: 25,
    # Add new zones here
}
```

## Troubleshooting

### Common Issues

**Connection Problems:**
- Verify LiveKit credentials in `.env`
- Check network connectivity
- Ensure LiveKit server is accessible

**Audio Issues:**
- Check microphone permissions
- Verify audio device settings
- Test with different audio inputs

**API Errors:**
- Validate OpenAI API key
- Check API quota and billing
- Review error logs for specific issues

### Logging
The application includes logging for temperature control functions. Check console output for debugging information.

## Limitations

- Temperature data is currently mock/static values
- Limited to predefined room zones
- Requires stable internet connection for all AI processing
- Voice processing latency depends on OpenAI API response times

## Future Enhancements

- [ ] Integration with real IoT temperature sensors
- [ ] Additional smart home controls (lights, HVAC)
- [ ] Multi-language support
- [ ] Custom wake word detection
- [ ] Conversation history and context memory
- [ ] Visual interface for temperature dashboards

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Support

For issues related to:
- **LiveKit**: Check [LiveKit documentation](https://docs.livekit.io/)
- **OpenAI**: Review [OpenAI API documentation](https://platform.openai.com/docs)
- **Project-specific**: [Add your contact/issue tracking info]
