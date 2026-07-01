# 🤖 AI Content Generation Bot

An intelligent content generation system powered by **Claude (Anthropic)** that creates high-quality, customized content across multiple formats using prompt engineering and Generative AI techniques.

---

## 🎯 Features

| Content Type | Description |
|---|---|
| **Blog Post** | SEO-friendly long-form posts with structure |
| **Social Media** | Twitter, LinkedIn & Instagram posts in one shot |
| **Email** | Subject line, preview text, and body |
| **Product Description** | Conversion-focused copy with bullets and CTA |

- 🧠 Powered by Claude claude-sonnet-4-6 (Anthropic)
- 🎨 Adjustable tone: professional, casual, friendly, persuasive
- 📊 Built-in content evaluation (readability, tone, suggestions)
- 💾 Auto-save outputs to `.txt` files
- 🖥️ Interactive CLI interface

---

## 🗂️ Project Structure

```
content-generation-bot/
│
├── content_generator.py   # Core generation + evaluation logic
├── prompts.py             # All prompt templates
├── demo.py                # Full demo of all content types
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository 
```bash
git clone https://github.com/YOUR_USERNAME/content-generation-bot.git
cd content-generation-bot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up API key
```bash
cp .env.example .env
# Edit .env and add your Anthropic API key
```
Get your key at: https://console.anthropic.com/

### 5. Run the bot

**Interactive mode:**
```bash
python content_generator.py
```

**Full demo (all content types):** 
```bash
python demo.py
```

---

## 🧪 How It Works

### Prompt Engineering
Each content type has a tailored prompt template in `prompts.py`. The templates inject:
- **Topic** — what the content is about
- **Tone** — the writing style
- **Extra** — optional additional context

### Content Evaluation
After generation, the bot sends the output back to the model for a structured evaluation:
- Word count
- Readability level (Easy / Medium / Hard)
- Detected tone
- Improvement suggestion

### Iterative Refinement
You can modify prompt templates in `prompts.py` to experiment with different structures and compare outputs — core to prompt engineering learning.

---

## 📋 Concepts Demonstrated

- ✅ **Generative AI & LLMs** — Using Claude for text generation
- ✅ **Prompt Engineering** — Structured, role-based prompts per content type
- ✅ **Multiple Content Types** — Blog, Social, Email, Product
- ✅ **Content Evaluation** — AI self-evaluation loop
- ✅ **Context Management** — System/user message structuring
- ✅ **API Integration** — Anthropic Python SDK
- ✅ **Content Personalization** — Tone + extra context injection
- ✅ **Responsible AI** — No harmful content prompts, clean outputs

---

## 🔧 Customization

To add a new content type:
1. Add a new key to `PROMPT_TEMPLATES` in `prompts.py`
2. The `generate_content()` function automatically supports it

To change the AI model, update the `model` parameter in `content_generator.py`.

---

## 📦 Tech Stack

- **Language:** Python 3.9+
- **AI Provider:** Anthropic (Claude)
- **SDK:** `anthropic` Python package
- **Interface:** CLI (Interactive + Demo modes)

---

## 👤 Author

**Gaurav Singh**  
MBA – AI & Data Science | Graphic Era University  
[GitHub](https://github.com/YOUR_USERNAME)

---

## 📄 License

MIT License — free to use and modify.
