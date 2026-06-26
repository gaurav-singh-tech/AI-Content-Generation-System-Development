"""
Prompt Templates for AI Content Generation Bot
Each template supports: topic, tone, extra (additional context)
"""

PROMPT_TEMPLATES = {
    "blog": """You are an expert blog writer. Write a complete blog post with the following specs:

Topic: {topic}
Tone: {tone}
Additional Instructions: {extra}

Structure:
- Catchy Title
- Introduction (hook + thesis)
- 3 main sections with subheadings
- Conclusion with a call to action

Make it engaging, SEO-friendly, and around 400-500 words.""",

    "social": """You are a social media content strategist. Create a social media content package:

Topic: {topic}
Tone: {tone}
Additional Instructions: {extra}

Deliver:
1. Twitter/X post (max 280 chars) with hashtags
2. LinkedIn post (professional, 150-200 words)
3. Instagram caption (engaging, with emojis and hashtags)

Each should be platform-appropriate and drive engagement.""",

    "email": """You are an expert email copywriter. Write a compelling email:

Topic/Purpose: {topic}
Tone: {tone}
Additional Instructions: {extra}

Include:
- Subject Line (punchy, <60 chars)
- Preview Text (1 sentence)
- Email Body (greeting, value, CTA, sign-off)

Keep it concise, personal, and action-oriented.""",

    "product": """You are a product copywriting specialist. Write persuasive product content:

Product/Topic: {topic}
Tone: {tone}
Additional Instructions: {extra}

Include:
- Product Headline
- Short Description (2-3 sentences, benefits-focused)
- 5 Key Feature Bullets (outcome-oriented)
- Call to Action

Focus on benefits over features. Make it conversion-focused.""",
}
