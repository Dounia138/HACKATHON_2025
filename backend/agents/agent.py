from crewai import Agent
from web_crawler import start_crawling
from llm_rag import ask_ai

class LeaderAgent(Agent):
    def assign_tasks(self, query):
        
        web_agent = WebCrawlingAgent()
        summary_agent = SummarizationAgent()
        structuring_agent = ContentStructuringAgent()
        
        web_data = web_agent.run(query)
        summary = summary_agent.run(web_data)
        return structuring_agent.run(summary)

class WebCrawlingAgent(Agent):
    def run(self, query):
        return start_crawling(query)

class SummarizationAgent(Agent):
    def run(self, text):
        return f"Résumé : {text[:300]}..."

class ContentStructuringAgent(Agent):
    def run(self, summary):
        return f"Article structuré :\n\n{summary}"
