import os
import time
from crewai import Crew
from langchain_groq import ChatGroq
from backend.agents import ProductAnalysisAgents
from backend.tasks  import Productanalysistask
from dotenv import load_dotenv

# Setup environment
load_dotenv()


def analyze_product(product_name):
    # 1. Create agents
    agents = ProductAnalysisAgents()
    market_analyst = agents.market_research_analyst(product_name)
    tech_expert = agents.technology_expert(product_name)
    business_consultant = agents.business_consultant(product_name)

    # 2. Create tasks
    tasks = Productanalysistask()

    # Create individual tasks
    market_research_task = tasks.market_research_analyst(
        agent=market_analyst,
        product_name=product_name
    )

    tech_assessment_task = tasks.technology_expert(
        agent=tech_expert,
        product_name=product_name
    )

    business_analysis_task = tasks.business_consultant(
        agent=business_consultant,
        product_name=product_name
    )

    # Setup Crew
    crew = Crew(
        agents=[
            market_analyst,
            tech_expert,
            business_consultant
        ],
        tasks=[
            market_research_task,
            tech_assessment_task,
            business_analysis_task
        ],
        max_rpm=29  # Rate limit for API calls
    )

    # Kick off the crew and measure time
    print(f"\nStarting analysis for {product_name}...")
    start_time = time.time()
    results = crew.kickoff()
    end_time = time.time()

    # Print results and metrics
    elapsed_time = end_time - start_time
    print(f"\nAnalysis completed in {elapsed_time:.2f} seconds.")
    print("Crew usage metrics:", crew.usage_metrics)

    return results


if __name__ == "__main__":
    # Get product name from user
    product_name = input("Enter the product name you want to analyze: ")

    # Run the analysis
    try:
        results = analyze_product(product_name)

        # Display results
        print("\n=== Analysis Results ===")
        for i, result in enumerate(results, 1):
            print(f"\nReport {i}:")
            print(result)
            print("\n" + "=" * 50)

    except Exception as e:
        print(f"An error occurred: {str(e)}")