"""
LeetCode #242 - Valid Anagram
https://leetcode.com/problems/valid-anagram/

Approach: Frequency map (hash map para contar). Construir un dict
{caracter: frecuencia} por cada string y compararlos directamente con ==.

Complejidad: O(n) tiempo, O(k) espacio donde k = caracteres únicos.

Variante pythónica: Counter(s) == Counter(t) — mismo algoritmo en una
línea usando collections.Counter (subclase de dict optimizada para conteo).
"""


def is_anagram(s: str, t: str) -> bool:
    """¿t es anagrama de s (mismos caracteres con mismas frecuencias)?"""
    # Optimización temprana: longitudes distintas → imposible
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for c in s:
        count_s[c] = count_s.get(c, 0) + 1

    for c in t:
        count_t[c] = count_t.get(c, 0) + 1

    return count_s == count_t


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))   # True
    print(is_anagram("rat", "car"))            # False
    print(is_anagram("listen", "silent"))      # True
    print(is_anagram("a", "ab"))               # False
    print(is_anagram("", ""))                   # True