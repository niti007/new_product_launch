import os
from crewai import Agent
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

class ProductAnalysisAgents():
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GEMINI_API_KEY"),
            model="gemini/gemini-1.5-flash",
           # api_key=os.getenv("GROQ_API_KEY"),
           # model="groq/llama-3.3-70b-versatile"
        )

    def market_research_analyst(self, product_name):
        return Agent(
            role="Market Research Analyst",
            goal=f"""Analyze the market demand for {product_name} and suggest marketing strategies""",
            backstory="""
                Expert at understanding market demand, target audience, 
                        and competition for products like {product_name}. 
                        Skilled in developing marketing strategies 
                        to reach a wide audience.
                """,
            verbose=True,
            llm=self.llm,
            tools=[search_tool],
            max_iter=2,
        )

    def technology_expert(self,product_name):
        return Agent(
            role="Technology Expert",
            goal=f"""
                Assess technological feasibilities and requirements for producing high-quality {product_name}
                """,
            backstory="""
                Visionary in current and emerging technological trends, 
                        especially in products like {product_name}. 
                        Identifies which technologies are best suited 
                        for different business models.
                """,
            verbose=True,
            llm=self.llm,
            tools=[search_tool],
            max_iter=2,
        )

    def business_consultant(self,product_name):
        return Agent(
            role="Business Development Consultant",
            goal=f"""
                Evaluate the business model for {product_name}, 
                   focusing on scalability and revenue streams
                """,
            backstory="""
Seasoned in shaping business strategies for products like {product_name}. 
                        Understands scalability and potential 
                        revenue streams to ensure long-term sustainability
                """,
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )


























