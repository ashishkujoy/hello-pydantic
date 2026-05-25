import asyncio

from pydantic_ai import Agent

async def main():
    agent = Agent(model="anthropic:claude-sonnet-4-6")

    res = await agent.run("Hello how are you")
    print(res.output)

if __name__ == "__main__":
    asyncio.run(main())