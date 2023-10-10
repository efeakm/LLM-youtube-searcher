# YouTube Video Info Fetcher 🎬

Welcome to the **YouTube Video Info Fetcher!** This web app, developed using Streamlit, is a testament to the integration of advanced language model capabilities with web development. Utilizing the **"langchain"** library, the app leverages the power of Large Language Models (LLMs) to interpret and generate responses based on user input. A key feature is the integration of the **ZERO_SHOT_REACT_DESCRIPTION agent** and **langchain Youtube Tool**, which augments the LLM's capabilities, allowing it to produce even more nuanced and contextually relevant results.  Dive in to explore the convergence of LLMs, web development, and YouTube data retrieval!

![Demo Screenshot](Screenshot_1.png) 

## Features 🌟

- Input a custom prompt to search for videos.
- Fetches details like:
  - Video Name
  - View Count
  - Like Count
  - Thumbnail (which is also a clickable link to the actual video)
  
## Prerequisites 📝

Ensure you have the following installed on your local machine:

- Python 3.x
- pip

## Setup and Installation ⚙️

1. **Clone the repository:**

   ```
   git clone https://github.com/efeakm/LLM-youtube-searcher.git
   cd LLM-youtube-searcher
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**

   ```
   streamlit run app.py
   ```

   This will open a new tab in your web browser with the app running.

## Contributing 🤝

Feel free to open issues or PRs if you want to contribute to the project! 

## License 📄

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details.
