# BookBot

BookBot is a text analysis tool that analyzes text files and provides word count and character frequency statistics.

## Features

- Count the total number of words in a text file
- Analyze character frequency (letters only)
- Sort characters by frequency in descending order
- Command-line interface for easy usage

## Usage

Run the program by providing the path to the text file you want to analyze:

```bash example
python main.py books/frankenstein.txt
```

## Project Structure

- `main.py`: Entry point of the application
- `stats.py`: Contains text analysis functions
- `/books`: Directory containing sample books for analysis

## Sample Books

The repository includes several classic texts for analysis:
- Frankenstein
- Moby Dick
- Pride and Prejudice
