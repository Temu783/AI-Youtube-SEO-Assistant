from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
import json

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load OpenAI LLM
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.7, model="gpt-3.5-turbo")

# Read prompt from file
with open("prompts/youtube_prompt.txt", "r", encoding="utf-8") as f:
    prompt_text = f.read()

# ✅ Correct prompt template with ONLY "topic" input
prompt = PromptTemplate(
    input_variables=["topic"],
    template=prompt_text
)

# Create LLM Chain
seo_chain = LLMChain(llm=llm, prompt=prompt)

# Function to generate SEO content
def generate_seo_content(topic):
    output = seo_chain.run({"topic": topic})
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        print("❌ JSON Parse Error. Raw Output:\n", output)
        return {"title": "", "description": "", "tags": [], "ideas": []}
