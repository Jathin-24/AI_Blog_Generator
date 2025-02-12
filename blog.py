
import streamlit as st
from transformers import pipeline
from huggingface_hub import login

# Get Hugging Face API key from Streamlit secrets
api_key = "apikey"

# Automatically log in using the API key stored in secrets
login(api_key)
st.success("Successfully logged in to Hugging Face!")

# Setup model pipeline
generator = pipeline('text-generation', model='gpt2')

# Streamlit UI with styling
st.title("🌟 AI Blog Generator 🌟")
st.write("Generate blog posts with an AI model from Hugging Face! 🤖✨")

# Adding custom CSS for colorful design
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        font-size: 16px;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #4682B4;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #FFF8DC;
        border-radius: 8px;
        border: 1px solid #DDD;
        color: #444;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    .stSlider div {
        font-weight: bold;
    }
    h1, h2 {
        color: #FF6347;
    }
    .stMarkdown {
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
""", unsafe_allow_html=True)

# Inputs for prompt and settings
st.header("🎨 Enter Prompt to Generate Blog 📝")
prompt = st.text_area("Your Blog Prompt", "The future of AI in content creation", height=120)

# Slider for maximum length of text
max_length = st.slider("🌟 Maximum Length of the Text", 100, 1000, 500)
num_sequences = st.slider("📝 Number of Blog Variations", 1, 5, 1)

# Button to generate the blog
if st.button("Generate Blog"):
    if prompt:
        with st.spinner('Generating your blog... 🖋️'):
            # Use Hugging Face API to generate text
            generated_text = generator(prompt, max_length=max_length, num_return_sequences=num_sequences)

            # Display the generated blogs
            st.subheader("📝 Generated Blog(s):")
            for idx, gen_text in enumerate(generated_text):
                st.markdown(f"**Blog {idx + 1}:**")
                st.write(gen_text['generated_text'])
    else:
        st.error("🚨 Please enter a prompt to generate the blog!")
