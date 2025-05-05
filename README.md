# 📡 streamlit_about: 
# RAG-Powered Personal Knowledge App
## 🧠 Overview

`streamlit_about` is an open-source application that showcases a [Retrieval-Augmented Generation](https://cloud.google.com/use-cases/retrieval-augmented-generation) (RAG) system, delivering personalized Question and Answer (Q\&A) experiences about Miklós. Written in [Python](https://www.python.org), it integrates modern [Natural Language Processing](https://aws.amazon.com/what-is/nlp/) (NLP) techniques, vector search, and modular backend design to provide an interactive and informative user experience.

- **Live App**: [about-miklos.streamlit.app](https://about-miklos.streamlit.app/)
- **Source Code**: [github.com/ikko/streamlit\_about](https://github.com/ikko/streamlit_about)
- **Contact**: [linkedin.com/in/miklosbeky](https://www.linkedin.com/in/miklosbeky/)

## 🔍 Key Features

### 1. 🧮 **Retrieval-Augmented Generation (RAG) System**

Combines vector-based semantic search with generative AI to provide accurate and contextually relevant answers.

* **Vector Store**: Utilizes [FAISS](https://github.com/facebookresearch/faiss/wiki) for efficient similarity search.
* **BM25 Indexing**: Employs [Best Matching 25](https://en.wikipedia.org/wiki/Okapi_BM25) (BM25) algorithm for keyword-based retrieval.
* **Metadata Management**: Stores and retrieves document metadata for enhanced context.

### 2. ⚖️ **Modular Backend Architecture**

Structured for scalability and maintainability, separating concerns across different modules.

* **Knowledge Base**: Handles data ingestion and vector index creation.
* **Backend Logic**: Manages query processing and response generation.
* **Dynamic Pages**: Generates content-rich pages dynamically based on user interactions.

### 3. 🛸 **Interactive Streamlit Frontend**

Leverages [Streamlit](https://streamlit.io/)'s capabilities to create an intuitive and responsive user interface.

* **Dynamic Content**: Updates in real-time based on user queries.
* **AI Generated Knowledge Base**: [Unuspervisied Learning enabled Clustering](https://developers.google.com/machine-learning/clustering/overview) of the Knowledge Topics and Large Language Model generated Q&A ensures generalized, easy to adopt and delicate articulate content.
* **Multi-Page Navigation**: Organizes content across multiple pages for better UX.

### 4. 🔬 **Efficient Deployment**

Designed for seamless deployment and scalability.

* **Streamlit Sharing**: Easily deployable via [Streamlit's sharing platform](https://streamlit.io/community).
* **Development**: Includes handy scripts for streamlined local deployment.
* **Requirements Management**: Specifies dependencies for reproducibility.

---

## 🧱 Architectural Patterns & Methodologies

### Retrieval-Augmented Generation (RAG)

Integrates information retrieval with generative models to enhance response accuracy. This hybrid approach ensures that generated answers are grounded in factual data.

### Modular Design

Adopts a clear [separation of concerns](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles#separation-of-concerns), facilitating easier **maintenance** and **scalability**. Each module handles a specific responsibility, promoting code clarity.

### Streamlit for Rapid Prototyping

Utilizes Streamlit to quickly develop and deploy interactive web applications, reducing the time **from concept to deployment**.

### Vector Search with FAISS

Employs FAISS for **high-speed** [similarity searches](https://medium.com/@serkan_ozal/vector-similarity-search-53ed42b951d9) in large datasets, enabling efficient retrieval of relevant information.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher
* pip package manager

### Installation

```bash
git clone https://github.com/ikko/streamlit_about.git
cd streamlit_about
pip install -r requirements.txt
```

### Running the Application

```bash
bash start.sh
```

This will launch the Streamlit app locally.

## 📁 Project Structure

```
streamlit_about/
├── accomplishments/           # Content related to achievements
├── backend/                   # Backend logic and processing
├── dynamic_pages/             # Dynamically generated pages
├── images/                    # Static images used in the app
├── pages/                     # AI generated pages
├── Knowledge_Base.py          # Handles data ingestion and indexing
├── rag_bm25result.pickle      # Serialized BM25 index
├── rag_openai_faiss.index     # FAISS vector index
├── rag_openai_metadata.json   # Metadata for indexed documents
├── requirements.txt           # Python dependencies
├── start.sh                   # Startup script for the app
├── style.css                  # Custom CSS styling
└── README.md                  # Project documentation
```

---

* **Hybrid Retrieval Techniques**: Combining BM25 and vector search offers a balance between keyword matching and semantic understanding.
* **Modular Architecture**: Facilitates experimentation with different components, such as swapping out the vector store or language model.
* **Streamlit Integration**: Demonstrates how to build user-friendly interfaces for complex AI systems without extensive frontend development.
* **Scalability Considerations**: The separation of backend logic and frontend presentation allows for scaling individual components as needed.

For any inquiries or contributions, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/miklosbeky).

---

## MIT Licence

Copyright (c) 2025 Miklós Béky
 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 
---
