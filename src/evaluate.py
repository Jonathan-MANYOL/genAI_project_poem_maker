# Script for evaluation of generated poems
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer
import streamlit as st

# Function to evaluate poems using BLEU and ROUGE scores
def evaluate_poems(poem1, poem2):
    """
    Evaluate two poems using BLEU and ROUGE metrics.

    Args:
        poem1 (str): The first generated poem.
        poem2 (str): The second generated poem.

    Returns:
        dict: A dictionary containing BLEU and ROUGE scores.
    """
    # Tokenize poems for BLEU evaluation
    ref_tokens = poem1.split()
    gen_tokens = poem2.split()

    # BLEU Score
    smoothie = SmoothingFunction().method4  # Smoothing for better BLEU results
    bleu_score = sentence_bleu([ref_tokens], gen_tokens, smoothing_function=smoothie)

    # ROUGE Scores
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(poem1, poem2)

    # Format results
    results = {
        'BLEU': round(bleu_score, 4),
        'ROUGE-1': round(rouge_scores['rouge1'].fmeasure, 4),
        'ROUGE-2': round(rouge_scores['rouge2'].fmeasure, 4),
        'ROUGE-L': round(rouge_scores['rougeL'].fmeasure, 4)
    }

    return results

# Function to interpret and display results
def interpret_results(results):
    """
    Interpret and print the evaluation results.

    Args:
        results (dict): A dictionary containing BLEU and ROUGE scores.
    """
    print("\nResults Evaluation & Interpretation:")
    print("===================")
    print(f"BLEU Score: {results['BLEU']:.4f}")
    print(f"ROUGE-1 F-Measure: {results['ROUGE-1']:.4f}")
    print(f"ROUGE-2 F-Measure: {results['ROUGE-2']:.4f}")
    print(f"ROUGE-L F-Measure: {results['ROUGE-L']:.4f}")
    
    print("\nInterpretation Results: \n⚠️ All the following scores range from 0.0 to 1.0!")
    print("===================")
    print("  |=> BLEU:  Measures the overlap of n-grams between the two texts.\n\t- A score closer to 1.0 indicates high similarity, \n\t- but a low score does not necessarily mean poor quality for creative tasks.")
    print("  |=> ROUGE-1:  Evaluates the overlap of unigrams (single words) between the texts. \n\t- Higher scores suggest greater word-level similarity.")
    print("  |=> ROUGE-2:  Evaluates the overlap of bigrams (two-word sequences). \n\t- This provides a more detailed comparison of textual structure.")
    print("  |=> ROUGE-L:  Focuses on the longest common subsequence, \n\t- reflecting sentence-level structural similarity. \n\t- Higher scores indicate better alignment.")

# Function to interpret and display results in Streamlit
def interpret_results_gui(results):
    """
    Interpret and display the evaluation results in Streamlit.

    Args:
        results (dict): A dictionary containing BLEU and ROUGE scores.
    """
    # st.write("### Evaluation Results")
    # st.write("The scores below range from **0.0 to 1.0**, where higher values indicate stronger similarity.")
    # st.write("----")
    
    # # Display BLEU and ROUGE scores
    # st.write(f"**BLEU Score**: {results['BLEU']:.4f}")
    # st.write(f"**ROUGE-1 F-Measure**: {results['ROUGE-1']:.4f}")
    # st.write(f"**ROUGE-2 F-Measure**: {results['ROUGE-2']:.4f}")
    # st.write(f"**ROUGE-L F-Measure**: {results['ROUGE-L']:.4f}")
    # st.write("----")
    
    # Interpretation of the scores
    st.write("### Interpretation")
    st.markdown(
        """
        - **BLEU**: Measures the overlap of n-grams between the two texts.
          - A score closer to **1.0** indicates high similarity.
          - A low score doesn't necessarily mean poor quality for creative tasks.
        
        - **ROUGE-1**: Evaluates the overlap of unigrams (single words) between the texts.
          - Higher scores suggest greater word-level similarity.
        
        - **ROUGE-2**: Evaluates the overlap of bigrams (two-word sequences).
          - This provides a more detailed comparison of textual structure.
        
        - **ROUGE-L**: Focuses on the longest common subsequence.
          - Reflects sentence-level structural similarity.
          - Higher scores indicate better alignment.
        """
    )
