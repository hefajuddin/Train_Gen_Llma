from transformers import AutoModelForCausalLM

# Load a pre-trained GPT model
model = AutoModelForCausalLM.from_pretrained("Llama-3.2-1B")