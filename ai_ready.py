import streamlit as st

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True


if check_password():
        # Define the weights for each question separately
    question_weights = {
            "Q1. How does your company view AI today?": 1.5,
            "Q2. How is AI initiative tied to goals of your org?": 1.2,
            "Q3. Have your org solved problems without big data/AI?": 1,
            "Q4. Do you have a team of AI experts in house?": 1.3,
            "Q5. Rate availability and accessibility of data?": 1.2,
            "Q6. How do you measure the impact of data initiatives?": 1,
            "Q7. What kind of budgets or investments are available or needed for above?": 1
        }


    weight_mapping = {
            "Strategic Advantage": 15,
            "Exploring Possibilities": 10,
            "Limited Integration": 5,
            "Not Considered": 0,
            "Aligned with Goals": 15,
            "Partial Alignment": 10,
            "Limited Impact": 5,
            "Not Tied": 0,
            "Successfully Solved": 15,
            "Partial Success": 10,
            "Limited Success": 5,
            "Not Applicable": 0,
            "Expert Team": 15,
            "Skillful Team": 10,
            "Limited Expertise": 5,
            "No AI Experts": 0,
            "Highly Accessible": 15,
            "Moderately Accessible": 10,
            "Limited Access": 5,
            "Data Quality Issues": 0,
            "Clear Metrics": 15,
            "Partial Metrics": 10,
            "Limited Measurement": 5,
            "No Defined Metrics": 0,
            "Adequate Budget": 15,
            "Budget Constraints": 10,
            "Seeking Investments": 5,
            "No Budget Allocated": 0,
        }


    def calculate_score(answers):
            # Calculate the final weighted score based on the answers
            total_score = sum(question_weights[q] * weight_mapping[answers[q]] for q in answers)
            return total_score

    def provide_recommendations(normalized_score):
        if normalized_score >= 80:
            return "Congratulations! Your organization is well-prepared for AI adoption. Continue to invest in AI initiatives and explore advanced applications."
        elif 60 <= normalized_score < 80:
            return "Your organization has made good progress in AI readiness. Consider addressing specific areas of improvement and expanding AI implementation."
        elif 40 <= normalized_score < 60:
            return "There is room for improvement in your organization's AI readiness. Focus on enhancing data accessibility, aligning AI initiatives with goals, and investing in AI expertise."
        else:
            return "Your organization may need significant improvements in AI readiness. Prioritize strategic planning, address data quality issues, and invest in building a skilled AI team."


    def ai_readiness_survey():
        st.title("AI Readiness Survey")

        # Get user input
        name = st.text_input("1. Name of the person answering")
        organization_name = st.text_input("2. Organization Name")
        industry_vertical = st.selectbox("3. Industry Vertical", ["Finance", "Healthcare", "Technology", "Manufacturing", "Other"])
        job_level = st.radio("4. Your job level",
                            ["Execution", "Mid-level", "Manager", "Director", "C-suite"])
        revenue_options = ["Less than 50 mil", "50-100 mil", "100-200 mil", "200+ mil"]
        company_revenue = st.radio("5. Your company revenue", revenue_options)

        st.subheader("Survey Questions:")

        # Questions and English language choices
        questions_choices = {
            "Q1. How does your company view AI today?": {
                "Strategic Advantage": "AI is seen as a strategic advantage",
                "Exploring Possibilities": "AI is being explored for potential benefits",
                "Limited Integration": "AI is used in specific areas but not integrated",
                "Not Considered": "AI is not considered or recognized"
            },
            "Q2. How is AI initiative tied to goals of your org?": {
                "Aligned with Goals": "AI initiatives are closely aligned with organizational goals",
                "Partial Alignment": "AI initiatives have some alignment with organizational goals",
                "Limited Impact": "AI initiatives have limited impact on organizational goals",
                "Not Tied": "AI initiatives are not explicitly tied to organizational goals"
            },
            "Q3. Have your org solved problems without big data/AI?": {
                "Successfully Solved": "Organization has successfully solved problems without AI",
                "Partial Success": "Organization has had some success without AI, but challenges persist",
                "Limited Success": "Organization has had limited success without AI",
                "Not Applicable": "Big data/AI is integral to problem-solving"
            },
            "Q4. Do you have a team of AI experts in house?": {
                "Expert Team": "Yes, we have a dedicated team of AI experts",
                "Skillful Team": "We have individuals with AI skills, but not a dedicated team",
                "Limited Expertise": "We have limited AI expertise in-house",
                "No AI Experts": "We do not have AI experts in-house"
            },
            "Q5. Rate availability and accessibility of data?": {
                "Highly Accessible": "Data is highly accessible and readily available",
                "Moderately Accessible": "Data is somewhat accessible but improvements are needed",
                "Limited Access": "Access to data is limited",
                "Data Quality Issues": "Data quality issues impact accessibility"
            },
            "Q6. How do you measure the impact of data initiatives?": {
                "Clear Metrics": "Impact is measured with clear and defined metrics",
                "Partial Metrics": "Some impact metrics are measured, but not comprehensive",
                "Limited Measurement": "Impact measurement is limited",
                "No Defined Metrics": "There are no defined metrics for measuring impact"
            },
            "Q7. What kind of budgets or investments are available or needed for above?": {
                "Adequate Budget": "Adequate budget is allocated for AI initiatives",
                "Budget Constraints": "Budget constraints impact AI initiatives",
                "Seeking Investments": "Additional investments are needed for AI initiatives",
                "No Budget Allocated": "No specific budget is allocated for AI initiatives"
            }
    
        }

    

        # Collect user responses
        answers = {}
        for question, choices in questions_choices.items():
            answers[question] = st.radio(question, list(choices.keys()), format_func=lambda x: choices[x])

        # Add a multi-select box for highlighting typical areas/problems
        problems = st.multiselect("Typical areas/problems that you face with", ["Data quality", "Data privacy", "Data security", "Data governance", "Other"])

        # Create a "Submit" button
        if st.button("Submit"):
            # Calculate the final score
            final_score = calculate_score(answers)

            # Calculate the maximum possible score
            max_possible_score = sum(question_weights[q] * max(weight_mapping.values()) for q in question_weights)

            normalized_score = (final_score / max_possible_score) * 100

            # Display the AI readiness score with bold formatting
            st.subheader("AI Readiness Score:")
            st.write(f"**{name}**, your AI readiness score is: **{normalized_score:.2f}/100**")

            # Provide recommendations based on the score
            st.subheader("Recommendations:")
            recommendation = provide_recommendations(normalized_score)
            st.write(recommendation)
            # ... (rest of the code remains the same)

    # Run the app
    if __name__ == "__main__":
        ai_readiness_survey()