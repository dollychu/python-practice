import fetch_data
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()

mc.add_string("Quickly, he ran and he ran until he couldn't.")
print(mc.generate_text())