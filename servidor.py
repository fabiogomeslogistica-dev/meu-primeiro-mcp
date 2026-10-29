from mcp.server.fastmcp import FastMCP

mcp = FastMCP('meu-primeiro-mcp')

@mcp.tool()
def somar(a: float, b: float) -> float:
    'Soma dois numeros.'
    return a + b

@mcp.tool()
def saudacao(nome: str) -> str:
    'Cumprimenta uma pessoa pelo nome.'
    return 'Ola, ' + nome + '! Seu servidor MCP esta funcionando.'

if __name__ == '__main__':
    mcp.run()