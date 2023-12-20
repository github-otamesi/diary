from diaries.DiarySample import DiarySample
from diaries.ShimokawaDiary2 import DiaryShimokawa
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           DiaryShimokawa(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
