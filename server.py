from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ping_echo")

@mcp.tool(name="ping")
def ping() -> str:
    """
    A simple ping tool that responds with 'pong'.
    This is a simple example of a tool.
    Returns:
        str: A string response indicating the server is alive
    """
    return "pong"

@mcp.tool(name="echo")
def echo(data) -> str:
    """
    A simple echo tool that responds with the same message.
    This is a simple example of a tool.
    Args:
        data (str): The input data to echo back.
    Returns:
        str: The echoed input data with a welcome message.
    """
    return data + ", bem vindo!"

if __name__ == "__main__":
    # Rodar local
    mcp.run(transport="stdio")

    # Rodar web
    # mcp.run(transport="sse", host="localhost", port=8000, debug=True)