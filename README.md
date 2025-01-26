# Generative AI Poem Maker

## I. Project description and setup instructions.
### **Objective**: 
    Create a Python application that generates poems using pre-trained language models (GPT-2 and GPT-Neo) with a simple graphical user interface (GUI) for user interaction.

### **Steps to Follow**

1. **Environment Setup**:
   - Install the necessary libraries: `transformers`, `torch`, `streamlit`, `nltk`, `rouge-score`.
   - Download pre-trained models (GPT-2 and GPT-Neo).

2. **Text Generation**:
   - Implement a script that uses GPT-2 and GPT-Neo to generate poems based on a prompt or keyword provided by the user.
   - Compare the two generated poems using BLEU and ROUGE scores.
   - Interpret and display the evaluation results.

3. **Graphical Interface**:
   - Use **Streamlit** to create a simple UI for the application:
     - Textbox to input a keyword.
     - Button to trigger poem generation.
     - Display generated poems from both models.
     - Display BLEU and ROUGE scores for the poems.

4. **Demonstrative Video**:
   - Prepare a short video demonstrating how to use the application:
     - Input keyword.
     - Generate poem.
     - Display and explain the scores.
     - Show the results in the interface.

### **Deliverables**
- A fully functional standalone application.
- A 2-minute video demonstrating the app and explaining its features.


## II. Project directory structure
final_project
|__ src
|   |_ `app.py` # The app, the one to be run using `streamlit run app.py`
|   |_ `evaluate.py` # The evaluation script
|   |_ `generate.py` # The script for poem generation 
|__ `GUI_Records.mov` # A recording of the `app.py` in action
|__ `requirements.txt` # The project requirements
|__ `README.md` # This file explaining the project
|__ `Sujet projet - IA GEN.pdf` # The project definition


## For future work

### 1. interesting Data sources: 
- Original txt file for W. Shakespeare poems: https://www.gutenberg.org/files/100/100-0.txt
- Original txt file for V. Hugo's poems: https://www.gutenberg.org/cache/epub/8775/pg8775.txt

The README you've written is clear and well-organized. However, a few areas could be enhanced for better clarity and flow. Here's a revised version with slight adjustments to improve readability:

---

# Generative AI Poem Maker

## I. Project Description and Setup Instructions

### **Objective**  
Create a Python application that generates poems using pre-trained language models (GPT-2 and GPT-Neo) with a simple graphical user interface (GUI) for user interaction.

### **Steps to Follow**

1. **Environment Setup**  
   - Install the necessary libraries:
     ```bash
     pip install transformers torch streamlit nltk rouge-score
     ```
   - Download the pre-trained models (GPT-2 and GPT-Neo).

2. **Text Generation**  
   - Implement a script that uses GPT-2 and GPT-Neo to generate poems based on a prompt or keyword provided by the user.
   - Compare the generated poems using **BLEU** and **ROUGE** scores.
   - Interpret and display the evaluation results.

3. **Graphical Interface**  
   - Use **Streamlit** to create a simple UI for the application:
     - A textbox to input a keyword.
     - A button to trigger poem generation.
     - Display the generated poems from both models.
     - Display the BLEU and ROUGE scores for the poems.

4. **Demonstrative Video**  
   - Prepare a short video demonstrating how to use the application:
     - Input a keyword.
     - Generate a poem.
     - Display and explain the scores.
     - Show the results in the interface.

### **Deliverables**
- A fully functional standalone application.
- A 2-minute video demonstrating the app and explaining its features.

---

## II. Project Directory Structure

```
final_project/
|__ src/
|   |_ `app.py`            # The app, the one to be run using `streamlit run app.py`
|   |_ `evaluate.py`       # The evaluation script
|   |_ `generate.py`       # The script for poem generation 
|__ `GUI_Records.mov`      # A recording of the `app.py` in action
|__ `requirements.txt`     # The project requirements
|__ `README.md`            # This file explaining the project
|__ `Sujet projet - IA GEN.pdf` # The project definition
```

---

## III. For Future Work

### 1. Interesting Data Sources  
- **W. Shakespeare Poems**: [Gutenberg - Shakespeare](https://www.gutenberg.org/files/100/100-0.txt)  
- **V. Hugo Poems**: [Gutenberg - Hugo](https://www.gutenberg.org/cache/epub/8775/pg8775.txt)  

---
