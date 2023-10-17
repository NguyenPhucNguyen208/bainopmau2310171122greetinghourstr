#region debai
"""
--- ma debai / id
greeting(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310171122greetinghourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/mb6ZrFw4pXW8DqeBA

--- debai / problem
Viết hàm 
  greeting(hour_str)
giúp chat bot in ra câu chào theo buổi sáng/chiều/tối trong ngày 
00:00AM  - 11:59AM Good morning!
12:00PM  - 05:59PM Good afternoon!
06:00PM  - 11:59PM Good evening!

Khi chạy với đầuvào / input  | Kếtquả đẩura / output  | Thứtự mẫuthử 
---------------------------- | ---------------------- | -----------
greeting(hour_str='6am')     | Good morning!          | 00

# AM / PM format
greeting('6am')              | Good morning!          | 01
greeting('6 am')             | Good morning!          | 02
greeting('6AM')              | Good morning!          | 03
greeting('6 AM')             | Good morning!          | 04

greeting('9pm')              | Good evening!          | 05
greeting('0900pm')           | Good evening!          | 06
greeting('09:00pm')          | Good evening!          | 07
greeting('09:00 pm')         | Good evening!          | 08
greeting('09:00 PM')         | Good evening!          | 09

greeting('1pm')              | Good afternoon!        | 10

# 24-hours format
greeting('06:00')            | Good morning!          | 11
greeting('0600')             | Good morning!          | 12
greeting('21:00')            | Good evening!          | 13
greeting('2100')             | Good evening!          | 14

"""
#endregion debai

#region bailam
def greeting(hour_str):
  for i in hour_str:
      if ord(i) >= 65 and ord(i) <= 122:
          n = 1
          break
      else:
          n = 0


  def loai_1 (hour_str):
      if 'a' in hour_str or "A" in hour_str:
          return "Good morning!"
      elif 'p' in hour_str or "P" in hour_str:
          if ':' in hour_str: 
            r = hour_str.split(":")[0]
            r = r.strip()
            r = int(r) + 12
            if r >= 12 and r <= 18:
                return "Good afternoon!"
            else:
                return "Good evening!"
          elif ":" not in hour_str :
            r = hour_str.split("p" or "P")[0]
            r = r.strip()
            r = int(r) + 12
            if r >= 12 and r <= 18:
                return "Good afternoon!"
            else:
                return "Good evening!"
  def loai_0 (hour_str) :
      if ':' in hour_str :
          a = hour_str.split(':')[0]
          a = a.strip()
          a = int(a)
          b = hour_str.split(':')[1]
          b = b.strip()
          b = int(b)
          if a >= 0 and a <= 11 :
              if b >= 0 and b <= 59 :
                  return "Good morning!"
              else : return "Good afternoon!"
          elif a <= 18 :
              if b >= 0 and b <= 59:
                  return "Good afternoon!"
              else :
                  return "Goon evening!"
          else :
              return "Good evening!"
      elif int(hour_str) >= 0 and int(hour_str) <= 1159 :
          return "Good morning!"
      elif int(hour_str) < 1800 :
          return "Good afternoon!"
      else :
          return "Good evening!"
  if n == 1:
      return (loai_1(hour_str))
  if n == 0:
      return (loai_0(hour_str))
#endregion bailam
