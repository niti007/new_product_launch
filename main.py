import streamlit as st
import time
from crewai import Crew
from langchain_groq import ChatGroq
from backend.agents import ProductAnalysisAgents
from backend.tasks import Productanalysistask
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
    start_time = time.time()
    results = crew.kickoff()
    end_time = time.time()

    # Print results and metrics
    elapsed_time = end_time - start_time
    usage_metrics = crew.usage_metrics

    return results, elapsed_time, usage_metrics

def display_results(results):
    for i, result in enumerate(results, 1):
        st.markdown(f"### Report {i}")
        try:
            # Assuming the tuple structure is (report_type, report_content)
            if isinstance(result, tuple) and len(result) > 1:
                report_type, report_content = result
                if report_type == 'raw':  # Adjust as per the actual tuple structure
                    st.markdown(report_content, unsafe_allow_html=True)
                else:
                    st.write(f"Type: {report_type}\nContent: {report_content}")
            else:
                st.write(result)
        except Exception as e:
            st.error(f"Failed to display report {i}: {e}")

def main():
    st.title("Product Analysis Dashboard")

    # Input section
    product_name = st.text_input("Enter the product name you want to analyze:", "")
    if st.button("Analyze Product"):
        if not product_name:
            st.error("Please enter a product name before starting the analysis.")
        else:
            st.info(f"Starting analysis for '{product_name}'... Please wait.")
            try:
                with st.spinner("Analyzing product... This may take a few moments."):
                    results, elapsed_time, usage_metrics = analyze_product(product_name)

                # Display results
                st.success(f"Analysis completed in {elapsed_time:.2f} seconds.")

                # Crew Metrics
                st.subheader("Crew Usage Metrics")
                st.json(usage_metrics)

                # Analysis Reports
                st.subheader("Analysis Results")
                display_results(results)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
