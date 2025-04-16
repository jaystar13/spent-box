# 명명규칙

# 🧾 DB 모델링 명명 규칙 (SpentBox 기준)

---

## 📁 테이블 / 엔티티 명

| 항목 | 규칙 | 예시 |
| --- | --- | --- |
| 복수형 | 복수형 사용 권장 | `users`, `expenses`, `categories` |
| 소문자 | 모두 소문자 | `user_expenses` |
| snake_case | 언더스코어로 구분 | `upload_files` |

---

## 🧱 컬럼 / 필드 명

| 항목 | 규칙 | 예시 |
| --- | --- | --- |
| snake_case | 언더스코어로 구분 | `created_at`, `user_id`, `amount` |
| 명확한 의미 | 축약어 지양 | `amt` ❌ → `amount` ✅ |
| 날짜/시간 | 접미사로 `_at`, `_date` 사용 | `created_at`, `payment_date` |

---

## 🔗 외래키(Foreign Key)

| 항목 | 규칙 | 예시 |
| --- | --- | --- |
| 참조 테이블명 + `_id` | 참조가 명확하게 | `user_id`, `category_id` |
| 인덱스 | FK는 인덱스 생성 추천 | `user_id (INDEX)` |

---

## 🗂 Python 파일 및 클래스

| 항목 | 규칙 | 예시 |
| --- | --- | --- |
| 모델 클래스명 | PascalCase, 단수형 | `User`, `Expense`, `Category` |
| 파일명 | snake_case | `user.py`, `expense.py` |
| Pydantic 모델명 | 동작 기준 접미사 | `UserCreate`, `ExpenseOut` |

---

## 🔁 API 경로(URL)

| 항목 | 규칙 | 예시 |
| --- | --- | --- |
| 소문자, 복수형 | RESTful한 리소스 구조 | `/users`, `/expenses` |
| 리소스 중심 | 동사 대신 명사 | `/getUser` ❌ → `/users/{id}` ✅ |

---

## ✅ SpentBox 적용 예시

```
테이블: users, expenses, categories, upload_files

컬럼: id, email, password_hash, created_at, amount, description, category_id, user_id

클래스: User, Expense, Category, UploadFile

API: /users, /expenses, /categories, /upload
```

# 🔤 SpentBox 프로젝트 권장 축약어 목록

명확성과 일관성을 위해 자주 사용하는 단어들에 대해 아래와 같은 축약어를 사용합니다.

DB 컬럼명, API 필드명, 변수명 등에 동일하게 적용하세요.

---

## ✅ 일반 필드용 축약어

| 원어 | 축약어 | 예시 |
| --- | --- | --- |
| amount | amt | total_amt, monthly_amt |
| quantity | qty | order_qty |
| date | dt | created_dt, purchase_dt |
| name | nm | user_nm, bank_nm |
| code | cd | status_cd, category_cd |
| count | cnt | item_cnt, retry_cnt |
| number | no | order_no, phone_no |
| description | desc | item_desc |
| identifier | id | user_id, category_id |
| type | tp | category_tp, file_tp |
| status | sts | login_sts, account_sts |
| result | rslt | upload_rslt |
| flag (Y/N) | yn | active_yn, deleted_yn |

---

## ⚠️ 사용 주의

- `amt`, `qty` 등은 너무 줄이지 않고 **의미가 명확히 전달되는 선에서만 사용**
- 위 목록에 없는 단어는 최대한 풀어쓰되, **공통 패턴 생기면 추후 추가 가능**
- 혼합 사용은 지양: `user_name` ✅ / `usr_nm` ❌

---

## 📝 예시 컬럼명 적용

| 원래 이름 | 권장 이름 |
| --- | --- |
| total amount | `total_amt` |
| transaction date | `txn_dt` |
| user name | `user_nm` |
| deleted flag | `deleted_yn` |
| category code | `category_cd` |
| retry count | `retry_cnt` |

---

> 이 목록은 계속 확장 가능합니다. 프로젝트에서 반복 사용되는 단어는 모두 여기에 추가하세요.
>