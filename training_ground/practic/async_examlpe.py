import asyncio

async def count():
    print("Tik")
    await asyncio.sleep(1)
    print("Tok")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    asyncio.run(main())