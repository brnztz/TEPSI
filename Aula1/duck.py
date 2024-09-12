from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()
result = ddg_search.run("Variola do macaco comparado com o covid19")
print(result)