
---

# Text Classification ML Model

## Overview
This is a Streamlit web application that utilizes a pre-trained text classification model to predict emotions associated with input text. The model used in this application is the `roberta-base-go_emotions` model from Hugging Face's Transformers library.

## Features
- Allows users to input text for emotion classification.
- Displays the predicted emotions along with their corresponding scores.
- Provides a user-friendly interface for interacting with the model.

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/RamRajurkar/Text-Classification-Model.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Text-Classification-Model
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app locally:
   ```bash
   streamlit run app.py
   ```
2. Access the app in your web browser at the provided local address.

## Configuration
- You need to set up an API key for authentication with the Hugging Face model server. Set the `API_KEY` environment variable with your API key.

## Contributors
- [Ram Rajurkar (Admin)](https://github.com/RamRajurkar)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Feel Free to Contribute
Your contributions are always welcome! Feel free to fork the repository and submit pull requests with your changes. Together, we can make this project even better!

---
