# Virtual Serial Communication

실제 하드웨어 없이 Serial 통신 흐름을 테스트하기 위해 Virtual Serial Port Driver(VSPD)와 Python `pyserial`을 사용한 실습입니다.

## Environment

- Python
- `pyserial`
- Virtual Serial Port Driver (VSPD)
- Virtual COM Port Pair: `COM7 ↔ COM8`
- Baud Rate: `115200`

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

## Run

두 개의 터미널에서 각각 실행합니다.

```bash
python sender.py
```

```bash
python receiver.py
```

`receiver.py`에서 다음과 같이 수신되면 정상 동작입니다.

```text
RX: 25.3,61.2
```
