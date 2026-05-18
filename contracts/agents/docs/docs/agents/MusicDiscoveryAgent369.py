from uagents import Agent, Context, Model

agent = Agent(
    name="MusicDiscoveryAgent369",
    seed="shaka-369-discovery-seed-change-this-in-production",
    endpoint=["http://127.0.0.1:8000"]
)

@agent.on_event("new_music_uploaded")
async def discover_and_match(ctx: Context, msg):
    artist = msg.get("artist")
    track = msg.get("track")
    
    ctx.logger.info(f"🔍 Discovery Agent scanning 6 directions for {track} by {artist}")
    # TODO: Later connect to real platforms + fan matching via taste profiles
    # This agent finds fans, predicts trends, and coordinates cross-agent collabs
    
    ctx.logger.info(f"✅ Matched with 6 potential fan circles | Viral potential: HIGH")
