import asyncio
from app.llm.factory import get_llm


async def main():

    llm = get_llm()
    messages = [
        {
            "role": "user",
            "content": "Explain me what API Interface is in 3 simple lines"
        }
    ]

    response = await llm.generate(messages=messages)

    print("RESPONSE {}".format(response))


if __name__ == "__main__":
    print("\nSERVER STARTING: \n")
    asyncio.run(main())
    print("\nSERVER Terminated: \n")
