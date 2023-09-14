# Treehouse

## Question

คุณออกเดินทางไปกับเหล่าเอลฟ์ ระหว่างทางคุณพบกับป่ารูปร่างประหลาดที่มีต้นไม้ที่ถูกปลูกเป็นตารางอย่างมีระเบียบ เหล่าเอลฟ์อธิบายว่านักเดินทางกลุ่มก่อนหน้าเป็นผู้ปลูกต้นไม้เหล่านี้เพื่อฟื้นฟูป่า และตอนนี้เหล่าเอลฟ์ต้องการการสร้างบ้านต้นไม้ในป่านี้

บ้านบนต้นไม้ต้นหนึ่งจะไม่ถูกมองเห็นก็ต่อเมื่อมีต้นไม้ต้นอื่นมาช่วยกำบัง การตรวจสอบว่าบ้านต้นไม้ถูกกำบังหรือไม่ ต้องตรวจสอบจากการมองเข้ามาจากภายนอกของของป่าทั้งตามแนวตั้งและแนวนอน

เหล่าเอลฟ์ได้ส่งโดรนขึ้นไปถ่ายภาพจากด้านบนและทำแผนที่เพื่อระบุความสูงของต้นไม้แต่ละต้น (input) ได้ผลลัพธ์ดังตัวอย่าง:

```
30373
25512
65332
33549
35390
```

ต้นไม้แต่ละต้นจะมีตัวเลขกำกับความสูง (เลขตัวเดียว) โดย 0 คือต้นไม้ที่เตี้ยที่สุด และ 9 คือต้นไม้ที่สูงที่สุด

ต้นไม้ต้นหนึ่งจะถูกมองเห็นได้จากภายนอกถ้าต้นไม้ระหว่างมันจนถึงต้นที่อยู่ชิดขอบมีความสูงน้อยกว่ามัน โดยมองทิศบน ล่าง ซ้าย และ ขวา เท่านั้น ไม่มีทแยงมุม

จากข้อมูลความสูงของต้นไม้ด้านบน ใส่ตัวอักษรกำกับเพื่อให้อ่านง่ายขึ้น:
```
3     0     3     7     3
2     5 A   5 B   1 C   2
6     5 D   3 E   3 F   2
3     3 G   5 H   4 I   9
3     5     3     9     0
```

ต้นไม้ที่อยู่ชิดขอบป่าจะถูกมองเห็นทั้งหมด (ไม่มีตัวอักษรกำกับ) เนื่องจากไม่มีต้นไหนกำบังมันได้ ทำให้เหลือต้นไม้เพียง 9 ต้นที่ต้องพิจารณา:
  - ต้นไม้ความสูง 5 (A) จะถูกมองเห็นจากด้านซ้ายและด้านบน (ด้านขวาและด้านล่างจะมองไม่เห็น เนื่องจากมีต้นไม้ความสูง 5 ช่วยบังไว้)
  - ต้นไม้ความสูง 5 (B) จะถูกมองเห็นได้จากด้านบนและด้านขวา
  - ต้นไม้ความสูง 1 (C) ไม่ถูกมองเห็นจากทางใดเลย (ต้นไม้ต้นนี้จะถูกมองเห็นได้ก็ต่อเมื่อต้นไม้ทุกต้นระหว่างมันไปจนถึงขอบ มีความสูงเป็น 0 ทั้งหมด)
  - ต้นไม้ความสูง 5 (D) ถูกมองเห็นได้จากทางด้านขวา
  - ต้นไม้ความสูง 3 (E) ไม่ถูกมองเห็นจากทางใดเลย (ต้นไม้ต้นนี้จะถูกมองเห็นได้ก็ต่อเมื่อต้นไม้ทุกต้นระหว่างมันไปจนถึงขอบ มีความสูงไม่เกิน 2 ทั้งหมด)
  - ต้นไม้ความสูง 3 (F) ถูกมองเห็นได้จากทางด้านขวา
  - แถวล่างสุด (G, H, I) ต้นไม้ความสูง 5 ถูกมองเห็นได้ แต่ต้นไม้ความสูง 3 และ 4 จะไม่ถูกมองเห็น


*จากต้นไม้ที่อยู่ชิดขอบป่าทั้ง 16 ต้นที่จะถูกมองเห็น รวมกับอีก 5 ต้นด้านในที่ถูกมองเห็นเช่นกัน ทำให้ได้จำนวนต้นไม้ที่จะถูกมองเห็นรวมทั้งหมด 21 ต้น*


คุณต้องการช่วยเหล่าเอลฟ์จึงรับอาสาเขียนโปรแกรม โดยมีข้อกำหนดดังนี้
  - input เป็นแผนที่ความสูงของต้นไม้ที่ได้รับมาจาก drone โดยอ่านจาก text file
  - ใช้ภาษาอะไรก็ได้ โดยต้องเป็นโปรแกรมที่รับชื่อ text file และทำงานบน command line เท่านั้น
  - output เป็นจำนวนต้นไม้ที่ถูกมองเห็นจากด้านใดด้านหนึ่ง โดยพิมพ์ผลลัพท์ออกทางหน้าจอ (พิมพ์คำตอบเป็นเลขตัวเดียว ห้ามพิมพ์ข้อมูลอื่น ๆ)
  - ส่ง code ที่พร้อม run พร้อมระบุวิธี run ด้วย

ตัวอย่างการเรียกใช้งานโปรแกรม
```
my_program data.txt
```

ตัวอย่างเนื้อหา text file (data.txt)
```
655844596877978788798778877777789987786
856455588758889976697878877879779779689
444578757959986968899898977877897898996
647847566676868677789988787877988768889
485874865599879687987787778887979998689
487886855599677798796997889879897679696
686776559678687978778776988988789699989
888557455887878979766976998998988687796
558856869587978588698986777867769887997
564477446998579957778766777979969987668
765556457588956779786987668699667999986
586548486575968979869899899668696676796
```

ตัวอย่าง output
```
187
```

## วิธีรันไฟล์

python treehouse.py ชื่อไฟล์ข้อมูล

เช่น

python treehouse.py datatest.txt

python treehouse.py dataexample.txt