# Virtual Serial Communication

실제 하드웨어 없이 Serial 통신 흐름을 테스트하기 위해 Virtual Serial Port Driver(VSPD)와 Python `pyserial`을 사용한 실습입니다.

## Environment

- Windows
- Ubuntu / WSL
- Python
- `pyserial`
- Virtual Serial Port Driver (VSPD)
- Virtual COM Port Pair: `COM7 ↔ COM8`
- Baud Rate: `115200`

> VSPD의 가상 COM Port(`COM7 ↔ COM8`) 송수신 테스트는 Windows 환경에서 수행했습니다. Ubuntu/WSL은 프로젝트 작업 과정에서 Linux 터미널과 기본 명령어를 익히는 용도로 함께 사용했습니다.

## Files

### `sender.py`
가상의 센서/장비 역할을 합니다.

- `COM7`을 통해 샘플 데이터 `25.3,61.2` 전송
- 5초 간격으로 반복 송신

### `receiver.py`
수집기 역할을 합니다.

- `COM8`에서 Serial 데이터 수신
- 수신한 byte 데이터를 문자열로 변환하여 출력

## Communication Flow

```text
sender.py
   ↓
 COM7
   ↓
Virtual Serial Port Driver
   ↓
 COM8
   ↓
receiver.py
```

## Ubuntu / WSL Practice

프로젝트 작업 과정에서 Ubuntu/WSL 터미널을 사용하며 Linux 기본 명령어도 함께 실습했습니다.

### 현재 위치 확인

```bash
pwd
```

### 파일과 디렉터리 확인

```bash
ls
ls -al
```

### 디렉터리 이동

```bash
cd <directory>
cd ..
```

### 디렉터리 생성

```bash
mkdir <directory>
```

### 파일 생성 및 확인

```bash
touch <file>
cat <file>
```

### Python 버전 확인 및 실행

```bash
python3 --version
python3 sender.py
python3 receiver.py
```

### Python 패키지 설치 예시

```bash
pip install pyserial
```

`uv` 환경을 사용할 경우에는 다음과 같이 실행할 수 있습니다.

```bash
uv add pyserial
uv run python sender.py
uv run python receiver.py
```

## What I Practiced

VSPD를 이용해 `COM7 ↔ COM8` 가상 포트 pair를 구성하고, 실제 Arduino나 센서가 연결되지 않은 환경에서도 Python 프로그램 간 Serial 송수신을 테스트했습니다.

이를 통해 실제 장비 연동 전에 다음 흐름을 시뮬레이션할 수 있음을 확인했습니다.

```text
가상 데이터 생성
      ↓
Serial 전송
      ↓
Virtual COM Port
      ↓
Python 수신
```

또한 Windows와 Ubuntu/WSL 환경을 함께 사용하면서 Windows의 가상 COM Port 기반 Serial 통신과 Linux 터미널 기본 명령어 사용을 각각 경험했습니다.

## Run

VSPD에서 `COM7 ↔ COM8` pair를 생성한 뒤, Windows의 두 개 터미널에서 각각 실행합니다.

```bash
python sender.py
```

```bash
python receiver.py
```

또는 `uv` 환경에서는 다음과 같이 실행합니다.

```bash
uv run python sender.py
uv run python receiver.py
```

`receiver.py`에서 다음과 같이 수신되면 정상 동작입니다.

```text
RX: 25.3,61.2
```
