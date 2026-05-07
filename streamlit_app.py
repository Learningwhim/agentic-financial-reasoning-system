import streamlit as st

from app.orchestration.pipeline import app

st.set_page_config(
    page_title="AI Investment Analysis System",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Investment Analysis System")

st.markdown(
    """
    Multi-agent investment research system using:
    - Planner Agent
    - Search Agent
    - Bull Analyst
    - Bear Analyst
    - Critic Agent
    """
)

query = st.text_input(
    "Enter Investment Query",
    placeholder="Should I invest in NVIDIA?"
)

if st.button("Run Analysis"):

    if not query.strip():
        st.warning("Please enter a query.")
        st.stop()

    # LIVE STATUS
    status = st.empty()

    with st.spinner("Running orchestration pipeline..."):

        status.info("Planner agent running...")
        status.info("Search agent gathering market intelligence...")
        status.info("Launching bull and bear analysts...")
        status.info("Critic evaluating arguments...")

        result = app.invoke({
            "query": query
        })

    status.success("Pipeline execution complete.")

    st.divider()

    # FINAL DECISION
    st.subheader("🎯 Final Decision")

    decision = result["final_decision"]
    critique = result["critique"]

    st.metric(
        label="Recommendation",
        value=decision
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Confidence",
            critique["confidence"]
        )

    with col2:
        st.metric(
            "Risk Level",
            critique["risk_level"]
        )

    st.divider()

    # BULL / BEAR
    col1, col2 = st.columns(2)

    # BULL
    with col1:

        st.subheader("📈 Bull Analysis")

        bull = result["bull_case"]

        st.metric(
            "Bull Score",
            f"{bull['score']}/10"
        )

        st.metric(
            "Bull Confidence",
            bull["confidence"]
        )

        with st.expander("View Bull Reasoning"):
            st.write(bull["reasoning"])

    # BEAR
    with col2:

        st.subheader("📉 Bear Analysis")

        bear = result["bear_case"]

        st.metric(
            "Bear Score",
            f"{bear['score']}/10"
        )

        st.metric(
            "Bear Confidence",
            bear["confidence"]
        )

        with st.expander("View Bear Reasoning"):
            st.write(bear["reasoning"])

    st.divider()

    # CRITIC
    st.subheader("🧠 Critic Evaluation")

    with st.expander("View Critic Reasoning", expanded=True):
        st.write(critique["final_reasoning"])

    st.divider()

    # RAW SEARCH DATA
    with st.expander("🔍 Retrieved Market Intelligence"):

        search_data = result["search_data"]

        if isinstance(search_data, list):

            for idx, item in enumerate(search_data, start=1):

                st.markdown(f"### Result {idx}")

                if isinstance(item, dict):

                    if "title" in item:
                        st.write(f"**Title:** {item['title']}")

                    if "content" in item:
                        st.write(item["content"])

                    if "url" in item:
                        st.markdown(f"[Source Link]({item['url']})")

                st.divider()

        else:
            st.write(search_data)