import random
import tkinter

a = random.randint(1,2)
b = input("Орёл или решка?: ")

if b == "орёл" and a == 1:
  print("Орёл, вы выйграли!!!")

if b == "решка" and a == 2:
  print("Решка, вы выйграли!!!")

if b == "орёл" and a == 2:
  print("Решка, вы проиграли! Не огорчайтесь, повезёт в следуйщий раз")

if b == "решка" and a == 2:
  print("Орёл, вы проиграли! Не огорчайтесь, повезёт в следуйщий раз")
