'''
- 파이썬 오퍼레이터와 연결된 콜백 함수 내부 연산의 결과로 조건부로 task를 선택하여 진행
- 의존성 컨트롤, 조건부 task 수행 -> 브런치(가지치기)
- 의존성 구성에서 여러 시나리오 작성
'''
# 1. 모듈
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator # 조건부 선택
from airflow.operators.empty import EmptyOperator
from airflow.utils.trigger_rule import TriggerRule # 성공, 실패, 등등 조건 설정
from datetime import datetime, timedelta
import logging
import pendulum
import random

# 2. 전역변수
KST = pendulum.timezone("Asia/Seoul")

# 4-1. 콜백함수

# 3. DAG
with DAG( 
  dag_id      = "04_basics_branching",
  description = "분기 처리, 선택적 TASK 구동",
  default_args= {
    "owner"           : "aic-de1-admin",    
    "retries"         : 1,
    "retry_delay"     : timedelta(minutes=1)
  },
  schedule_interval = "@daily",  
  start_date  = pendulum.datetime( 2026,6,29, tz=KST ),
  catchup     = False,
  tags        = ['branch', 'trigger_rule']
) as dag:

  # 4. 오퍼레이터를 이용하여 task를 정의
  
  # 5. 의존성(수행순서)  