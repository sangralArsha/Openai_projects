
# import openai library
import openai
openai.api_key = "YOUR_API_KEY"

# getting setiment response from openai model 
def get_sentiment(text):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Analyze the sentiment of the following text: {text}",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    sentiment = response.choices[0].text.strip()
    return sentiment
    
text = input("Enter some text: ")
sentiment = get_sentiment(text)
print("The sentiment of the text is " + sentiment)