"""
AI Content Generation Bot
Supports: Blog Posts, Social Media, Emails, Product Descriptions
"""

import anthropic
import os
from prompts import PROMPT_TEMPLATES


def get_client():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set in environment variables.")
    return anthropic.Anthropic(api_key=api_key)


def generate_content(content_type: str, topic: str, tone: str = "professional", extra: str = "") -> str:
    """
    Generate content based on type, topic, tone, and optional extras.

    Args:
        content_type: One of 'blog', 'social', 'email', 'product'
        topic: Subject or theme of the content
        tone: Writing tone (professional, casual, friendly, persuasive)
        extra: Any additional context or instructions

    Returns:
        Generated content as a string
    """
    client = get_client()

    if content_type not in PROMPT_TEMPLATES:
        raise ValueError(f"Unsupported content type: {content_type}. Choose from: {list(PROMPT_TEMPLATES.keys())}")

    prompt = PROMPT_TEMPLATES[content_type].format(topic=topic, tone=tone, extra=extra)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text


def evaluate_content(content: str) -> dict:
    """
    Evaluate generated content for quality metrics.

    Returns:
        dict with keys: word_count, readability, suggestions
    """
    client = get_client()

    eval_prompt = f"""Evaluate the following content and respond in this exact format:

WORD_COUNT: <number>
READABILITY: <Easy/Medium/Hard>
TONE: <detected tone>
SUGGESTIONS: <one sentence suggestion to improve>

Content:
{content}"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[
            {"role": "user", "content": eval_prompt}
        ]
    )

    raw = message.content[0].text
    result = {}
    for line in raw.strip().splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            result[key.strip().lower()] = val.strip()
    return result


def run_interactive():
    """Interactive CLI for the content bot."""
    print("\n" + "=" * 50)
    print("   AI Content Generation Bot")
    print("=" * 50)

    content_types = {"1": "blog", "2": "social", "3": "email", "4": "product"}
    tones = ["professional", "casual", "friendly", "persuasive", "formal"]

    print("\nContent Types:")
    for k, v in content_types.items():
        print(f"  {k}. {v.title()}")

    choice = input("\nSelect content type (1-4): ").strip()
    content_type = content_types.get(choice)
    if not content_type:
        print("Invalid choice. Exiting.")
        return

    topic = input("Enter topic/subject: ").strip()
    if not topic:
        print("Topic cannot be empty.")
        return

    print(f"\nTones: {', '.join(tones)}")
    tone = input("Enter tone (default: professional): ").strip() or "professional"

    extra = input("Any extra instructions (optional, press Enter to skip): ").strip()

    print("\n⏳ Generating content...\n")

    try:
        content = generate_content(content_type, topic, tone, extra)
        print("=" * 50)
        print("GENERATED CONTENT:")
        print("=" * 50)
        print(content)

        evaluate = input("\nEvaluate this content? (y/n): ").strip().lower()
        if evaluate == "y":
            print("\n⏳ Evaluating...\n")
            evaluation = evaluate_content(content)
            print("=" * 50)
            print("CONTENT EVALUATION:")
            print("=" * 50)
            for k, v in evaluation.items():
                print(f"  {k.title()}: {v}")

        save = input("\nSave content to file? (y/n): ").strip().lower()
        if save == "y":
            filename = f"output_{content_type}_{topic[:20].replace(' ', '_')}.txt"
            with open(filename, "w") as f:
                f.write(f"Content Type: {content_type.title()}\n")
                f.write(f"Topic: {topic}\n")
                f.write(f"Tone: {tone}\n")
                f.write("=" * 50 + "\n")
                f.write(content)
            print(f"✅ Saved to {filename}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    run_interactive()
