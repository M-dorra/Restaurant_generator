from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model & tokenizer
model_id = "google/gemma-1.1-2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto" if torch.cuda.is_available() else None
)

def ask_model(prompt, max_new_tokens=100):
    inputs = tokenizer(prompt + "\nAnswer:", return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("Answer:")[-1].strip()

def generate_restauant_name_and_items(cuisine):
    # Step 1: suggest a restaurant name
    restaurant_prompt = f"Suggest a fancy restaurant name for a {cuisine} cuisine.Only return the name, nothing else."
    restaurant_name = ask_model(restaurant_prompt)

    # Step 2: generate a menu
    menu_prompt = f"The restaurant is called {restaurant_name}. Suggest 5 creative menu items for this restaurant knowing it specializes in {cuisine} cuisine . Only return the list."
    menu = ask_model(menu_prompt)
    return {
        "restaurant_name": restaurant_name,
        "menu": menu
    }
    
   
if __name__=="__main__":
    print(generate_restauant_name_and_items("Italian"))