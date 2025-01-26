# Script for poem generation

from transformers import AutoTokenizer, AutoModelForCausalLM, GPT2LMHeadModel, GPT2Tokenizer
import torch

#___________
# Load models and tokenizers
def load_model(model_name):
    """Load the model if already downloaded, else download first and load it"""
    print(f"Loading model {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    print(f" Model {model_name} successfully loaded!✔️")
    return tokenizer, model

# Generate poem from keyword or phrase
def generate_poem(model:AutoModelForCausalLM, tokenizer:AutoTokenizer, prompt, max_length=600):
    """Based on the passed model, tokenizer and prompt, generate a poem"""
    
    # Encode the input prompt
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generate output from the model
    outputs = model.generate(
        inputs['input_ids'], 
        max_length=max_length, 
        num_return_sequences=1, 
        no_repeat_ngram_size=2,  # Prevent repetition
        top_p=0.92,  # Top-p sampling
        top_k=50,  # Top-k sampling
        temperature=0.8,  # Creativity level
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Decode and return the generated poem
    poem = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return poem
#___________
