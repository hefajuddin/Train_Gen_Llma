from transformers import AutoModelForCausalLM
print('111')
model_name = "meta-llama/Llama-2-7b-hf"  # Example of a valid LLaMA model
print('222')
model = AutoModelForCausalLM.from_pretrained(model_name)
print('333')
