#!/usr/bin/env python
# -*- coding: utf-8 -*-

annee = int(input("Entrez l' année a verifier :"))

if(annee%4==0 and annee%100!=0 or annee%400==0):
    print("L'année est une annee bissextile !!")
else:
    print("L'année n'est pas une annee bissextile !!")