"""
Day 1 - LLM API Foundation
AICB-P1: AI Practical Competency Program, Phase 1
"""

import os
import sys
import time
from typing import Any, Callable

COST_PER_1K_OUTPUT_TOKENS = {
    "gpt-4o": 0.010,
    "gpt-4o-mini": 0.0006,
}

OPENAI_MODEL = "gpt-4o"
OPENAI_MINI_MODEL = "gpt-4o-mini"


def _openai_client():
    from openai import OpenAI

    kwargs = {"api_key": os.getenv("OPENAI_API_KEY")}
    base_url = os.getenv("OPENAI_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


def call_openai(
    prompt: str,
    model: str = OPENAI_MODEL,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    """
    Call the OpenAI-compatible Chat Completions API and return response text
    plus measured latency.
    """
    client = _openai_client()
    start_time = time.perf_counter()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )
    latency = max(time.perf_counter() - start_time, sys.float_info.epsilon)
    content = response.choices[0].message.content or ""
    return content, latency


def call_openai_mini(
    prompt: str,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    """Call the cheaper GPT-4o-mini model."""
    return call_openai(
        prompt,
        model=OPENAI_MINI_MODEL,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )


def compare_models(prompt: str) -> dict:
    """Compare GPT-4o and GPT-4o-mini responses, latency, and estimated cost."""
    gpt4o_response, gpt4o_latency = call_openai(prompt)
    mini_response, mini_latency = call_openai_mini(prompt)

    estimated_output_tokens = len(gpt4o_response.split()) / 0.75
    gpt4o_cost_estimate = (
        estimated_output_tokens
        / 1000
        * COST_PER_1K_OUTPUT_TOKENS["gpt-4o"]
    )

    return {
        "gpt4o_response": gpt4o_response,
        "mini_response": mini_response,
        "gpt4o_latency": gpt4o_latency,
        "mini_latency": mini_latency,
        "gpt4o_cost_estimate": gpt4o_cost_estimate,
    }


def streaming_chatbot() -> None:
    """
    Run an interactive streaming chatbot in the terminal.

    Keeps the last 3 conversation turns, where each turn is a user message and
    its assistant reply.
    """
    client = _openai_client()
    history: list[dict[str, str]] = []

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            return
        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})
        messages = history[-6:]
        stream = client.chat.completions.create(
            model=OPENAI_MINI_MODEL,
            messages=messages,
            temperature=0.7,
            top_p=0.9,
            max_tokens=256,
            stream=True,
        )

        print("Assistant: ", end="", flush=True)
        assistant_parts: list[str] = []
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            if delta:
                print(delta, end="", flush=True)
                assistant_parts.append(delta)
        print()

        history.append({"role": "assistant", "content": "".join(assistant_parts)})
        history = history[-6:]


def retry_with_backoff(
    fn: Callable,
    max_retries: int = 3,
    base_delay: float = 0.1,
) -> Any:
    """Run fn with exponential backoff and raise the last exception on failure."""
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except Exception:
            if attempt == max_retries:
                raise
            time.sleep(base_delay * (2 ** attempt))

    raise RuntimeError("unreachable retry state")


def batch_compare(prompts: list[str]) -> list[dict]:
    """Run compare_models for every prompt and include the original prompt."""
    results = []
    for prompt in prompts:
        result = compare_models(prompt)
        result["prompt"] = prompt
        results.append(result)
    return results


def _truncate(value: Any, width: int = 40) -> str:
    text = str(value)
    if len(text) <= width:
        return text
    return text[: width - 3] + "..."


def format_comparison_table(results: list[dict]) -> str:
    """Format comparison results as a readable fixed-width text table."""
    headers = [
        "Prompt",
        "GPT-4o Response",
        "Mini Response",
        "GPT-4o Latency",
        "Mini Latency",
    ]
    rows = []
    for result in results:
        rows.append(
            [
                _truncate(result.get("prompt", "")),
                _truncate(result.get("gpt4o_response", "")),
                _truncate(result.get("mini_response", "")),
                f"{result.get('gpt4o_latency', 0):.2f}s",
                f"{result.get('mini_latency', 0):.2f}s",
            ]
        )

    table = [headers, *rows]
    widths = [max(len(row[index]) for row in table) for index in range(len(headers))]

    def format_row(row: list[str]) -> str:
        return " | ".join(value.ljust(widths[index]) for index, value in enumerate(row))

    lines = [format_row(headers)]
    lines.append("-+-".join("-" * width for width in widths))
    lines.extend(format_row(row) for row in rows)
    return "\n".join(lines)


_TEST_MODULE_ALIAS = "solution_alias"
sys.modules[_TEST_MODULE_ALIAS] = sys.modules[__name__]
for _function in (
    call_openai,
    call_openai_mini,
    compare_models,
    streaming_chatbot,
    retry_with_backoff,
    batch_compare,
    format_comparison_table,
):
    _function.__module__ = _TEST_MODULE_ALIAS


if __name__ == "__main__":
    test_prompt = "Explain the difference between temperature and top_p in one sentence."
    print("=== Comparing models ===")
    result = compare_models(test_prompt)
    for key, value in result.items():
        print(f"{key}: {value}")

    print("\n=== Starting chatbot (type 'quit' to exit) ===")
    streaming_chatbot()
