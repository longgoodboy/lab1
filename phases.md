# Phases - Lab 1 Progress

## Current Status

- [x] Doc `README.md`.
- [x] Doc `exercises.md`.
- [x] Doc `tests/test_solution.py`.
- [x] Xac dinh test co kiem tra them cac ham bonus.
- [x] Tao folder `solution/`.
- [x] Tao `solution/solution.py`.
- [x] Implement `call_openai`.
- [x] Implement `call_openai_mini`.
- [x] Implement `compare_models`.
- [x] Implement `streaming_chatbot`.
- [x] Implement `retry_with_backoff`.
- [x] Implement `batch_compare`.
- [x] Implement `format_comparison_table`.
- [x] Tao `solution/exercises.md`.
- [x] Dien cau tra loi bai tap 2.1, 2.2, 2.3.
- [ ] Chay xong `pytest tests/ -v`.
- [ ] Xu ly loi test neu co.
- [ ] Kiem tra lan cuoi truoc khi nop.

## API Key Check

- `OPENAI_API_KEY`: chua duoc set trong terminal hien tai.
- `OPENAI_BASE_URL`: chua duoc set trong terminal hien tai.
- Tim trong repo chi thay:
  - Placeholder trong `README.md`.
  - Code doc bien moi truong trong `solution/solution.py`.
  - Khong thay API key that trong file source.

## Notes

- Lan chay `pytest tests/ -v` truoc do bi user interrupt, nen chua co ket qua test cuoi cung.
- Lenh `git status --short` bi chan do Git bao "dubious ownership"; viec nay khong anh huong truc tiep den code lab, nhung neu can dung Git thi can them safe.directory.

## Next Phase

1. Chay lai:

```bash
pytest tests/ -v
```

2. Neu test fail, sua dung theo contract trong `tests/test_solution.py`.
3. Neu test pass, co the zip folder `solution/` de nop bai.
