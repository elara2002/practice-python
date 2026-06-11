"""
LeetCode #125 - Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Approach: Pre-procesar el string filtrando alfanuméricos y convirtiendo
a lowercase, después aplicar two pointers desde extremos opuestos.

Complejidad: O(n) tiempo, O(n) espacio (por el string limpio).

Variante O(1) espacio: saltar caracteres no válidos in-stream con
nested while loops. Más eficiente en memoria pero menos legible.
"""


def is_palindrome(s: str) -> bool:
    """¿Es palíndromo, ignorando case y caracteres no alfanuméricos?"""
    limpio = "".join(c.lower() for c in s if c.isalnum())

    l, r = 0, len(limpio) - 1
    while l < r:
        if limpio[l] != limpio[r]:
            return False
        l += 1
        r -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                       # False
    print(is_palindrome(" "))                                # True
    print(is_palindrome("racecar"))                          # True
    print(is_palindrome("hello"))                            # False
    print(is_palindrome(""))                                 # True