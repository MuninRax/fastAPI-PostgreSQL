# fastAPI-PostgreSQL

### Run
- Run ใน folder app ``` uvicorn main:app --reload ```

- ทันทีที่ Run จะมีการสร้าง Table ขึ้นมาชื่อว่า users
    - column id เป็น Primary Key เป็น (Generate ให้อัตโนมัติ)
    - column name เป็น String (ใส่เอง)
    - column height เป็นเลขทศนิยม 2 ตำแหน่ง (ใส่เอง)
    - column date เป็นวันที่ที่เอาข้อมูลเข้า (Generate ให้อัตโนมัติ)
    - column time เป็นเวลาที่เอาข้อมูลเข้า (Generate ให้อัตโนมัติ)
    - column vector เป็นข้อมูล vector (Generate ให้อัตโนมัติ 3 ตัว)

- URL นี้จะไปหน้าแรก ``` http://127.0.0.1:8000 ```
- URL นี้จะไปหน้าที่มี CRUD ``` http://127.0.0.1:8000/docs ```