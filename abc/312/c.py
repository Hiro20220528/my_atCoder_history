N, M = map(int, input().split())


seller_list = list( map( int, input().split() ) )
s_tmp = [0] * N

buyer_list = list(map(int, input().split()))
b_tmp = [1] * M

seller_list.sort()
buyer_list.sort()

all_list = [_ for _ in range(N+M)] 

for s, i in enumerate(zip(seller_list, s_tmp)):
          # print(s, i)
          
          all_list[s] = i
          

for b, i in enumerate(zip(buyer_list, b_tmp)):
          all_list[N+b] = i


# print(len(all_list), N, M)
# print(all_list)

all_list.sort()
# print(all_list)

seller_count = 0
buyer_count = 0
for price in all_list:
          # seller
          if price[1] == 0:
                    seller_count += 1
                    # print(price[0], '以上で売りたい')
                    # 90円以下の人
          # buyer
          else:
                    buyer_count += 1
          
          # buyerの人数
          num_buyer = M - buyer_count
          
          
          if seller_count >= num_buyer:
                    print(price[0])
                    print(seller_count, num_buyer, price)
                    break