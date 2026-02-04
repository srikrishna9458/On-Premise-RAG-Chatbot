import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # This pulls in your working ChromaDB logic

# 1. Page Configuration
st.set_page_config(page_title="Pizza Expert", page_icon="🍕")
st.title("On-Premise Pizza Review Chatbot")
st.markdown("---")

# 2. Initialize Model & Chain
# We use st.cache_resource so the model stays in memory and doesn't reload
@st.cache_resource
def get_chain():
    # Using Llama 3.2 as your local brain
    model = OllamaLLM(model="llama3.2")
    
    template = """
    You are an expert in answering questions about a pizza restaurant.
    
    Here are some relevant customer reviews to help you:
    {reviews}
    
    User Question: {question}
    
    Instructions: Use only the provided reviews to answer. If the answer isn't in 
    the reviews, politely say you don't have that information.
    """
    prompt = ChatPromptTemplate.from_template(template)
    return prompt | model

chain = get_chain()

# 3. Initialize Chat History (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Chat History on Rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Handle User Input
if user_input := st.chat_input("Ask me about the pizza..."):
    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Searching local review database..."):
            # A. Retrieve context using your vector.py retriever
            relevant_docs = retriever.invoke(user_input)
            
            # B. Format context for the prompt
            context_text = "\n\n".join([doc.page_content for doc in relevant_docs])
            
            # C. Run the Chain
            response = chain.invoke({"reviews": context_text, "question": user_input})
            
            # D. Display result
            st.markdown(response)
            
            # Optional: Show which reviews were used (collapsible)
            with st.expander("Show source context"):
                for doc in relevant_docs:
                    st.write(f"- {doc.page_content[:150]}...")
    
    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
    