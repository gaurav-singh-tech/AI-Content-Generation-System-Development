"""
demo.py - Demonstrates all content types with sample outputs
Run this to showcase the bot to evaluators/professors.
"""

from content_generator import generate_content, evaluate_content

DEMO_CASES = [
    {
        "content_type": "blog",
        "topic": "The Future of AI in Healthcare",
        "tone": "professional",
        "extra": "Target audience: medical professionals and tech enthusiasts"
    },
    {
        "content_type": "social",
        "topic": "Launch of a new productivity app",
        "tone": "casual",
        "extra": "Focus on saving time and reducing stress"
    },
    {
        "content_type": "email",
        "topic": "Re-engaging inactive newsletter subscribers",
        "tone": "friendly",
        "extra": "Offer a free resource as incentive to return"
    },
    {
        "content_type": "product",
        "topic": "Smart Water Bottle with hydration tracking",
        "tone": "persuasive",
        "extra": "Highlight health benefits and connectivity features"
    },
]


def run_demo():
    print("\n" + "=" * 60)
    print("   AI CONTENT GENERATION BOT — FULL DEMO")
    print("=" * 60)

    for i, case in enumerate(DEMO_CASES, 1):
        print(f"\n{'=' * 60}")
        print(f"DEMO {i}: {case['content_type'].upper()} — {case['topic']}")
        print(f"Tone: {case['tone']}")
        print("=" * 60)

        try:
            content = generate_content(
                content_type=case["content_type"],
                topic=case["topic"],
                tone=case["tone"],
                extra=case["extra"]
            )
            print(content)

            # Evaluate each output
            print("\n--- Content Evaluation ---")
            evaluation = evaluate_content(content)
            for k, v in evaluation.items():
                print(f"  {k.title()}: {v}")

            # Save each output
            filename = f"demo_output_{case['content_type']}.txt"
            with open(filename, "w") as f:
                f.write(f"Type: {case['content_type'].title()}\n")
                f.write(f"Topic: {case['topic']}\n")
                f.write(f"Tone: {case['tone']}\n\n")
                f.write(content + "\n\n")
                f.write("--- Evaluation ---\n")
                for k, v in evaluation.items():
                    f.write(f"{k.title()}: {v}\n")
            print(f"\n✅ Saved: {filename}")

        except Exception as e:
            print(f"❌ Error in demo {i}: {e}")

    print("\n" + "=" * 60)
    print("   DEMO COMPLETE - All content types demonstrated!")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
