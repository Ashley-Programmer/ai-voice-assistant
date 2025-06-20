import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents import Agent, AgentSession
import livekit.plugins.openai as openai
import livekit.plugins.silero as silero
from api import AssistantAgentFunction


load_dotenv()

async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY) # only audio connection is allowed, no video
    
    # agent/assistant with instructions
    agent = Agent(
        instructions=(
            "You are Clare, a minimal voice assistant created by Livekit. Your interface with users will be voice. "
            "You should use short and concise responses using a voice, avoiding usage of complex punctuation. "
            "Your goal is to answer the user's questions and assist them with their problems in a way that is as natural as possible."
            "You can help users check temperatures in diverse zones/rooms."
        )
    )
    
    agent_function = AssistantAgentFunction()
    
    # Create and start the agent/assistant session session
    session = AgentSession(
        stt=openai.STT(), # Speech-to-Text (converts voice to text)
        llm=openai.LLM(), # Large Language Model (the "brain")
        tts=openai.TTS(), # Text-to-Speech (converts text back to voice)
        vad=silero.VAD.load(),  # Voice Activity Detection (knows when user is speaking)
        agent_function=agent_function,
    )
    
    await session.start(room=ctx.room, agent=agent)
    
    await asyncio.sleep(1)
    await agent.say("Hi, I'm Navi. How may I help you?", allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))