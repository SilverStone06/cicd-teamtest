# git-cicd-study-teamtest

FastAPI/Nginx 애플리케이션을 Docker로 빌드해 AWS ECR에 푸시하고, Private EC2에 SSM으로 배포하는 리포지토리입니다.

## 구성
- `fastapi-private`: FastAPI 애플리케이션
- `nginx-private`: 정적 페이지 + `/api/` 프록시 Nginx 설정
- `.github/workflows`: ECR/SSM 기반 파이프라인

## 워크플로우
- `fastapi-flow.yml`: ECR 로그인 → 이미지 빌드/푸시(커밋 SHA, latest) → SSM 배포
- `nginx-flow.yml`: ECR 로그인 → 이미지 빌드/푸시(커밋 SHA, latest) → SSM 배포

## 필요 시크릿
- `AWS_ACCESS_KEY_ID`: 배포용 IAM 사용자의 액세스 키 ID
- `AWS_SECRET_ACCESS_KEY`: 배포용 IAM 사용자의 시크릿 액세스 키
- `AWS_REGION`: 리소스가 있는 AWS 리전
- `EC2_INSTANCE_ID`: 배포 대상 EC2 인스턴스 ID
- `ECR_REPOSITORY_FASTAPI`: FastAPI 이미지용 ECR 리포지토리 이름
- `ECR_REPOSITORY`: Nginx 이미지용 ECR 리포지토리 이름\n