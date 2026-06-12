import streamlit as st
from agents.main_agent import MainAgent
from database.db_manager import DatabaseManager
from utils.docx_generator import DocxGenerator
from utils.pdf_generator import PdfGenerator

if "results" not in st.session_state:
    st.session_state.results = {}

# Page Configuration
st.set_page_config(
    page_title="EduGen AI",
    page_icon="🎓",
    layout="wide"
)

# Sidebar
st.sidebar.title("🎓 EduGen AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Generate Content",
        "History",
        "Settings"
    ]
)

# Dashboard Page
if page == "Dashboard":

    st.title("🎓 EduGen AI Dashboard")

    st.success(
        """
    Welcome to EduGen AI

    Generate lesson plans, quizzes,
    teacher notes and learning activities
    using Agentic AI.
    """
    )
    
    db = DatabaseManager()

    lesson_count = db.get_content_count(
        "Lesson Plan"
    )

    notes_count = db.get_content_count(
        "Teacher Notes"
    )

    quiz_count = db.get_content_count(
        "Quiz"
    )
    recent_history = db.get_recent_history()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📘 Lesson Plans",
            lesson_count
        )

    with col2:
        st.metric(
            "📋 Quizzes",
            quiz_count
        )

    with col3:
        st.metric(
            "📝 Teacher Notes",
            notes_count
        )

    st.divider()

    st.subheader(
        "🚀 Features Available"
    )

    st.markdown(
        """
    ✅ Lesson Plan Generator

    ✅ Teacher Notes Generator

    ✅ Quiz Generator

    ✅ Activity Generator

    ✅ Learning Outcomes Generator

    ✅ Download Content

    ✅ History Tracking

    ✅ SQLite Database
    """
    )

    st.divider()

    st.subheader(
        "🕒 Recent Activity"
    )

    if len(recent_history) == 0:

        st.info(
            "No recent activity available."
        )

    else:

        for item in recent_history:

            st.write(
                f"• {item[0]} ({item[1]})"
            )
    
