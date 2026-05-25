import asyncio

from pydantic_ai import Agent
from pydantic_ai.capabilities import Thinking, WebSearch


async def main():
    agent = Agent(
        model="anthropic:claude-sonnet-4-6",
        instructions="Be precise and always reply in one sentence only.",
        capabilities=[Thinking(), WebSearch(local="duckduckgo")]
    )

    res = await agent.run("What was the mass of the largest meteorite found this year?")
    print(res.output)


if __name__ == "__main__":
    asyncio.run(main())
