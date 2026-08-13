'''
- 평가를 해야하는 고객 데이터 구조(요쳥/응답)
  - [ {}, {}, ... ]
'''
# 1. 모듈 가져오기
from fastapi import FastAPI     # 앱
from pydantic import BaseModel  # 요쳥/응답 클레스 구성시 수퍼클레스 역활
from typing import List         # 요청/응답 데이터 구성시 구조 정의시 사용
import random                   # 신용평가시 활용

# 2. FastAPI 객체 생성

# 3. 요청/응답 구조 정의 => class

# 4. 라우팅 : url, 처리함수 매핑 정의