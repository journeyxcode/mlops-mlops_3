[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/xoFPmgXs)
## TMDB 데이터를 활용한 영화 평점 예측 서비스 개발 및 MLOps 파이프라인 구축
## ML 3조

| ![정다영](https://avatars.githubusercontent.com/u/156163982?v=4) | ![박성재](https://avatars.githubusercontent.com/u/156163982?v=4) | ![서효림](https://avatars.githubusercontent.com/u/156163982?v=4) | ![김대섭](https://avatars.githubusercontent.com/u/156163982?v=4) | 
| :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | 
|            [정다영(팀장)](https://github.com/UpstageAILab)             |            [박성재(팀원)](https://github.com/UpstageAILab)             |            [서효림(팀원)](https://github.com/UpstageAILab)             |            [김대섭(팀원)](https://github.com/UpstageAILab)             |            
|                            소스취합, Docker 빌드배포                             |                            소스취합,학습 자동화(Airflow)                            |                            소스취합,학습 자동화(Airflow)                             |                            -                                                         |


## 1. Project Overview
- TMDB 데이터를 활용하여 정보를 모델 학습 및 추론으로 예측 서비스 구축 | MLOps Pipeline 자동화 진행
### 진행방식
* 각자 역활을 정하고, 진행사항을 서로 공유 및 진행사항 체크
* 1단계(MLOps 소스 취합)와 2단계(자동화)로 나누어 진행
* 프로젝트 관리는 노션 진행

### Timeline

- December 17, 2025 - Start Date
- January 02, 2026 - Final submission deadline

## 진행 횟수 및 일정 
- 1단계 : 3 회 이상 진행 ( 12/17 ,19., 22 ) - > 주제, 담당 역할, 진행 방법
- 2단계: 논의할 내용은 팀장 먼저 시작, 날짜 정함 없이 진행 

### 개발환경
*  Ubuntu 24.04 - Ubuntu 설치 후 Docker engine 설치 (컨테이너 기반 환경)
*  Docker (Hub)
*  Python:3.11 - 사용하는 Python 버전
*  Mysql 8
*  Airflow - 데이터 추출부터 평기까지의 자동화 구현
*  Python LIbrary

### 단계별 프로젝트 수행 목표 
- 1단계 : 기능별 모듈화 방식(추론 결과 mysql 로컬 저장), 도커 컨테이너 환경을 동일하게 맞춤
- 2단계 : 데이터 추출부터 평가까지 자동화 구현, 실험 추적(반자동화), 도커 이미지 배포 자동화

## 2. 프로젝트 수행 진행

### Automated Pipeline
- Automated Pipeline：모델학습실행 -> preprocess -> train 순서로실행 (초록색(success)이면정상)

### Docker
- 도커 빌드 환경 구성 : 이미지 배포  -> 도커 허브 업로드 


## 3.  프로젝트진행 내용

### 1단계
- 기능별 소스 모듈화 방식  구현
- 데이터 수집 및 전처리 / 모델 학습 및 평가 / 추론 :  docker run 활용
```text
    // 기본(bash)
    docker run -it --rm --env-file .env --name test -v $(pwd):/opt/mlops mlops-pipeline:latest bash
    // progress
    docker run -it --rm --env-file .env --name test -v $(pwd):/opt/mlops mlops-pipeline:latest preprocess
    // train
    docker run --rm --env-file .env -v $(pwd):/opt/mlops mlops-pipeline:latest train --model_name movie_predictor --num_epochs 20 --batch_size 64
    // inference
    docker run -it --rm --env-file .env --name test -v $(pwd):/opt/mlops mlops-pipeline:latest inference
```
```text
    // preprocess
    docker exec -it test python src/main.py preprocess
    // train
    docker exec -it test python src/main.py train --model_name movie_predictor --num_epochs 50
    // inference
    docker run -it --rm --env-file .env --name test -v $(pwd):/opt/mlops mlops-pipeline:latest inference
```

### 2단계
```text
    docker build --no-cache -t mlops-pipeline:latest .
    process : docker build ->tag 지정 ->  도커허브 login -> 도커 허브업로드 ( 수동)
```

### Docker Hub Info
- Public : https://hub.docker.com/repository/docker/journeyxcode/mlops-pipeline/general

### Docker Files
- Dockerfile
- .dockerignore
- requirements.txt

### Directory

```
├── Dockerfile
├── README.md
├── airflow
│   ├── dags
│   │   └── mlops_train_dag.py
│   ├── logs
│   │   ├── dag_processor_manager
│   │   │   └── dag_processor_manager.log
│   │   └── scheduler
│   │       ├── 2026-01-01
│   │       ├── 2026-01-02
│   │       └── latest -> 2026-01-02
│   └── plugins
├── data-prepare
│   ├── crawler.py
│   ├── main.py
│   ├── preprocessing.py
│   └── result
│       ├── popular.json
│       └── watch_log.csv
├── docker-compose.airflow.yml
├── docker-compose.yml
├── entrypoint.sh
├── models
│   └── movie_predictor
│       ├── E50_T260102021335.pkl
│       └── E50_T260102021335.sha256
├── mysql_data
├── requirements.txt`
├── src
│   ├── dataset
│   │   ├── crawler.py
│   │   ├── data_loader.py
│   │   ├── preprocessing.py
│   │   └── watch_log.py
│   ├── evaluate
│   │   │   └── evaluate.cpython-311.pyc
│   │   └── evaluate.py
│   ├── inference
│   │   │   └── inference.cpython-311.pyc
│   │   └── inference.py
│   ├── main.py
│   ├── model
│   │   └── movie_predictor.py
│   ├── postprocess
│   │   │   └── postprocess.cpython-311.pyc
│   │   └── postprocess.py
│   ├── train
│   │   │   └── train.cpython-311.pyc
│   │   └── train.py
│   └── utils
│       │   ├── enums.cpython-311.pyc
│       │   └── utils.cpython-311.pyc
│       ├── enums.py
│       └── utils.py
└── wandb
```

### Model Deploy

- github Reposigoty - Dockerfile
- dockerhub - image file (manual)

## . 프로젝트수행결과
- 완료 or 일부 진행
    - 기능별 모듈화 구조 방식 진행(추론결과 로컬저장)
    - 도커 컨테이너 환경 환경 구성 및 이미지 배포
    - Airflow를 활용한 Automated Pipeline 일부만 진행 ( preprocess, train )
- 미진행
    - Automated Pipeline 에 과정마다 미진행
    - 도커 이미지 배포 자동화
## etc
### Meeting & Project Progress Log
- 프로젝트 관리 : https://www.notion.so/MLOps-3-2d05a743976581afbbcfcaa7cb89dbc5?pvs=11

### Reference
 - Docker: https://www.docker.com/
 - Docker Hub : https://hub.docker.com/
 - AirFlow : https://airflow.apache.org/
