Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # 파일이름 : 2차과제
... # 작 성 자 : 장서윤
... print("소개팅 애프터 성공률 분석 시스템")
... print("=" * 50)
... 
... portfolio = []
... 
... for i in range(3):
...     print(f"\n[{i+1} 번째 소개팅 데이터 입력]")
...     
...         name = input("상대방 이름: ")
...         
...         response_speed = float(input("답장 속도 (1: 빠름 ~ 10: 느림): "))
...         if response_speed < 1 or response_speed > 10:
...             print("1~10 사이 값만 입력하세요. 다시 입력!")
...             continue
... 
...         chat_time = float(input("대화 시간(시간): "))
...         emoticon = int(input("이모티콘 빈도 (1~10): "))
... 
...         target = []
...         portfolio.append(target)
...         portfolio.append(response_spped)
...         portfolio.append(chat_time)
...         portfolio.append(emoticon)
... 
...         portfolio.append(target)
... 
... print(f"\n총 입력된 데이터 수: {len(portfolio)} 명")
... print("\n결과 분석 시작\n")
... 
... scores = []
... for person in portfolio:
...     name = person[0]
...     speed = person[1]
...     time = person[2]
...     emo = person[3]

    time = min(time, 5)
    emo = min(emo, 10)
    speed = max(1, min(speed, 10))

    raw_score = (0)
    raw_score += time * 2.0
    raw_score += emo * 0.3
    raw_score += (10 - speed) * 0.3
    
    max_score = 16
    score = (raw_score / max_score) * 10

    scores.append(score)

  
    if score >= 9:
        grade = "S급"
    elif score >= 8:
        grade = "A급"
    elif score >= 7:
        grade = "B급"
    elif score >= 6:
        grade = "C급"
    else:
        grade = "D급"

    print(f"{name} 님의 애프터 지수: {score:.1f} / 10 → {grade}")

  
    if score >= 8:
        if speed <= 3 and emo >= 7:
            print("핑크빛 고속도로")
    
    if score > 9.5:
        print(f"거의 성공 확정! 분석종료")
        break

print("\n 전체 통계")
print(f"최고 점수: {max(scores):.1f}")
