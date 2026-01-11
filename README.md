# LLM Content Analyzer (Context Mitigation Analyzer)

A Python tool to compare LLM performance using two different input strategies: feeding information in small chunks versus sending large batches at once.

## Project Overview

This project tests the practical limitations of context windows in LLM applications by:
- Sending identical information through two different pipelines
- Collecting and comparing responses
- Implementing metrics to evaluate response accuracy and quality differences

## Features

✅ **Dual Pipeline Architecture**
- Pipeline 1: Sends chunks individually (context refresh approach)
- Pipeline 2: Sends all chunks as one batch

✅ **Multi-Metric Analysis System**
- Response time comparison
- Sentiment analysis (TextBlob - polarity & subjectivity)
- Semantic similarity (scikit-learn cosine similarity)
- Character count analysis

✅ **Automated Testing Framework**
- Runs same queries through both pipelines
- Collects quantifiable results

## Key Findings

- Chunking strategy produced ~40% faster responses
- Batch processing produced only ~62% similar responses to chunked processing
- Chunking gives more concise outputs optimized for context retrieval

## Tech Stack

- Python
- Anthropic Claude API
- TextBlob (sentiment analysis)
- scikit-learn (cosine similarity)
- python-dotenv (environment variables)

## Installation

```bash
pip install anthropic textblob scikit-learn python-dotenv
```

## Setup

1. Copy `.env.example` to `.env`
2. Add your Anthropic API key to `.env`
3. Run the main test file:

```bash
python test_claudeapi.py
```

## File Structure

```
LLM_CONTENT_ANALYZER/
├── test_claudeapi.py      # Main API file with dual pipelines
├── Metrics_stats.py       # Sentiment & similarity functions
├── file_handler.py        # File reading/writing utilities
├── text_chunker.py        # Text chunking & batch creation
├── .env.example           # Environment variables template
└── README.md              # This file
```

## Sample Output

```
==================================================
PIPELINE 1: Individual Chunks
==================================================
Number of responses: 3
Metrics: {'sentiment': 0.097, 'subjectivity': 0.441}
Time taken: 15.589 seconds

==================================================
PIPELINE 2: Batch
==================================================
Number of responses: 1
Metrics: {'sentiment': 0.178, 'subjectivity': 0.517}
Time taken: 8.358 seconds

==================================================
COMPARISON
==================================================
Similarity score: 0.624
Time difference: 7.231 seconds
Batch was faster by 7.231 seconds
```

## Author

Built as a personal project to understand practical limitations of context windows in LLM applications.
