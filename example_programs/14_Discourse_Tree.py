import spacy
from nltk import Tree

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to perform discourse operation and draw the tree
def discourse_operation_and_draw_tree(sentence):
    # Parse the sentence using spaCy
    doc = nlp(sentence)

    # Create a dependency tree from spaCy's parsed result
    def to_nltk_tree(node):
        if node.n_lefts + node.n_rights > 0:
            return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
        else:
            return node.orth_

    tree = to_nltk_tree(list(doc.sents)[0].root)
    tree.pretty_print()

# Example sentence
sentence = "Don't piss in my garden and tell me you're trying to help my plants grow.We're careful about orange ping pong balls because people might think they're fruit."

# Perform discourse operation and draw the tree
discourse_operation_and_draw_tree(sentence)
