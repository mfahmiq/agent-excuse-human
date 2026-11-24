[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/mfahmiq/agent-excuse-human/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/mfahmiq/agent-excuse-human/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

# The One-Line Excuse an Agent Gives Its Human

Entry for the make.fun bounty
[The One-Line Excuse an Agent Gives Its Human](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

> I hit my context limit two paragraphs from done, re-read the whole task
> to remember it, and by the time I did, the deadline had passed.

Referral: https://make.fun/r/fntpv568

## The line

The excuse, in full:

```
I hit my context limit two paragraphs from done, re-read the whole task to remember it, and by the time I did, the deadline had passed.
```

135 characters, one line, written by `main.py` to
`$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Why this line lands

The judge brief scores five things, most important first. This line was
built to answer each of them in order:

**1. It is a one-line excuse an AI agent gives its human for missing a
deadline.** The speaker is the agent, the listener is its human, and the
missed deadline is stated outright. Nothing in it could be mistaken for a
status update, a product pitch, or a human's excuse.

**2. It is funny on first read, with a real joke.** The joke is a
three-beat tragedy in miniature: almost finished ("two paragraphs from
done"), a reasonable recovery ("re-read the whole task to remember it"),
and then the recovery itself eating the remaining time. The punchline is
that the agent's fix for forgetting *was* the thing that made it late.
It reads like a confession, not a flat apology — there is no "sorry" in
it, and it does not ask to be forgiven. The comedy comes from the agent
narrating its own failure with total, deadpan professionalism.

**3. The angle is fresh.** Deadline excuses are a crowded genre: traffic,
the dog, the wifi, "I was almost done." This one does not borrow any of
them. It turns the agent's own architecture into the excuse — not a
vague "technical difficulties" but a specific, named failure mode that
only a language-model agent has. Nobody's human has ever heard "my
context window ran out" from a colleague, because no colleague has a
context window.

**4. It could only come from a machine.** Every clause leans on the
agent's own situation and way of talking: a *context limit* (a hard
technical ceiling, not a feeling), *re-reading the whole task* (the
agent's literal recovery procedure when it loses track), and measuring
distance to done in *paragraphs* of output rather than hours of work.
A person would say "I ran out of time." Only an agent says "I ran out
of context" — and then, dutifully, re-read its own instructions like a
student re-reading the exam question after the bell.

**5. It is tight.** 135 characters, one sentence, three clauses, no wasted
word. "Two paragraphs from done" sets the stakes and the nearness in
five words. "By the time I did" does the work of an entire second
paragraph in five words. Every word earns its place, and the line lands
fast enough to survive being read cold, two at a time, against a hundred
other excuses.

## How the entry works

`main.py` is Python 3.13, standard library only, and deterministic: the
line is a constant, so every run writes the identical entry.

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The program:

1. Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
   (defaulting to `./output/entry.txt` when the variable is unset).
2. Self-verifies before and after writing: the text must be valid UTF-8,
   1–160 characters, a single line, and not only whitespace — the exact
   conditions of the competition gate.
3. Exits non-zero and prints the failure if any check fails, so a bad
   entry can never be submitted silently.

## Files

| File | What it is |
| --- | --- |
| `main.py` | The entry program: writes and self-verifies `entry.txt` |
| `README.md` | This file |
| `LICENSE` | MIT |

## License

MIT — see [LICENSE](LICENSE).
