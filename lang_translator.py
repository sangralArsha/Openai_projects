
import openai
openai.api_key = "YOUR_API_KEY"

def translate_text(text, target_language):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Translate the following text to {target_language}: {text}",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    translation = response.choices[0].text.strip()
    return translation
    
text = input("Enter some text: ")
target_language = input("Enter target language: ")
translation = translate_text(text, target_language)
print("The translation is " + translation)