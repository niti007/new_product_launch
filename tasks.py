from crewai import Task


class Productanalysistask():
    def market_research_analyst(self,agent,product_name):
        return Task(
            description=f"""
Analyze the market demand for {product_name}. Current month is Jan 2024.
                          Write a report on the ideal customer profile and marketing 
                          strategies to reach the widest possible audience. 
                          Include at least 10 bullet points addressing key marketing areas.
            """,
            agent=agent,
            expected_output="A detailed market research report with customer profile and marketing strategies",
            async_execution=True,
        )

    def technology_expert(self, agent, product_name):
        return Task(
            description=f"""
                        Assess the technological aspects of manufacturing 
                        high-quality {product_name}. Write a report detailing necessary 
                        technologies and manufacturing approaches. 
                        Include at least 10 bullet points on key technological areas
            """,
            expected_output="A comprehensive technology assessment report with manufacturing requirements",
            agent=agent,
        )

    def business_consultant(self, agent, product_name):
        return Task(
            description=f"""
                        Summarize the market and technological reports 
                        and evaluate the business model for {product_name}. 
                        Write a report on the scalability and revenue streams 
                        for the product. Include at least 10 bullet points 
                        on key business areas. Give Business Plan, 
                        Goals and Timeline for the product launch. Current month is Jan 2024
            """,
            expected_output="A complete business analysis report with scalability assessment and launch timeline",
            agent=agent,
        )