
# Documentation

## Purpose of Document

This document serves as the primary documentation for the CI/CD pipelines associated with the DevOps project. It provides detailed explanations of each step and technology used to ensure code quality, security, and seamless deployment.

## Format of Document

The format of this documentation mirrors the following structure for clarity:

```yaml
Pipeline:
  Job:
    - Step:
      - Requirements: (e.g., prerequisites like secrets, tools, or configurations)
      - Summary: (e.g., a brief description of the step)
```

## Pipelines Overview

### 1. Main Branch CI/CD Pipeline
#### Description
This pipeline runs on pull requests to the `main` branch and workflow dispatch triggers. It ensures code quality, performs security scans, builds Docker images, and deploys the application.

### 2. Feature Branch Pipeline
#### Description
This pipeline triggers on pushes to `feature/*` branches and workflow dispatch. It focuses on linting, testing, and validating new features under development.

---

## Jobs and Steps

### Main Branch CI/CD Pipeline

#### 1. Lint
##### Description
Ensures code adheres to defined coding standards.
##### Steps:
- **Step 1: Checkout Code**
  - **Requirements**: None
  - **Summary**: Retrieves the latest code from the repository.
- **Step 2: Setup Python**
  - **Requirements**: None
  - **Summary**: Configures the Python environment (version 3.10.16).
- **Step 3: Install Flake8**
  - **Requirements**: None
  - **Summary**: Installs the `flake8` package for linting.
- **Step 4: Run Flake8**
  - **Requirements**: Flake8 installed
  - **Summary**: Executes linting on the `app` directory.

#### 2. Unit and Integration Tests
##### Description
Executes unit and integration tests to validate application logic.
##### Steps:
- **Step 1: Checkout Code**
  - **Requirements**: None
  - **Summary**: Retrieves the latest code from the repository.
- **Step 2: Setup Python**
  - **Requirements**: None
  - **Summary**: Configures the Python environment.
- **Step 3: Install Dependencies**
  - **Requirements**: `requirements.txt`
  - **Summary**: Installs necessary dependencies for testing.
- **Step 4: Run Tests**
  - **Requirements**: Dependencies installed
  - **Summary**: Executes all tests using Pytest.
- **Step 5: Generate Coverage Report**
  - **Requirements**: Coverage package installed
  - **Summary**: Generates a test coverage report.

#### 3. SonarQube Analysis
##### Description
Analyzes code quality and detects vulnerabilities using SonarQube.
##### Steps:
- **Step 1: Checkout Code**
  - **Requirements**: None
  - **Summary**: Retrieves the codebase.
- **Step 2: SonarQube Scan**
  - **Requirements**: `SONAR_TOKEN` secret
  - **Summary**: Executes code quality analysis.

#### 4. Docker Build
##### Description
Builds and pushes Docker images.
##### Steps:
- **Step 1: Checkout Code**
  - **Requirements**: None
  - **Summary**: Retrieves the latest code.
- **Step 2: Authenticate Docker Registry**
  - **Requirements**: Secrets for `GITHUB_TOKEN`
  - **Summary**: Logs into the Docker registry.
- **Step 3: Build and Push Docker Image**
  - **Requirements**: Docker installed
  - **Summary**: Builds and pushes Docker images tagged with the commit SHA.

#### 5. Security Scanning (Docker Image)
##### Description
Scans Docker images for vulnerabilities using Snyk.
##### Steps:
- **Step 1: Authenticate Snyk**
  - **Requirements**: `SNYK_TOKEN` secret
  - **Summary**: Authenticates Snyk tool.
- **Step 2: Perform Security Scan**
  - **Requirements**: Docker image built
  - **Summary**: Scans the Docker image for vulnerabilities.

#### 6. EKS Deployment
##### Description
Deploys the application to Amazon Elastic Kubernetes Service (EKS).
##### Steps:
- **Step 1: Configure AWS CLI**
  - **Requirements**: AWS credentials
  - **Summary**: Configures AWS CLI with necessary credentials.
- **Step 2: Install kubectl**
  - **Requirements**: None
  - **Summary**: Installs Kubernetes CLI for deployment.
- **Step 3: Apply Kubernetes Manifests**
  - **Requirements**: Kubernetes manifests
  - **Summary**: Deploys the application and service to EKS.

#### 7. Monitoring Setup
##### Description
Installs Prometheus and Grafana for application monitoring.
##### Steps:
- **Step 1: Apply Monitoring Manifests**
  - **Requirements**: Kubernetes environment
  - **Summary**: Deploys monitoring tools to the cluster.
- **Step 2: Verify Monitoring**
  - **Requirements**: Monitoring tools deployed
  - **Summary**: Ensures all monitoring pods are running.

---

### Feature Branch Pipeline

#### 1. Lint
##### Description
Validates code quality using Flake8.
##### Steps:
- **Step 1: Checkout Code**
  - **Requirements**: None
  - **Summary**: Pulls the feature branch.
- **Step 2: Setup Python**
  - **Requirements**: None
  - **Summary**: Configures Python environment.
- **Step 3: Install Flake8**
  - **Requirements**: None
  - **Summary**: Installs the `flake8` package.
- **Step 4: Run Flake8**
  - **Requirements**: Flake8 installed
  - **Summary**: Lints the feature branch code.

#### 2. Unit Tests
##### Description
Runs unit tests for the feature branch.
##### Steps:
- **Step 1: Checkout Code**
  - **Requirements**: None
  - **Summary**: Pulls the feature branch.
- **Step 2: Setup Python**
  - **Requirements**: None
  - **Summary**: Configures Python environment.
- **Step 3: Install Dependencies**
  - **Requirements**: `requirements.txt`
  - **Summary**: Installs dependencies.
- **Step 4: Run Unit Tests**
  - **Requirements**: Dependencies installed
  - **Summary**: Executes unit tests.

---

## Technologies Used

1. **AWS RDS**: For relational database storage.
2. **AWS S3**: For object storage.
3. **AWS IAM**: For secure access management.
4. **AWS EKS**: For deploying Kubernetes clusters.
5. **Flake8**: For Python linting.
6. **SonarQube**: For code quality analysis.
7. **Snyk**: For security vulnerability scans.
8. **Prometheus**: For monitoring metrics.
9. **Grafana**: For visualizing monitoring data.
10. **Pytest**: For unit and integration testing.

---

## Clean Up

### To clean up Kubernetes resources:
```bash
kubectl delete service devops-project-service
kubectl delete deployment devops-project-deployment
```

### To stop the Minikube cluster:
```bash
minikube stop
```

### Optionally, delete the Minikube environment:
```bash
minikube delete
```
