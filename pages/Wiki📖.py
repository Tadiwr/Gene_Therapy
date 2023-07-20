import streamlit as st

choice = ""


options = [
    "Phases",
    "Therapuetic Areas",
    "Therapuetic Routes",
    "Drugs",
    "Points",
    "Vectors",
    "Trial Status",
    "Efficacy",
    "Gene Therapy"
]

def readFile(choice: str) -> str :
    fileName : str = f"./assets/wikis/{choice.lower()}.md"
    text : str = ""

    file = open(fileName, "r")
    text = file.read()

    return text


"# Wiki 📖"

"## Don't Understand Something? Refer to the wiki 🔎"

choice = st.selectbox(
    label="What dont you understand?",
    options=options
)


st.write(f"# {choice}")
st.write(readFile(choice))



