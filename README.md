* การใช้งานโปรเจ็กต์
* วิธีติดตั้ง
* โครงสร้างไฟล์
* โครงสร้างฐานข้อมูล + คำอธิบายทุกตารางทุกฟิลด์
* ภาพรวม API
* ภาพรวมการทำงานของระบบ
* เหมือน “คู่มือโปรเจ็กต์” แบบครบจบในไฟล์เดียว

ผมจัดให้ใหม่ทั้งหมดแบบ FULL VERSION
**นี่คือ README.md ที่ “ครบทุกอย่าง” ตามที่คุณต้องการ**

---

# ✅ README.md (Full Project Documentation)

คุณสามารถก็อปทั้งไฟล์นี้ไปวางในโปรเจ็กต์ได้ทันที

---

````markdown
# EV Service Center Management API
ระบบ Backend สำหรับบริหารจัดการศูนย์บริการรถยนต์ไฟฟ้า (EV Service Center)  
พัฒนาด้วย **FastAPI + SQLAlchemy** ในรูปแบบ Modular เพื่อให้ขยายระบบได้ง่าย เช่นเพิ่มโมดูล Parts, Billing, Notification, Technician Workflow ฯลฯ  

ระบบนี้ถูกออกแบบให้รองรับการทำงานระดับศูนย์บริการจริง เช่น:
- จัดการผู้ใช้งานตามบทบาท
- จัดการลูกค้า + รถยนต์
- การจองคิวเข้าศูนย์ (Appointment)
- การเปิดใบสั่งซ่อม (Work Order)
- รองรับหลายสาขา (Multi-Branch)
- ใช้ JWT Authentication
- รองรับต่อยอดเชื่อม ERP/CRM ได้

---

# 1. Installation Guide

## 1.1 Install Dependencies

```bash
pip install -r requirements.txt
````

## 1.2 Run Server

```bash
uvicorn app.main:app --reload
or
python -m uvicorn app.main:app --reload
```

## 1.3 Access API Documentation

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

# 2. Project Structure

```
ev_service_backend/
│
├── requirements.txt
├── README.md
│
└── app/
    ├── main.py
    │
    ├── core/
    │   ├── config.py      # ENV, SECRET_KEY, Database URL
    │   ├── database.py    # SQLAlchemy engine + Base
    │   └── security.py    # JWT, bcrypt hash
    │
    ├── dependencies.py    # get_db() dependency
    │
    ├── models/
    │   ├── user.py
    │   ├── branch.py
    │   ├── customer.py
    │   ├── vehicle.py
    │   ├── appointment.py
    │   └── work_order.py
    │
    ├── schemas/
    │   ├── user.py
    │   ├── branch.py
    │   ├── customer.py
    │   ├── vehicle.py
    │   ├── appointment.py
    │   └── work_order.py
    │
    └── routers/
        ├── auth.py
        ├── branches.py
        ├── customers.py
        ├── vehicles.py
        ├── appointments.py
        └── work_orders.py
