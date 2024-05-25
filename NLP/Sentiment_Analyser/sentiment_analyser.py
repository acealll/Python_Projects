from transformers import pipeline

def main():
    #Setting up the sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")

    #Getting user input
    input_sentence = input("Please enter a sentence to analyze its sentiment: ")

    #Determining the sentiment
    result = sentiment_pipeline(input_sentence)[0]

    #Displaying the result
    label = result['label']
    score = result['score']

    print(f"Sentiment: {label}, Score: {score:.4f}")

if __name__ == "__main__":
    main()
