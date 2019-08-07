# 현금 인출기★★
money = int (input("인출 금액 (1천 단위 이상으로) : "))

m50000 = money // 50000    # 5만원짜리 
money = money % 50000       # 남은 돈

m10000 = money // 10000    # 1만원짜리
money = money % 10000       # 남은 돈

m5000 = money // 5000      # 5천원짜리
money = money % 5000        # 남은 돈

m1000 = money // 1000      # 1천원짜리                

print()
print("=" * 15)
print("인출내역:")
print("5만원 - ", m50000, "장")
print("1만원 - ", m10000, "장")
print("5천원 - ", m5000, "장")
print("1천원 - ", m1000, "장")
      