```

---

# 3. Core Features

## ✔ Authentication (JWT)

* Register user
* Login → Return access token
* Protect all sensitive routes

## ✔ Branch Management

* Create / Update / List branch
* Multi-branch support

## ✔ Customer Management

* จัดเก็บข้อมูลลูกค้า
* ค้นหาเบื้องต้น (phone, name)

## ✔ Vehicle Management

* รถยนต์ 1 ลูกค้า สามารถมีหลายคันได้
* รองรับ EV metadata เช่น battery kWh, EV Type

## ✔ Appointment System

* จองคิวเข้าศูนย์
* บันทึก schedule service

## ✔ Work Order

* เปิดใบงานซ่อม
* เชื่อมต่อกับลูกค้า & รถ & สาขา
* รองรับ status flow เช่น DRAFT → IN_PROGRESS → DONE

---

# 4. Database Design (FULL DETAIL)

ด้านล่างคือรายละเอียดโครงสร้างฐานข้อมูลทั้งหมด พร้อมคำอธิบายฟิลด์แบบเต็ม

---

# 4.1 Table: `branches`

เก็บข้อมูลศูนย์บริการแต่ละสาขา

| Field     | Type       | Description        |
| --------- | ---------- | ------------------ |
| id        | Integer PK | รหัสสาขา           |
| code      | String     | รหัสย่อ เช่น BR001 |
| name      | String     | ชื่อสาขา           |
| address   | String     | ที่อยู่            |
| city      | String     | อำเภอ              |
| province  | String     | จังหวัด            |
| country   | String     | ประเทศ             |
| phone     | String     | เบอร์โทรศูนย์      |
| is_active | Boolean    | เปิด/ปิดการใช้งาน  |

**ใช้ทำอะไร?**
→ ระบบหลายสาขาจะใช้ branch_id เชื่อม เช่น customer, vehicle, work order

---

# 4.2 Table: `users`

ใช้จัดเก็บข้อมูลผู้ใช้ระบบ และการกำหนดสิทธิ์ตาม role

| Field         | Type          | Description                  |
| ------------- | ------------- | ---------------------------- |
| id            | Integer PK    | รหัสผู้ใช้                   |
| username      | String        | ชื่อเข้าใช้งาน               |
| password_hash | String        | bcrypt hash ของรหัสผ่าน      |
| full_name     | String        | ชื่อ-นามสกุล                 |
| email         | String        | อีเมล                        |
| phone         | String        | เบอร์โทร                     |
| role          | String        | เช่น ADMIN / SA / TECHNICIAN |
| branch_id     | FK → branches | สาขาที่พนักงานประจำ          |
| is_active     | Boolean       | เปิดใช้งานบัญชี              |
| created_at    | DateTime      | วันที่สร้าง                  |
| updated_at    | DateTime      | วันที่แก้ไขล่าสุด            |

**ใช้ทำอะไร?**
→ Authentication, Authorization, Logging

---

# 4.3 Table: `customers`

ข้อมูลลูกค้าเจ้าของรถ

| Field                     | Type      | Description          |
| ------------------------- | --------- | -------------------- |
| id                        | PK        |                      |
| full_name                 | String    | ชื่อจริง             |
| phone                     | String    | ใช้ค้นหาได้เร็ว      |
| email                     | String    |                      |
| line_id                   | String    | ผูก LINE OA ได้      |
| preferred_contact_channel | String    | PHONE / LINE / EMAIL |
| preferred_branch_id       | FK        | สาขาที่ชอบไป         |
| created_at                | timestamp |                      |
| updated_at                | timestamp |                      |

**ใช้ทำอะไร?**
→ ใช้เชื่อมโยงกับ vehicles / appointments / work_orders

---

# 4.4 Table: `vehicles`

รถแต่ละคันที่เข้าศูนย์

| Field                | Type    | Description        |
| -------------------- | ------- | ------------------ |
| id                   | PK      |                    |
| vin                  | String  | เลขตัวถัง (unique) |
| plate_no             | String  | ทะเบียนรถ          |
| brand                | String  | ยี่ห้อ             |
| model                | String  | รุ่น               |
| model_year           | Integer | ปีรุ่น             |
| ev_type              | String  | BEV / PHEV / HEV   |
| battery_capacity_kwh | Integer | ขนาดแบตเตอรี่      |
| customer_id          | FK      | เจ้าของรถ          |
| created_at           | ts      |                    |
| updated_at           | ts      |                    |

**ใช้ทำอะไร?**
→ ใช้ผูกใบสั่งซ่อม, นัดหมาย

---

# 4.5 Table: `appointments`

นัดหมายเข้าศูนย์บริการ

| Field                | Type     | Description                       |
| -------------------- | -------- | --------------------------------- |
| id                   | PK       |                                   |
| branch_id            | FK       | สาขาที่จอง                        |
| customer_id          | FK       |                                   |
| vehicle_id           | FK       |                                   |
| appointment_datetime | DateTime | วันเวลานัด                        |
| status               | String   | REQUESTED / CONFIRMED / CANCELLED |
| service_type         | String   | Maintenance / Repair / Battery    |
| notes                | String   | หมายเหตุ                          |
| created_by           | FK User  | พนักงานที่สร้าง                   |
| created_at           | ts       |                                   |
| updated_at           | ts       |                                   |

**ใช้ทำอะไร?**
→ ใช้เป็นจุดเริ่มต้นของการสร้าง Work Order

---

# 4.6 Table: `work_orders`

ใบสั่งซ่อม (Work Order) ในศูนย์บริการ

| Field                      | Type    | Description                     |
| -------------------------- | ------- | ------------------------------- |
| id                         | PK      |                                 |
| branch_id                  | FK      |                                 |
| customer_id                | FK      |                                 |
| vehicle_id                 | FK      |                                 |
| service_advisor_id         | FK User | SA ผู้รับผิดชอบ                 |
| status                     | String  | DRAFT / IN_PROGRESS / COMPLETED |
| promised_delivery_datetime | ts      | นัดหมายส่งมอบ                   |
| actual_delivery_datetime   | ts      | วันที่เสร็จจริง                 |
| created_at                 | ts      |                                 |
| updated_at                 | ts      |                                 |

**ใช้ทำอะไร?**
→ เป็นแกนหลักของงานซ่อม
→ ในระบบจริงอาจต่อยอดเพิ่ม work_order_jobs, work_order_parts

---

# 5. API Overview

## 5.1 `/auth`

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| POST   | `/auth/register` | สมัครผู้ใช้         |
| POST   | `/auth/token`    | Login ได้ JWT Token |

---

## 5.2 `/branches`

| Method | Endpoint         | Description |
| ------ | ---------------- | ----------- |
| GET    | `/branches`      | List สาขา   |
| POST   | `/branches`      | เพิ่มสาขา   |
| PUT    | `/branches/{id}` | แก้ไข       |
| GET    | `/branches/{id}` | ดูข้อมูล    |

---

## 5.3 `/customers`

| Method                | Endpoint |
| --------------------- | -------- |
| GET `/customers`      |          |
| POST `/customers`     |          |
| PUT `/customers/{id}` |          |
| GET `/customers/{id}` |          |

---

## 5.4 `/vehicles`

| Method               | Endpoint |
| -------------------- | -------- |
| GET `/vehicles`      |          |
| POST `/vehicles`     |          |
| PUT `/vehicles/{id}` |          |
| GET `/vehicles/{id}` |          |

---

## 5.5 `/appointments`

| Method                   | Endpoint |
| ------------------------ | -------- |
| GET `/appointments`      |          |
| POST `/appointments`     |          |
| PUT `/appointments/{id}` |          |
| GET `/appointments/{id}` |          |

---

## 5.6 `/work-orders`

| Method                  | Endpoint |
| ----------------------- | -------- |
| GET `/work-orders`      |          |
| POST `/work-orders`     |          |
| PUT `/work-orders/{id}` |          |
| GET `/work-orders/{id}` |          |

---

# 6. System Workflow Overview

## A. Customer Flow

1. ลูกค้าโทรหรือจองเข้าศูนย์
2. SA บันทึก Appointment
3. ลูกค้านำรถเข้าศูนย์ (Check-in → ยังไม่ทำใน version นี้)
4. SA เปิด Work Order
5. ช่างดำเนินงาน (เวอร์ชันต่อไปเพิ่ม module Technician)
6. ออกบิล / จ่ายเงิน (จะเพิ่ม Billing module ภายหลัง)

---

# 7. Next Step / Suggested Extensions

คุณสามารถต่อยอดระบบนี้ได้ทันทีโดยเพิ่ม:

### ✔ Parts / Inventory

* ตารางอะไหล่
* คลังอะไหล่แต่ละสาขา
* การตัดสต็อก

### ✔ Billing / Payment

* invoices
* invoice_items
* payments

### ✔ Technician Module

* job list ตามช่างแต่ละคน
* time tracking

### ✔ Notification System

* LINE Messaging API
* Email / SMS

### ✔ Reporting Dashboard

* งานรออะไหล่
* WO ต่อวัน / ต่อสาขา
* SLA

---

# 8. Summary

โปรเจ็กต์นี้เป็นโครงสร้าง backend ที่ออกแบบให้ใช้งานได้จริง รองรับการขยายต่อเป็นระบบศูนย์บริการ EV เต็มรูปแบบ
คุณสามารถนำไปต่อยอดได้ทั้งด้านฟีเจอร์, Performance, และ Integration กับ ERP เช่น Microsoft D365, SAP, หรือระบบ Payment Gateway ได้ทันที


