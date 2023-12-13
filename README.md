# Lorem English Generator

This Python script generates pseudo-English words based on a simple syllable structure. It utilizes a combination of consonants (souhlasky) and vowels (samohlasky) to construct words. The user can specify the number of words to generate.
 when prompted.

## Syllable Structure

The script follows various syllable structures, defined as follows:

- **"CV"**: Consonant followed by a vowel.
- **"CVCV"**: Consonant followed by a vowel, followed by another consonant and another vowel.
- **"CCV"**: Two consecutive consonants followed by a vowel.
- **"CVC"**: Consonant followed by a vowel, followed by another consonant.

## Premade Words

The script includes a set of premade words that may appear with a certain probability instead of following the defined syllable structures.

## Configuration

You can modify the weights assigned to consonants (`cons_w`) and vowels (`vowe_w`) to affect the frequency of their occurrence in the generated words; the letter weights are basically the same as in real English. In addition, you can extend the list of `premade_words` with your own words.

## Sources

Frequency of monosyllables: https://www.sttmedia.com/characterfrequency-english
