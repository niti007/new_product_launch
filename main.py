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
        max_rpm=29
    )

    # Kick off the crew
    results = crew.kickoff()
    return results


def extract_report_content(result):
    """Extract the actual report content from various result formats."""
    if isinstance(result, tuple):
        report_type, content = result
        if report_type == 'raw' and content:
            return content
    elif isinstance(result, dict) and result.get('raw'):
        return result['raw']
    elif hasattr(result, 'raw') and result.raw:
        return result.raw
    return None


def display_results(results):
    """Display the reports in a clean, formatted way."""
    for i, result in enumerate(results, 1):
        content = extract_report_content(result)

        if content:
            # Create an expander for each report
            with st.expander(f"Report {i}", expanded=True):
                # Split the report into sections based on headers
                sections = content.split('\n\n')

                for section in sections:
                    if section.strip():
                        # Check if it's a header (starts with common header indicators)
                        if section.strip().startswith(('Executive Summary', 'Market Analysis', 'Customer Profile',
                                                       'Revenue Streams', 'Scalability', 'Business Plan', 'Goals',
                                                       'Timeline')):
                            st.markdown(f"### {section.strip()}")
                            st.markdown("---")
                        else:
                            st.markdown(section)


def main():
    st.title("Product Analysis Dashboard")

    # Custom CSS to improve readability
    st.markdown("""
        <style>
        .reportview-container {
            max-width: 1200px;
            padding-top: 2rem;
        }
        .markdown-text-container {
            max-width: 100% !important;
        }
        h3 {
            color: #1f77b4;
            margin-top: 1rem;
        }
        .stExpander {
            border: 1px solid #f0f2f6;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        .stMarkdown {
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    # Input section
    product_name = st.text_input("Enter the product name you want to analyze:", "")

    if st.button("Analyze Product"):
        if not product_name:
            st.error("Please enter a product name before starting the analysis.")
        else:
            # Create a placeholder for the loading message
            loading_placeholder = st.empty()
            loading_placeholder.info(f"Starting analysis for '{product_name}'... Please wait.")

            try:
                with st.spinner("Analyzing product... This may take a few moments."):
                    results = analyze_product(product_name)

                # Clear the loading message
                loading_placeholder.empty()

                # Display the reports
                st.subheader("Analysis Results")
                display_results(results)

            except Exception as e:
                loading_placeholder.empty()  # Clear loading message if error occurs
                st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
