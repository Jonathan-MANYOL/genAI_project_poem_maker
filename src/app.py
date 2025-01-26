# # Streamlit GUI application
import streamlit as st
from generate import load_model, generate_poem
from evaluate import evaluate_poems, interpret_results_gui

# Cache the models and tokenizers
@st.cache_resource
def initialize_model(model_name):
    return load_model(model_name)

# Load both models lazily
gpt2_tokenizer, gpt2_model = initialize_model("gpt2")
neo_tokenizer, neo_model = initialize_model("EleutherAI/gpt-neo-125M")

def main():
    # App title and description
    st.title("Poem Generator and Evaluator")
    st.markdown("**Generate poems using GPT-2 and GPT-Neo and evaluate their quality using BLEU and ROUGE scores.**")

    # Input Section
    st.header("1. Input Prompt")
    prompt = st.text_input(
        "Enter a prompt for the poem:",
        # "Write a poem about a ... ",
        help="Type a short description or theme for the poem.", 
        placeholder='Type here the beginning of your poem'
    )
    # Add a "Generate" button
    generate_button = st.button("Generate Poems")
        
    # Proceed if there's a valid prompt or the generate button is pressed
    if prompt.strip() or generate_button:
        # # Load both models lazily
        # with st.spinner("Loading models..."):
        #     gpt2_tokenizer, gpt2_model = initialize_model("gpt2")
        #     neo_tokenizer, neo_model = initialize_model("EleutherAI/gpt-neo-125M")

        # Display the generated poems side by side
        st.subheader("2. Generated Poems")
        # Generate poems
        with st.spinner("Generating poems..."):
            gpt2_poem = generate_poem(gpt2_model, gpt2_tokenizer, prompt)
            neo_poem = generate_poem(neo_model, neo_tokenizer, prompt)

            # Calculate text area height dynamically based on text length
            gpt2_poem_height = max(300, len(gpt2_poem) // 50)  # Dynamically adjust height based on length
            neo_poem_height = max(300, len(neo_poem) // 50)

            # Create two columns for side-by-side display
            col1, col2 = st.columns(2)

            # Place the text areas in each column
            with col1:
                st.text_area("**GPT-2 Poem:**", gpt2_poem, height=gpt2_poem_height)

            with col2:
                st.text_area("**GPT-Neo Poem:**", neo_poem, height=neo_poem_height)

        # Evaluate the poems
        st.subheader("3. Results Evaluation & Interpretation")
        st.write("The scores below range from **0.0 to 1.0**, where higher values indicate stronger similarity.")
        st.write("----")
        results = evaluate_poems(gpt2_poem, neo_poem)
        st.json(results)

        # Display interpretation of results
        st.subheader("Interpretation of Evaluation Results")
        interpretation_text = interpret_results_gui(results)
        st.markdown(interpretation_text)

    else:
        st.info("Enter a prompt and click 'Generate Poems' or simply type to generate poems.")


if __name__ == "__main__":
    main()
