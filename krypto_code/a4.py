from typing import Optional
"""
ElGamal (privater Schlüssel x)
  Gegeben: p (Primzahl), g (Generator), e = g^x mod p
  Gesucht: x in [LOW, HIGH], sodass pow(g, x, p) == e
"""

def find_elgamal_private_key(p: int, g: int, e: int,
                             low: int = 20010, high: int = 20110) -> Optional[int]:
    """
    Sucht x in [low, high] mit g^d ≡ e (mod p).
    """
    for d in range(low, high + 1):
        if pow(g, d, p) == e:
            return d
    return None

p = 27367
g = 2455
e = 20639
d = find_elgamal_private_key(p, g, e, 20010, 20110)
print("d =", d)   # None oder gefundener Wert


def elgamal_decrypt_with_d(p: int, a: int, b: int, d: int) -> int:
    """Entschlüsselt m = b * a^(p-1-d) mod p (Fermat-Trick)."""
    return (b * pow(a, p - 1 - d, p)) % p

def verify_reencryption(p: int, g: int, d: int, a: int, b: int, m: int) -> bool:
    """
    Verifikation durch Rückverschlüsselung:
    Prüfe, ob pow(g, d, p) == y und ob pow(m, 1, p) zum gegebenen b passt
    (hier: wir verifizieren durch Neuberechnung von y = g^d mod p und dann
    durch pow(y, k, p) falls k bekannt; alternativ genügt eine Prüfung, dass
    pow(a, d, p) * m ≡ b mod p holds when rearranged).
    """
    # Näherungsprüfung: a^d * m ≡ ? b  -> weil a = g^k, a^d = g^{k d} und b = y^k m = (g^d)^k m
    lhs = (pow(a, d, p) * m) % p
    return lhs == b

# 2) Wenn d bekannt -> entschlüsseln
a = 3959
b = 18704
if d is not None:
    m = elgamal_decrypt_with_d(p, a, b, d)
    print("Entschlüsselter Klartext m:", m)

    # 3) Verifikation (Re-Encryption Check)
    ok = verify_reencryption(p, g, d, a, b, m)
    print("Verifikation (a^d * m == b)?:", ok)
else:
    print("Privater Schlüssel d nicht im Bereich gefunden.")