import time
from anthropic import Anthropic
from dotenv import load_dotenv
import os
from Metrics_stats import analyze_sentiment, calc_similarity

# Load environment variables
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)

# Pipeline 1: Send chunks individually
def send_chunks_individually(chunks):
    responses_list = []
    start = time.time()
    for item in chunks:
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": item}
            ]
        )
        reply = response.content[0].text
        responses_list.append(reply)
    end = time.time()
    duration_time = end - start
    return responses_list, duration_time

# Pipeline 2: Send as one batch
def send_as_batch(chunks):
    start = time.time()
    combined = " ".join(chunks)
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": combined}
        ]
    )
    reply = response.content[0].text
    end = time.time()
    duration = end - start
    return reply, duration

# Response length analyzer
def response_length_analyzer(responses, pipeline):
    response_list = []
    for characters in responses:
        length = len(characters)
        response_list.append(length)
    total = sum(response_list)
    average = total / len(responses)
    maximum = max(response_list)
    minimum = min(response_list)
    return {
        "total": total,
        "average": round(average, 3),
        "longest": maximum,
        "shortest": minimum
    }

# Response metric analyzer (sentiment)
def response_metric(responses):
    polarity_list = []
    subjectivity_list = []
    for response in responses:
        result = analyze_sentiment(response)
        polarity_list.append(result["sentiment"])
        subjectivity_list.append(result["subjectivity"])
    
    average_polarity = sum(polarity_list) / len(polarity_list)
    average_subjectivity = sum(subjectivity_list) / len(subjectivity_list)
    
    return {
        "sentiment": round(average_polarity, 3),
        "subjectivity": round(average_subjectivity, 3)
    }

# ============================================
# MAIN TEST - Compare Both Pipelines
# ============================================
if __name__ == "__main__":
    test_chunks = ["What is Python?", "What is an API?", "What is a loop?"]
    
    print("=" * 50)
    print("PIPELINE 1: Individual Chunks")
    print("=" * 50)
    responses_1, time_taken_1 = send_chunks_individually(test_chunks)
    print(f"Number of responses: {len(responses_1)}")
    print(f"Metrics: {response_metric(responses_1)}")
    print(f"Time taken: {round(time_taken_1, 3)} seconds")
    
    print("\n" + "=" * 50)
    print("PIPELINE 2: Batch")
    print("=" * 50)
    responses_2, time_taken_2 = send_as_batch(test_chunks)
    print(f"Number of responses: 1")
    print(f"Metrics: {response_metric([responses_2])}")
    print(f"Time taken: {round(time_taken_2, 3)} seconds")
    
    print("\n" + "=" * 50)
    print("COMPARISON")
    print("=" * 50)
    
    # Combine Pipeline 1 responses for similarity comparison
    combined_text = " ".join(responses_1)
    similarity_score = calc_similarity(combined_text, responses_2)
    
    print(f"Similarity score: {similarity_score}")
    print(f"Time difference: {round(time_taken_1 - time_taken_2, 3)} seconds")
    print(f"Batch was {'faster' if time_taken_2 < time_taken_1 else 'slower'} by {round(abs(time_taken_1 - time_taken_2), 3)} seconds")
