# Arabic reels: rules

For pages whose `page.md` Language includes Arabic. These hold for any dialect; the dialect itself comes from `page.md`.

## Words

- **Spoken lines in the page's dialect** (Gulf, Egyptian, Levantine…), the way the user really talks. Have the user read the script aloud once and change any line that doesn't sound like them.
- **On-screen text** can sit a little closer to standard Arabic so every Arab viewer reads it fast, but stay in the same register as the voice. Don't mix dialects in one reel.
- **Hooks run longer in Arabic.** For the claim to land by 1.6 s, keep it to 3 to 6 words. Put the subject first, as the `virality` checklist asks.
- **Digits:** choose Western (0 to 9) or Arabic-Indic (٠ to ٩) once, write it in `page.md`, and use it everywhere: screen, cover, captions. Western digits are common in Gulf social content.
- **Currency:** the audience's own (SAR, AED, KWD…), written the same way every time (ريال or SAR, not both).
- **Punctuation:** Arabic comma ، and question mark ؟.

## Type on screen

- Never add letter-spacing: it breaks the joins between letters.
- No fake italics or all-caps effects. Use weight and colour for emphasis.
- Line height 1.3 or more; Arabic needs room above and below.
- Leave out tashkeel (vowel marks) except where a word would be misread; a shadda is fine.
- Never break a word across lines. Keep 2 to 4 words per line for big text.
- Right-aligned. Fonts: Noto Kufi Arabic for display, IBM Plex Sans Arabic for text (both in `assets/fonts/`).
- Mixed runs (an English brand name, a handle, a price with a Latin currency code) go in their own `<bdi>` element or a `dir="ltr"` span, so they don't scramble the line.

## Captions and hashtags (the post text)

- Follow the caption languages in `page.md`. If there's an English first line, give it its own line, then the Arabic below. Start each line in its own language so the text direction doesn't flip mid-line.
- The first line carries the main search keyword.
- Arabic hashtags join words with underscores: `#تسعير_التصميم`. Mix 2 or 3 Arabic hashtags with 1 or 2 English ones if the audience searches in both.

## Comment-keyword CTA

Pick one exact keyword. If it's Arabic, accept its Latin version too (سعر or PRICE), and tell whoever sends the DMs to accept both.

## Voice

The user's own voice is best. ElevenLabs has Arabic voices, but dialect accuracy varies: if one is used, have the user listen for wrong words or accent before it's rendered.
