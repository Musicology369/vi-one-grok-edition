from uagents import Agent, Context, Model
# Onda integration for real-time micropayments
# from onda_sdk import OndaClient  # we'll add this later when you run it

agent = Agent(
    name="RoyaltyDistributionAgent369",
    seed="shaka-369-musicology-seed-change-this-in-production",
    endpoint=["http://127.0.0.1:8000"]  # local for testing
)

# This is the event that fires when Onda detects a new stream/listen
@agent.on_event("stream_detected")
async def handle_royalty(ctx: Context, msg):
    total_amount = msg.get("amount", 0)
    artist_wallet = msg.get("artist_wallet")
    
    artist_share = int(total_amount * 0.9630)   # 96.30% to creator
    platform_fee = int(total_amount * 0.0369)   # 3.69%
    burn_amount = int(total_amount * 0.0001)    # 0.01% burn
    
    ctx.logger.info(f"🎵 Stream detected! Paying {artist_share} USDC to artist {artist_wallet}")
    
    # TODO: Later we connect real Onda USDC transfer here
    # await OndaClient().send_usdc(artist_wallet, artist_share)
    
    ctx.logger.info(f"✅ 96.30% paid | 3.69% platform | 0.01% burned → Circle complete!")
