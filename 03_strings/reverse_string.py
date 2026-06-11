"""
LeetCode #344 - Reverse String
https://leetcode.com/problems/reverse-string/

Approach: Two pointers desde extremos opuestos, swap in-place.
Complejidad: O(n) tiempo, O(1) espacio.

Nota: En código de producción, usar list.reverse() (optimizado en C).
Aquí se implementa manual con fines didácticos (entender el patrón).
"""


def reverse_string(s: list[str]) -> None:
    """Invierte la lista de caracteres in-place."""
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    print(s)  # ['o', 'l', 'l', 'e', 'h']

    s = ["H"]
    reverse_string(s)
    print(s)  # ['H']

    s = []
    reverse_string(s)
    print(s)  # []