# Generate Content Page
elif page == "Generate Content":

    st.title("📝 Generate Content")

    subject = st.text_input(
        "Subject"
    )

    grade = st.selectbox(
        "Grade",
        [
            "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "10"
        ]
    )

    topic = st.text_input(
        "Topic"
    )

    duration = st.selectbox(
        "Duration",
        [
            "30 Minutes",
            "45 Minutes",
            "1 Hour",
            "2 Hours"
        ]
    )

    st.subheader("Select Content")

    lesson_plan = st.checkbox(
        "Lesson Plan"
    )

    notes = st.checkbox(
        "Teacher Notes"
    )

    quiz = st.checkbox(
        "Quiz"
    )

    activities = st.checkbox(
        "Activities"
    )

    outcomes = st.checkbox(
        "Learning Outcomes"
    )

    generate_button = st.button(
        "Generate Content"
    )

    if generate_button:

        if subject.strip() == "":

            st.error(
                "Please enter a subject."
            )

        elif topic.strip() == "":

            st.error(
                "Please enter a topic."
            )

        else:

            selected_content = []

            if lesson_plan:
                selected_content.append(
                    "lesson_plan"
                )

            if notes:
                selected_content.append(
                    "notes"
                )

            if quiz:
                selected_content.append(
                    "quiz"
                )

            if activities:
                selected_content.append(
                    "activities"
                )

            if outcomes:
                selected_content.append(
                    "outcomes"
                )

            if len(selected_content) == 0:

                st.warning(
                    "Please select at least one content type."
                )

            else:

                agent = MainAgent()

                with st.spinner(
                    "Generating AI Content..."
                ):

                    st.session_state.results = (
                        agent.generate_selected_content(
                            subject=subject,
                            grade=grade,
                            topic=topic,
                            duration=duration,
                            selected_content=selected_content
                        )
                    )
                    st.session_state.subject = subject
                    st.session_state.grade = grade
                    st.session_state.topic = topic

                    db = DatabaseManager()

                    if lesson_plan:

                        db.save_generation(
                            subject,
                            grade,
                            topic,
                            "Lesson Plan"
                        )

                    if notes:

                        db.save_generation(
                            subject,
                            grade,
                            topic,
                           "Teacher Notes"
                        )

                    if quiz:

                        db.save_generation(
                            subject,
                            grade,
                            topic,
                            "Quiz"
                        )

                    if activities:

                        db.save_generation(
                            subject,
                            grade,
                            topic,
                            "Activities"
                        )

                    if outcomes:

                        db.save_generation(
                            subject,
                            grade,
                            topic,
                            "Learning Outcomes"
                        )
    results = st.session_state.results

    if "lesson_plan" in results:        

        with st.expander(        
            "📘 Lesson Plan",       
            expanded=True        
        ):       

            st.write(        
                results["lesson_plan"]        
            )

            st.download_button(
                label="📥 Download Lesson Plan",
                data=results["lesson_plan"],
                file_name=f"{topic}_Lesson_Plan.txt",
                mime="text/plain"
            )

            lesson_docx = (
                DocxGenerator.create_docx_buffer(
                    f"{topic} Lesson Plan",
                    results["lesson_plan"]
                )
            )

            lesson_pdf = (
                PdfGenerator.create_pdf_buffer(
                    f"{topic} Lesson Plan",
                    results["lesson_plan"]
                )
            )

            st.download_button(
                label="📄 Download DOCX",
                data=lesson_docx,
                file_name=f"{topic}_Lesson_Plan.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

            st.download_button(
                label="📕 Download PDF",
                data=lesson_pdf,
                file_name=f"{topic}_Lesson_Plan.pdf",
                mime="application/pdf"
            )

    if "notes" in results:

        with st.expander(
            "📝 Teacher Notes"
        ):

            st.write(
                results["notes"]
            )

            st.download_button(
                label="📥 Download Teacher Notes",
                data=results["notes"],
                file_name=f"{topic}_Teacher_Notes.txt",
                mime="text/plain"
            )

            notes_docx = (
                DocxGenerator.create_docx_buffer(
                    f"{topic} Teacher Notes",
                    results["notes"]
                )
            )

            notes_pdf = (
                PdfGenerator.create_pdf_buffer(
                    f"{topic} Teacher Notes",
                    results["notes"]
                )
            )

            st.download_button(
                label="📄 Download Notes DOCX",
                data=notes_docx,
                file_name=f"{topic}_Teacher_Notes.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

            st.download_button(
                label="📕 Download Notes PDF",
                data=notes_pdf,
                file_name=f"{topic}_Teacher_Notes.pdf",
                mime="application/pdf"
            )

    if "quiz" in results:

        with st.expander(
            "📋 Quiz"
        ):

            st.write(
                results["quiz"]
            )

            st.download_button(
                label="📥 Download Quiz",
                data=results["quiz"],
                file_name=f"{topic}_Quiz.txt",
                mime="text/plain"
            )

            quiz_docx = (
                DocxGenerator.create_docx_buffer(
                    f"{topic} Quiz",
                    results["quiz"]
                )
            )

            quiz_pdf = (
                PdfGenerator.create_pdf_buffer(
                    f"{topic} Quiz",
                    results["quiz"]
                )
            )

            st.download_button(
                label="📄 Download Quiz DOCX",
                data=quiz_docx,
                file_name=f"{topic}_Quiz.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

            st.download_button(
                label="📕 Download Quiz PDF",
                data=quiz_pdf,
                file_name=f"{topic}_Quiz.pdf",
                mime="application/pdf"
            )

    if "activities" in results:

        with st.expander(
            "🎯 Activities"
        ):

            st.write(
                results["activities"]
            )

            st.download_button(
                label="📥 Download Activities",
                data=results["activities"],
                file_name=f"{topic}_Activities.txt",
                mime="text/plain"
            )

            activities_docx = (
                DocxGenerator.create_docx_buffer(
                    f"{topic} Activities",
                    results["activities"]
                )
            )

            activities_pdf = (
                PdfGenerator.create_pdf_buffer(
                    f"{topic} Activities",
                    results["activities"]
                )
            )

            st.download_button(
                label="📄 Download Activities DOCX",
                data=activities_docx,
                file_name=f"{topic}_Activities.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

            st.download_button(
                label="📕 Download Activities PDF",
                data=activities_pdf,
                file_name=f"{topic}_Activities.pdf",
                mime="application/pdf"
            )

    if "outcomes" in results:

        with st.expander(
            "🎓 Learning Outcomes"
        ):

            st.write(
                results["outcomes"]
            ) 

            st.download_button(
                label="📥 Download Learning Outcomes",
                data=results["outcomes"],
                file_name=f"{topic}_Learning_Outcomes.txt",
                mime="text/plain"
            )

            outcomes_docx = (
                DocxGenerator.create_docx_buffer(
                    f"{topic} Learning Outcomes",
                    results["outcomes"]
                )
            )

            outcomes_pdf = (
                PdfGenerator.create_pdf_buffer(
                    f"{topic} Learning Outcomes",
                    results["outcomes"]
                )
            )

            st.download_button(
                label="📄 Download Outcomes DOCX",
                data=outcomes_docx,
                file_name=f"{topic}_Learning_Outcomes.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

            st.download_button(
                label="📕 Download Outcomes PDF",
                data=outcomes_pdf,
                file_name=f"{topic}_Learning_Outcomes.pdf",
                mime="application/pdf"
            )
      

elif page == "History":

    st.title("📚 History")

    if st.button(
        "🗑 Clear History"
    ):

        db = DatabaseManager()

        db.clear_history()

        st.success(
            "History cleared successfully."
        )   

        st.rerun()

    db = DatabaseManager()

    history = db.get_history()

    if len(history) == 0:

        st.info(
            "No history available."
        )

    else:

        for row in history:

            with st.expander(
                f"📚 {row[3]}"
            ):

                st.write(
                    f"**Subject:** {row[1]}"
                )

                st.write(
                    f"**Grade:** {row[2]}"
                )

                st.write(
                    f"**Content Type:** {row[4]}"
                )

                st.write(
                    f"**Generated On:** {row[5]}"
                )

# Settings Page
elif page == "Settings":

    st.title(
        "⚙ Settings"
    )

    st.subheader(
        "Application Information"
    )

    st.info(
        """
EduGen AI

Version: 1.0

AI Provider: Gemini

Database: SQLite

Mode: Mock Mode Enabled
        """
    )

    db = DatabaseManager()

    total_records = len(
        db.get_history()
    )

    st.metric(
        "Total Generated Records",
        total_records
    )