#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorielle(n):
    if n < 2:
        return 1
    else:
        return n * factorielle(n - 1)


if __name__ == '__main__':
    nb = int(input("Entrer un nombre entier positif : "))
    fact_nb = factorielle(nb)
    print(f"La factorielle de {nb} vaut {fact_nb}.")


# Commentaires en Python


