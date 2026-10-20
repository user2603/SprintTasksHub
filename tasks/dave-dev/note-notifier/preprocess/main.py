import argparse
import asyncio


async def main(args):
    # prepares the note-notifier task
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent_workspace", required=False)
    parser.add_argument("--token_path", required=False)
    parser.add_argument("--launch_time", required=False)
    args = parser.parse_args()
    asyncio.run(main(args))
