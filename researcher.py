from tavily import TavilyClient
import os

tavily = TavilyClient(api_key=os.getenv("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"))

def research_topic(topic):
    query = f"environmental impact of {topic}"
    
    results = tavily.search(query=query, search_depth="advanced")

    content = ""
    for r in results["results"]:
        content += r["content"][:500] + "\n"

    return content