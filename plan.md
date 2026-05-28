# Plan - Lab 1 LLM API Foundation

## Goal

Hoan thanh lab nhanh, re, khong ton tien API khi chay test, va toi da diem o muc "Cham diem".

## Strategy

- Dung `solution/solution.py` lam file nop bai chinh vi test uu tien doc file nay.
- Giu code tuong thich OpenAI SDK de pass mock tests.
- Ho tro OpenRouter gia re khi chay thu cong bang `OPENAI_BASE_URL`, nhung khong bat buoc chay API that.
- Khong dua API key vao source code; chi doc qua bien moi truong.
- Hoan thanh ca cac ham bonus vi test co kiem tra:
  - `retry_with_backoff`
  - `batch_compare`
  - `format_comparison_table`

## Implementation Plan

1. Tao folder `solution/`.
2. Tao `solution/solution.py` tu template va implement cac ham:
   - `call_openai`
   - `call_openai_mini`
   - `compare_models`
   - `streaming_chatbot`
   - `retry_with_backoff`
   - `batch_compare`
   - `format_comparison_table`
3. Tao `solution/exercises.md` va dien cau tra loi cho:
   - Bai 2.1: temperature
   - Bai 2.2: cost tradeoff
   - Bai 2.3: streaming UX
4. Chay `pytest tests/ -v` de xac nhan tat ca test pass.
5. Neu muon demo API that bang OpenRouter:
   - Set `OPENAI_API_KEY`.
   - Set `OPENAI_BASE_URL=https://openrouter.ai/api/v1`.
   - Uu tien model re/free khi goi thu cong de tranh ton tien.

## Cost Plan

- Pytest dung mock nen khong ton tien API.
- Khong can API key de pass test.
- Neu demo thu cong, dung OpenRouter va model re/free.
- Khong hardcode key trong repo de tranh lo key va bi tru diem bao mat.

## Grading Focus

- 50 diem: tat ca pytest tests pass.
- 10 diem: `compare_models` tra ve dung dict.
- 10 diem: `streaming_chatbot` duy tri lich su hoi thoai.
- 30 diem: dien day du 3 cau hoi trong `exercises.md`.

## Acceptance Criteria

- `pytest tests/ -v` pass het.
- `solution/solution.py` co day du cac ham can thiet.
- `solution/exercises.md` da dien day du cau tra loi.
- Khong co API key that trong source code.
