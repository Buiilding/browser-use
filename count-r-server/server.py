from mcp.server.fastmcp import FastMCP
import time
import signal 
import sys


def signal_handler(sig, frame):
    print("Shutting down gracefully")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

mcp = FastMCP(
        name = "count-r",
        host = "127.0.0.1",
        port = 5000,
        timeout=30
)

@mcp.tool()
def count_r(word : str) -> int:
    try: 
        if not isinstance(word, str):
            return 0 
        return word.lower().count("r")
    except Exception as e:
        print(f"Error in count_r: {e}")
        return 0
    
if __name__ == "__main__":
    try:
        print("Starting MCP Server count-r on 127.0.0.1 port 5000")
        mcp.run()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)