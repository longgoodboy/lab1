
## Phan 2 - Bai Tap Mo Rong (1:00-1:30)

### Bai tap 2.1 - Do Nhay Cua Temperature

Goi `call_openai` voi cac gia tri temperature 0.0, 0.5, 1.0 va 1.5 su dung prompt **"Hay ke cho toi mot su that thu vi ve Viet Nam."**

**Ban nhan thay quy luat gi qua bon phan hoi?** (2-3 cau)
> Khi temperature thap nhu 0.0, cau tra loi thuong on dinh, ngan gon va it thay doi giua cac lan goi. Khi temperature tang len 1.0 hoac 1.5, cau tra loi da dang va sang tao hon, nhung cung de kem nhat quan hoac them chi tiet khong can thiet.
> Neu chay lai nhieu lan voi cung prompt, temperature cao thuong tao ra cach dien dat moi me hon, trong khi temperature thap phu hop hon khi can cau tra loi co the du doan.

**Ban se dat temperature bao nhieu cho chatbot ho tro khach hang, va tai sao?**
> Toi se dat temperature khoang 0.2 den 0.5 cho chatbot ho tro khach hang. Muc nay giup cau tra loi tu nhien nhung van on dinh, de kiem soat va phu hop voi thong tin chinh xac.

---

### Bai tap 2.2 - Danh Doi Chi Phi

Xem xet kich ban: 10.000 nguoi dung hoat dong moi ngay, moi nguoi thuc hien 3 lan goi API, moi lan trung binh ~350 token.

**Uoc tinh xem GPT-4o dat hon GPT-4o-mini bao nhieu lan cho workload nay:**
> GPT-4o co gia output $0.010 moi 1K token, GPT-4o-mini la $0.0006 moi 1K token, nen GPT-4o dat hon khoang 16.67 lan. Workload moi ngay la 10,000 * 3 * 350 = 10,500,000 token; chi phi output uoc tinh la khoang $105/ngay voi GPT-4o va $6.30/ngay voi GPT-4o-mini.

**Mo ta mot truong hop ma chi phi cao hon cua GPT-4o la xung dang, va mot truong hop GPT-4o-mini la lua chon tot hon:**
> GPT-4o xung dang khi tac vu can chat luong lap luan cao, vi du phan tich ho so phuc tap, viet noi dung quan trong, hoac xu ly yeu cau co rui ro cao. GPT-4o-mini phu hop hon cho chatbot FAQ, tom tat ngan, phan loai noi dung, hoac cac tinh nang co luu luong lon can toi uu chi phi.

---

### Bai tap 2.3 - Trai Nghiem Nguoi Dung voi Streaming

**Streaming quan trong nhat trong truong hop nao, va khi nao thi non-streaming lai phu hop hon?** (1 doan van)
> Streaming quan trong nhat khi cau tra loi dai hoac nguoi dung can thay tien trinh ngay, vi du chatbot, tro ly lap trinh, giai thich bai hoc, hoac tao noi dung dai. No lam ung dung co cam giac nhanh hon vi nguoi dung doc duoc ket qua trong khi model van dang sinh tiep. Non-streaming phu hop hon voi cau tra loi ngan, tac vu batch, API noi bo, hoac khi can kiem tra toan bo ket qua truoc khi hien thi cho nguoi dung, nhu tra ve JSON hop le hoac loc noi dung nhay cam.

