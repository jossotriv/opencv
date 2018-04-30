string = """
1:00.0: April Johnson
1:02.5: Gary Zhexi Zhang
1:30.0: Vibha Agarwal
1:32.5: Max Allen
1:35.0: Safinah Arshad Ali
1:37.5: Danielle Aspitz
1:40.0: Burhan Azeem
1:42.5: Andrew Bahle
1:45.0: Eghbal Hosseini
1:47.5: Jaclyn Berry
1:50.0: Kyle Branchesi
1:52.5: Agnes Fury Cameron
1:55.0: Elizabeth Carre
1:57.5: Priyanka Chatterjee
2:00.0: Sam Chin
2:02.5: Kyung Yun Choi
2:05.0: Zach Cohen
2:07.5: Joshua Coven
2:10.0: Pinar Yanardag
2:12.5: Honghao Deng
2:15.0: Julia Ebert
2:17.5: Casey Evans
2:20.0: Lily Gabaree
2:22.5: Erin Genia
2:25.0: Joel Gustafson
2:27.5: Keitaro Bando
2:30.0: Sean Hickey
2:32.5: Alexandre Kaspar
2:35.0: Jordan Kennedy
2:37.5: Seowoo Kim
2:40.0: Elysa Kohrs
2:42.5: break
2:45.0: break
2:47.5: break
2:50.0: Akshata Krishnamurthy
2:52.5: Natalie Lao
2:55.0: Chastity Li
2:57.5: Jiabao Li
3:00.0: Richard Liu
3:02.5: Daniel Marshall
3:05.0: Soma Mitra-Behura
3:07.5: Richard Park
3:10.0: Vik Parthiban
3:12.5: Eleanor Pence
3:15.0: Rui Qing
3:17.5: Jake Read
3:20.0: Oscar Rosello
3:22.5: Emily Salvador
3:25.0: Samuel Schneider
3:27.5: Darle Shinsato
3:30.0: George Sun
3:32.5: Robert Tran
3:35.0: Niki Tubacki
3:37.5: Tomás Vega
3:40.0: Nikita Waghani
3:42.5: Anna Waldman-Brown
3:45.0: Jessica Wang
3:47.5: Yanru Wang
3:50.0: Kate Weishaar
3:52.5: Jeremy Welborn
3:55.0: Xin Wen
3:57.5: Diana Yan
4:00.0: Takatoshi Yoshida
4:02.5: Ben Z Yuan
4:05.0: Diana Zwetzich"""

list_ = string.split()
listz = list(zip(list_[0::3],list_[1::3],list_[2::3]))
print(listz)
print(len(listz)-3)
