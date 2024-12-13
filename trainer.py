from transformers import TrainingArguments
print('111111111111111111111')
from transformers import Trainer
print('2222222222222222222')
from src.pretrained_model import model
print('333333333333333333')
from src.tokenized_model import tokenized_dataset
print('444444444444444444444')
from src.collator import data_collator
print('555555555555555555555555')
from src.tokenized_model import tokenizer
print('aaaaaaaaaaaaaaa')
# Define training arguments
training_args = TrainingArguments(
    output_dir="./llama_model",       # Directory to save the model
    overwrite_output_dir=True,     
    num_train_epochs=3,            # Number of epochs
    per_device_train_batch_size=2, # Batch size per GPU
    save_steps=500,                # Save checkpoints every 500 steps
    save_total_limit=2,            # Keep the last 2 checkpoints
    logging_dir="./logs",          # Logging directory
    logging_steps=10               # Log every 10 steps
)
print('bbbbbbbbbbbbbbbbbbb')
# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=data_collator
)

print('cccccccccccccccccccc')

trainer.train()
print('dddddddddddddddddddddddd')
# Save the fine-tuned model
model.save_pretrained("./fine_tuned_llama")
print('eeeeeeeeeeeeeeeeeeeeeee')
# Save the tokenizer
tokenizer.save_pretrained("./fine_tuned_llama")
print('ffffffffffffffffffffffff')
print("Model and tokenizer have been saved to './fine_tuned_llama'")
